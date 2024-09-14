import requests
from bs4 import BeautifulSoup
import json
import re

def get_twitch_channel_info_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('meta', {'property': 'og:title'})
    name = title_tag.get('content', 'Nom non trouvé') if title_tag else 'Nom non trouvé'

    image_tag = soup.find('meta', {'property': 'og:image'})
    image = image_tag.get('content', 'Image non trouvée') if image_tag else 'Image non trouvée'

    # Essayer de trouver la description dans un script JSON
    script_tag = soup.find('script', text=re.compile('description'))
    if script_tag:
        try:
            # Rechercher le texte JSON à l'intérieur du script
            json_text = re.search(r'{"props".*}', script_tag.string).group(0)
            data = json.loads(json_text)
            description = data['props']['pageProps']['description']
        except (AttributeError, KeyError, json.JSONDecodeError):
            description = 'Description non trouvée'
    else:
        description = 'Description non trouvée'

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

    # Affichage des résultats
    print(json.dumps(channel_infos, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
