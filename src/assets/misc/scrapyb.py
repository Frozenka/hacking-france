import os
import json
import requests
from bs4 import BeautifulSoup

def fetch_youtube_channels():
    url = "https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_youtube.txt"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def fetch_channel_info(channel_url):
    # Utiliser BeautifulSoup pour extraire les informations de la chaîne
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemple de données, vous devrez ajuster le parsing en fonction du contenu réel
    return {
        "id": channel_url.split('/')[-1],
        "name": "Nom de la chaîne",
        "description": "Description de la chaîne",
        "image": "URL de l'image",
        "link": channel_url
    }

def main():
    channels = fetch_youtube_channels()
    channel_info_list = []

    for channel in channels:
        info = fetch_channel_info(channel)
        channel_info_list.append(info)

    file_path = os.path.join(os.path.dirname(__file__), 'chaines_youtubes.json')

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(channel_info_list, file, ensure_ascii=False, indent=4)

    print(f"Les informations des chaînes YouTube ont été écrites dans : {file_path}")

if __name__ == "__main__":
    main()
