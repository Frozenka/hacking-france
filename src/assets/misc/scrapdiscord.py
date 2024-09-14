import requests
from bs4 import BeautifulSoup
import json
import os

# URL de la liste des serveurs Discord
discord_urls_file = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_discord.txt'

# Définir le chemin du fichier de sortie
output_file_path = os.path.join('src', 'assets', 'misc', 'discord_servers_info.json')

# URL de l'image par défaut
default_image_url = 'https://logo-marque.com/wp-content/uploads/2020/12/Discord-Logo.png'

def fetch_discord_urls(url):
    response = requests.get(url)
    response.encoding = 'utf-8'  # Forcer l'encodage UTF-8
    response.raise_for_status()
    return response.text.splitlines()

def extract_discord_info(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'  # Forcer l'encodage UTF-8
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraction des informations à partir du code source HTML
        description_tag = soup.find('meta', {'name': 'description'})
        description = description_tag['content'] if description_tag else 'Description non disponible'

        # Extraction du nombre de membres
        description_parts = description.split('|')
        if len(description_parts) > 1:
            members_text = description_parts[-1].strip()
            members = ''.join(filter(str.isdigit, members_text))
        else:
            members = 'Membres non disponibles'

        # Retirer le nombre de membres de la description
        description_text = description_parts[0].strip() if len(description_parts) > 1 else description

        # Extraction du logo
        image_tag = soup.find('meta', {'property': 'og:image'})
        image_url = image_tag['content'] if image_tag else default_image_url

        # Extraction du nom
        title_tag = soup.find('meta', {'property': 'og:title'})
        title = title_tag['content'] if title_tag else 'Nom non disponible'

        return {
            'name': title.strip(),
            'description': f"{description_text} | {members} members",
            'members': members.strip(),
            'image': image_url.strip(),
            'link': url.strip()
        }
    except Exception as e:
        print(f"Erreur pour {url}: {e}")
        return None  # Ne pas inclure cette entrée dans le fichier JSON

def main():
    discord_urls = fetch_discord_urls(discord_urls_file)
    discord_channels = []
    
    for url in discord_urls:
        info = extract_discord_info(url)
        if info is not None:  # Inclure seulement si info n'est pas None
            discord_channels.append(info)
            print(f"Infos récupérées pour {url}: {info}")

    # Écriture des résultats dans un fichier JSON
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(discord_channels, json_file, indent=2, ensure_ascii=False)

    print(f"Les informations des serveurs Discord ont été sauvegardées dans '{output_file_path}'.")

if __name__ == "__main__":
    main()
