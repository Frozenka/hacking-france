import requests
from bs4 import BeautifulSoup
import json
import os

def get_twitch_channel_info_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('meta', {'property': 'og:title'})
    name = title_tag.get('content', 'Nom non trouvé') if title_tag else 'Nom non trouvé'

    meta_description = soup.find('meta', {'name': 'description'})
    description = meta_description.get('content', 'Description non trouvée') if meta_description else 'Description non trouvée'

    image_tag = soup.find('meta', {'property': 'og:image'})
    image = image_tag.get('content', 'Image non trouvée') if image_tag else 'Image non trouvée'

    channel_id = url.split('/')[-1]

    return {
        'id': channel_id,
        'name': name,
        'description': description,
        'image': image,
        'link': url
    }

def read_urls_from_web(url):
    response = requests.get(url)
    return [line.strip() for line in response.text.splitlines() if line.strip()]

def main():
    list_url = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_twitch.txt'
    urls = read_urls_from_web(list_url)

    channel_infos = []

    for url in urls:
        try:
            channel_info = get_twitch_channel_info_from_url(url)
            channel_infos.append(channel_info)
        except Exception as e:
            print(f"Erreur lors de la récupération des informations pour {url} : {e}")

    # Écriture des résultats dans un fichier JSON
    output_file_path = os.path.join('src', 'assets', 'misc', 'twitch_channels_info.json')
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(channel_infos, json_file, indent=2, ensure_ascii=False)

    print(f"resultat : {channel_infos}")
    print(f"Les informations ont été écrites dans {output_file_path}")

if __name__ == "__main__":
    main()
