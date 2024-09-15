import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

def clean_subscribers_text(text):
    # Nettoyage des caractères non imprimables comme \xa0 (espace insécable)
    text = text.replace('\xa0', ' ').strip()
    
    # Recherche du nombre d'abonnés avec le format typique
    match = re.search(r'(\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+)(?:\s*[-|]?\s*(?:k|K|m|M))?\s*abonnés', text)
    if match:
        return match.group(0).strip()
    return "Données abonnés non disponibles"

def get_channel_info_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupération des informations de base
    title_tag = soup.find('meta', {'property': 'og:title'})
    name = title_tag.get('content', 'Nom non trouvé') if title_tag else 'Nom non trouvé'

    meta_description = soup.find('meta', {'name': 'description'})
    description = meta_description.get('content', 'Description non trouvée') if meta_description else 'Description non trouvée'

    image_tag = soup.find('link', {'rel': 'image_src'})
    image = image_tag.get('href', 'Image non trouvée') if image_tag else 'Image non trouvée'
    
    # Extraction du texte brut de la page
    page_text = soup.get_text(separator=' ', strip=True)

    # Recherche et affichage des sections contenant le mot "abonnés" dans le texte brut
    matches = re.findall(r'.*?(\b\w+\b \b\w+\b \b\w+\b \b\w*\b \b\w*\b) abonnés.*?', page_text)
    subscribers_text = ""
    if matches:
        print(f"Texte brut contenant 'abonnés' pour l'URL {url}:")
        for match in matches:
            print(match)
            subscribers_text = match  

    # Recherche des balises <script> contenant du JSON
    script_tags = soup.find_all('script')
    for script in script_tags:
        script_content = script.string
        if script_content:
            # Recherche de structures JSON dans le contenu des balises <script>
            json_matches = re.findall(r'\{[^}]*"content":"[^"]*abonnés[^"]*"[^}]*\}', script_content)
            if json_matches:
                print(f"JSON contenant 'abonnés' pour l'URL {url}:")
                for json_text in json_matches:
                    try:
                        # Affichage du JSON brut
                        subscribers_text = json_text
                        print(json_text)
                    except json.JSONDecodeError:
                        print(f"Erreur lors de l'analyse du JSON pour l'URL {url}.")

    channel_id = url.split('/')[-1]

    # Nettoyage du champ subscribers après extraction
    cleaned_subscribers_text = clean_subscribers_text(subscribers_text)

    return {
        'id': channel_id,
        'name': name,
        'description': description,
        'image': image,
        'link': url,
        'subscribers': cleaned_subscribers_text
    }

def read_urls_from_web(url):
    response = requests.get(url)
    return [line.strip() for line in response.text.splitlines() if line.strip()]

def main():
    list_url = 'https://raw.githubusercontent.com/Frozenka/hacking-france/main/src/assets/misc/liste_youtube.txt'
    urls = read_urls_from_web(list_url)

    channel_infos = []

    for url in urls:
        time.sleep(2)  # Attendre 2 secondes entre les requêtes
        try:
            channel_info = get_channel_info_from_url(url)
            channel_infos.append(channel_info)
        except Exception as e:
            print(f"Erreur lors de la récupération des informations pour {url} : {e}")

    print(f"Résultats: {channel_infos}")

    output_file_path = os.path.join('src', 'assets', 'misc', 'channels_info.json')
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(channel_infos, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
