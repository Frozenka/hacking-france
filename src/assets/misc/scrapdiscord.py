import requests
from bs4 import BeautifulSoup
import json
import os  # Importer le module os

# URL de la liste des serveurs Discord
discord_urls_file = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_discord.txt'

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

        # Extraction de la description
        description_tag = soup.find('meta', {'name': 'description'})
        description = description_tag['content'] if description_tag else 'Description non disponible'

        # Extraction du nombre de membres
        # Exemple: "Découvre la communauté FransoTeam sur Discord - discute avec 378 autres membres et profite du chat vocal et textuel gratuit."
        if ' avec ' in description and ' membres' in description:
            description_text = description.split(' avec ')[0].strip()
            members_text = description.split(' avec ')[1].split(' membres')[0].strip()
            members = ''.join(filter(str.isdigit, members_text))
        else:
            description_text = description
            members = 'Membres non disponibles'

        # Extraction du logo
        image_tag = soup.find('meta', {'property': 'og:image'})
        image_url = image_tag['content'] if image_tag else 'Logo non disponible'

        # Extraction du nom
        title_tag = soup.find('meta', {'property': 'og:title'})
        title = title_tag['content'] if title_tag else 'Nom non disponible'

        return {
            'name': title.strip(),
            'description': f"Rejoignez notre serveur Discord dédié aux CTF (Capture The Flag) pour les passionnés de sécurité informatique | {members} membres | {members} members",
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
