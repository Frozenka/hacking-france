import requests
from bs4 import BeautifulSoup
import json

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

def read_urls_from_web(url):
    """
    Lit les URLs des chaînes YouTube depuis une URL web.
    """
    response = requests.get(url)
    urls = [line.strip() for line in response.text.splitlines() if line.strip()]
    return urls

def main():
    """
    Fonction principale qui gère le traitement des URLs et l'écriture des informations dans un fichier JSON.
    """
    # URL de la liste des chaînes YouTube
    list_url = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_youtube.txt'
    
    # Lire les URLs depuis l'URL web
    urls = read_urls_from_web(list_url)
    
    channel_infos = []
    
    for url in urls:
        try:
            # Récupérer les informations de la chaîne
            channel_info = get_channel_info_from_url(url)
            channel_infos.append(channel_info)
        except Exception as e:
            print(f"Erreur lors de la récupération des informations pour {url} : {e}")

    # Écrire les données JSON dans un fichier
    with open('channels_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(channel_infos, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
