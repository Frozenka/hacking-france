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
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Fetching info for: {channel_url}")
    # Simulate actual scraping here; replace placeholders with real scraping logic
    return {
        "id": channel_url.split('/')[-1],
        "name": "Actual Channel Name",  # Replace with actual data
        "description": "Actual Description",  # Replace with actual data
        "image": "Actual Image URL",  # Replace with actual data
        "link": channel_url
    }

def main():
    channels = fetch_youtube_channels()
    channel_info_list = []

    for channel in channels:
        info = fetch_channel_info(channel)
        channel_info_list.append(info)
        print(f"Fetched info: {info}")

    file_path = 'src/assets/misc/channels_info.json'
    
    # Debug print statements
    print(f"Writing to file: {file_path}")
    print(f"Directory contents: {os.listdir(os.path.dirname(file_path))}")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(channel_info_list, file, ensure_ascii=False, indent=4)

    print(f"Les informations des chaînes YouTube ont été écrites dans : {file_path}")

if __name__ == "__main__":
    main()
