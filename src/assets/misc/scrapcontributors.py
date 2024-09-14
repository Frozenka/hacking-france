import requests
import json

# URL du dépôt GitHub
repo_url = 'https://api.github.com/repos/Frozenka/hacking-france/contributors'

def get_contributors(repo_url):
    # Envoyer une requête GET à l'API GitHub
    response = requests.get(repo_url)
    if response.status_code == 200:
        # Extraire les données JSON
        contributors = response.json()
        # Préparer les données au format souhaité
        data = []
        for contributor in contributors:
            user_data = {
                "username": contributor['login'],
                "avatar_url": contributor['avatar_url']
            }
            data.append(user_data)
        return {"data": data}
    else:
        print(f"Erreur de récupération des contributeurs : {response.status_code}")
        return {"data": []}

if __name__ == "__main__":
    contributors_data = get_contributors(repo_url)
    # Sauvegarder les données dans src/assets/cards.json
    with open('src/assets/cards.json', 'w') as f:
        json.dump(contributors_data, f, indent=4)
    print("Les contributeurs ont été sauvegardés dans 'src/assets/cards.json'.")
