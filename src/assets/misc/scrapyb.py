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
    if title_tag:
        name = title_tag.get('content', 'Nom non trouvé')
    else:
        name = 'Nom non trouvé'
    
    # Extraire la description de la chaîne
    meta_description = soup.find('meta', {'name': 'description'})
    if meta_description:
        description = meta_description.get('content', 'Description non trouvée')
    else:
        description = 'Description non trouvée'
    
    # Extraire l'image de la chaîne
    image_tag = soup.find('link', {'rel': 'image_src'})
    if image_tag:
        image = image_tag.get('href', 'Image non trouvée')
    else:
        image = 'Image non trouvée'

    # Extraire l'ID de la chaîne à partir de l'URL (URL personnalisée ne contient pas directement l'ID)
    channel_id = url.split('/')[-1]  # Pour les URLs sous forme de handle, cet ID peut ne pas être présent
    
    return {
        'id': channel_id,
        'name': name,
        'description': description,
        'image': image,
        'link': url
    }

def main():
    """
    Fonction principale qui gère l'entrée utilisateur et l'affichage des informations.
    """
    # Lire la liste des URL de chaînes YouTube
    url_list_file = 'src/assets/misc/liste_youtube.txt'
    with open(url_list_file, 'r') as file:
        urls = file.read().splitlines()
    
    channels_info = []
    
    for url in urls:
        try:
            # Récupérer les informations de la chaîne
            channel_info = get_channel_info_from_url(url)
            channels_info.append(channel_info)
        except Exception as e:
            print(f"Erreur lors de la récupération des informations pour {url}: {e}")
    
    # Écrire les informations dans le fichier JSON
    file_path = '/chaines_youtubes.json'
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(channels_info, file, indent=2, ensure_ascii=False)
    
    print(f"Les informations des chaînes YouTube ont été écrites dans : {os.path.abspath(file_path)}")

if __name__ == "__main__":
    main()
