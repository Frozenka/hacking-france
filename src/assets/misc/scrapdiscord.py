import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

# URL de la liste des serveurs Discord
discord_urls_file = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_discord.txt'

# Définir le chemin du fichier de sortie
output_file_path = os.path.join('src', 'assets', 'misc', 'discord_servers_info.json')

# URL de l'image par défaut
default_image_url = 'https://logo-marque.com/wp-content/uploads/2020/12/Discord-Logo.png'

def fetch_discord_urls(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  # Forcer l'encodage UTF-8
        response.raise_for_status()
        urls = response.text.splitlines()
        # Validation basique des URL
        valid_urls = [u for u in urls if re.match(r'https://discord\.com/invite/.+', u)]
        return valid_urls
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des URLs: {e}")
        return []

def extract_discord_info(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  # Forcer l'encodage UTF-8
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraction du nom du serveur
        title_tag = soup.find('meta', {'property': 'og:title'})
        title = title_tag['content'] if title_tag else 'Nom non disponible'

        # Extraction de la description
        description_tag = soup.find('meta', {'name': 'description'})
        description = description_tag['content'] if description_tag else 'Description non disponible'

        # Extraction du nombre de membres
        members_match = re.search(r'(\d+(?:,\d+)?)\s*members?|(\d+(?:,\d+)?)\s*autres membres', description, re.IGNORECASE)
        members = members_match.group(1).replace(',', '') if members_match else 'Membres non disponibles'

        # Retirer le nombre de membres de la description
        description_text = re.sub(r'(\d+(?:,\d+)?)\s*members?|(\d+(?:,\d+)?)\s*autres membres', 'Membres non disponibles', description, flags=re.IGNORECASE)

        # Extraction de l'image
        image_tag = soup.find('meta', {'property': 'og:image'})
        image_url = image_tag['content'] if image_tag else default_image_url

        return {
            'name': title.strip(),
            'description': f"{description_text.strip()} | {members} membres",
            'members': members.strip(),
            'image': image_url.strip(),
            'link': url.strip()
        }
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des infos pour {url}: {e}")
    except Exception as e:
        print(f"Erreur inconnue pour {url}: {e}")
    return None  # Ne pas inclure cette entrée dans le fichier JSON

def main():
    discord_urls = fetch_discord_urls(discord_urls_file)
    discord_channels = []

    for url in discord_urls:
        info = extract_discord_info(url)
        if info is not None:  # Inclure seulement si info n'est pas None
            discord_channels.append(info)
            print(f"Infos récupérées pour {url}: {info}")

        # Ajouter un délai entre les requêtes pour éviter les problèmes de surutilisation
        time.sleep(2)  # Délai de 2 secondes (ajuster selon les besoins)

    # Écriture des résultats dans un fichier JSON
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(discord_channels, json_file, indent=2, ensure_ascii=False)

    print(f"Les informations des serveurs Discord ont été sauvegardées dans '{output_file_path}'.")

if __name__ == "__main__":
    main()
