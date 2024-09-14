import requests
from bs4 import BeautifulSoup
import json
import os

def get_channel_info_from_url(url):
    """
    Récupère les informations de la chaîne YouTube en scrappant la page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraire le nom de la chaîne
    title_tag = soup.find('meta', {'property': 'og:title'})
    name = title_tag.get('content', 'Nom non trouvé') if title_tag else 'Nom non trouvé'
    
    # Extraire la description de la chaîne
    meta_description = soup.find('meta', {'name': 'description'})
    description = meta_description.get('content', 'Description non trouvée') if meta_description else 'Description non trouvée'
    
    # Extraire l'image de la chaîne
    image_tag = soup.find('link', {'rel': 'image_src'})
    image = image_tag.get('href', 'Image non trouvée') if image_tag else 'Image non trouvée'

    # Extraire l'ID de la chaîne
    channel_id = url.split('/')[-1]
    
    return {
        'id': channel_id,
        'name': name,
        'description': description,
        'image': image,
        'link': url
    }

def main():
    """
    Fonction principale qui récupère les informations des chaînes et les écrit dans un fichier JSON.
    """
    # URL de la liste des chaînes YouTube
    url_list = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_youtube.txt'
    response = requests.get(url_list)
    urls = response.text.splitlines()

    all_channels = []
    for url in urls:
        try:
            channel_info = get_channel_info_from_url(url)
            all_channels.append(channel_info)
        except Exception as e:
            print(f"Erreur lors du traitement de {url}: {e}")

    # Chemin vers le fichier JSON
    file_path = 'src/assets/misc/channels_info.json'

    # Écrire les informations dans le fichier JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(all_channels, file, indent=2, ensure_ascii=False)

    # Afficher l'emplacement du fichier JSON
    print(f"Les informations des chaînes YouTube ont été écrites dans : {os.path.abspath(file_path)}")

if __name__ == "__main__":
    main()
