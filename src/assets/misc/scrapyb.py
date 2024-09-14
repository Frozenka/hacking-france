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
    name = title_tag.get('content', 'Nom non trouvé') if title_tag else 'Nom non trouvé'
    
    # Extraire la description de la chaîne
    meta_description = soup.find('meta', {'name': 'description'})
    description = meta_description.get('content', 'Description non trouvée') if meta_description else 'Description non trouvée'
    
    # Extraire l'image de la chaîne
    image_tag = soup.find('link', {'rel': 'image_src'})
    image = image_tag.get('href', 'Image non trouvée') if image_tag else 'Image non trouvée'

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
    Fonction principale qui gère la lecture de l'URL des chaînes, le scraping et l'écriture du fichier JSON.
    """
    # URL du fichier liste des chaînes
    list_url = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_youtube.txt'
    
    # Télécharger la liste des chaînes
    response = requests.get(list_url)
    urls = response.text.strip().split('\n')
    
    # Scraper les informations pour chaque chaîne
    new_data = []
    for url in urls:
        channel_info = get_channel_info_from_url(url.strip())
        new_data.append(channel_info)
    
    # Écrire les nouvelles données dans le fichier JSON
    with open('/src/assets/misc/channels_info.json', 'w') as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)
    
    print("Les informations des chaînes ont été mises à jour.")

if __name__ == "__main__":
    main()
#merci ChatGPT !
