import requests
import json

url = "https://raw.githubusercontent.com/share424/Indonesian-Text-to-Image-synthesis-with-Sentence-BERT-and-FastGAN/refs/heads/master/dataset/indo_cub_200_2011_captions.json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    with open("indo_cub_200_2011_captions.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("JSON data saved.")
else:
    print(f"Failed to fetch data: {response.status_code}")
