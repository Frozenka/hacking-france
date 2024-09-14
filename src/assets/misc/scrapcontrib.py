import requests
from bs4 import BeautifulSoup
import json
import os

# Fonction pour récupérer les informations des contributeurs GitHub
def get_github_contributors_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    contributors = []

    for img in soup.find_all('img', class_='avatar circle'):
        avatar_url = img.get('src')
        username = img.get('alt').replace('@', '')

        if avatar_url and username:
            avatar_url = avatar_url.split('?')[0]
            contributors.append({
                'username': username,
                'avatar_url': avatar_url
            })

    return {'data': contributors}

def main():
    # URL des contributeurs GitHub
    github_url = 'https://github.com/Frozenka/hacking-france'

    # Récupération des contributeurs GitHub
    github_contributors = get_github_contributors_images(github_url)

    # Écriture des informations des contributeurs GitHub dans le fichier
    github_output_file_path = os.path.join('src', 'assets', 'cards.json')
    with open(github_output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(github_contributors, json_file, indent=2, ensure_ascii=False)

    print(f"Les informations des contributeurs GitHub ont été écrites dans {github_output_file_path}")

if __name__ == "__main__":
    main()
