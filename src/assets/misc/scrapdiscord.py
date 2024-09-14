def extract_discord_info(url):
    if not is_valid_url(url):
        print(f"URL invalide : {url}")
        return None

    response = requests.get(url)
    response.encoding = 'utf-8'  # Forcer l'encodage UTF-8
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraction des informations à partir du code source HTML
    description_tag = soup.find('meta', {'name': 'description'})
    description = description_tag['content'] if description_tag else 'Description non disponible'

    # Supprimer le texte à partir de "- discute avec"
    description = re.sub(r'-\s*discute\s*avec.*$', '', description).strip()

    # Si le caractère "|" est présent, supprimer tout ce qui suit
    if "|" in description:
        description = description.split('|')[0].strip()

    # Recherche du nombre de membres dans la description
    members_match = re.search(r'Discord\s*(.*?)\s*autres\s*membres\s*et\s*profite\s*du\s*chat\s*vocal\s*et\s*textuel\s*gratuit', description, re.IGNORECASE)
    if members_match:
        members_text = members_match.group(1).strip()
        # Retirer le texte "- discute avec" s'il est présent
        members = re.sub(r'-\s*discute\s*avec\s*', '', members_text).strip() + ' membres'
    else:
        # Recherche d'une autre méthode pour extraire le nombre de membres
        members_match = re.search(r'\|\s*(\d+)\s*(membres|members)', description, re.IGNORECASE)
        if members_match:
            members = members_match.group(1).strip() + ' membres'
        else:
            members = 'Données non disponibles'

    # Extraction du logo
    image_tag = soup.find('meta', {'property': 'og:image'})
    image_url = image_tag['content'] if image_tag else default_image_url

    # Extraction du nom
    title_tag = soup.find('meta', {'property': 'og:title'})
    title = title_tag['content'] if title_tag else 'Nom non disponible'

    return {
        'name': title.strip(),
        'description': description,
        'members': members,
        'image': image_url.strip(),
        'link': url.strip()
    }
