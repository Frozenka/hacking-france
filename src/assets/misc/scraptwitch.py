import requests
from bs4 import BeautifulSoup
import json
import os  # Importer le module os

# URL de la liste des serveurs Discord
discord_urls_file = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/discord.txt'

# Définir le chemin du fichier de sortie
output_file_path = os.path.join('src', 'assets', 'misc', 'discord_servers_info.json')

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
        members_text = description.split('|')[-1].strip() if '|' in description else 'Membres non disponibles'
        members = ''.join(filter(str.isdigit, members_text))

        # Extraction du logo
        image_tag = soup.find('meta', {'property': 'og:image'})
        image_url = image_tag['content'] if image_tag else 'Logo non disponible'

        # Extraction du nom
        title_tag = soup.find('meta', {'property': 'og:title'})
        title = title_tag['content'] if title_tag else 'Nom non disponible'

        return {
            'name': title.strip(),
            'description': description.strip(),
            'members': members.strip(),
            'image': image_url.strip(),
            'link': url.strip()
        }
    except Exception as e:
        print(f"Erreur pour {url}: {e}")
        return {
            'name': 'Erreur',
            'description': f"Erreur lors de la récupération des informations: {e}",
            'members': 'N/A',
            'image': 'N/A',
            'link': url
        }

def main():
    discord_urls = fetch_discord_urls(discord_urls_file)
    discord_channels = []
    
    for url in discord_urls:
        info = extract_discord_info(url)
        discord_channels.append(info)
        print(f"Infos récupérées pour {url}: {info}")

    # Écriture des résultats dans un fichier JSON
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(discord_channels, json_file, indent=2, ensure_ascii=False)

    print(f"Les informations des serveurs Discord ont été sauvegardées dans '{output_file_path}'.")

if __name__ == "__main__":
    main()
