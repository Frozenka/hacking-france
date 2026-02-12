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

    subscribers_text = ""

    # 1) Tentative principale : chercher la valeur de "subscriberCountText"
    #    dans les gros blobs JSON que YouTube met dans des <script>.
    script_tags = soup.find_all('script')
    for script in script_tags:
        script_content = script.string or ""
        if "subscriberCountText" in script_content and "abonnés" in script_content:
            match = re.search(
                r'"subscriberCountText"\s*:\s*\{[^}]*"simpleText"\s*:\s*"([^"]*abonnés)"',
                script_content
            )
            if match:
                subscribers_text = match.group(1)
                break

    # 2) Fallback : si on n’a rien trouvé dans le JSON, on essaie dans le texte brut
    if not subscribers_text:
        page_text = soup.get_text(separator=' ', strip=True)
        match = re.search(r'([0-9][0-9\s.,]*(?:[kKmM])?\s*abonnés)', page_text)
        if match:
            subscribers_text = match.group(1)

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
        try:
            channel_info = get_channel_info_from_url(url)
            time.sleep(2)  # Attendre 2 secondes entre les requêtes
            channel_infos.append(channel_info)
        except Exception as e:
            print(f"Erreur lors de la récupération des informations pour {url} : {e}")

    print(f"Résultats: {channel_infos}")

    output_file_path = os.path.join('src', 'assets', 'misc', 'channels_info.json')
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(channel_infos, json_file, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
