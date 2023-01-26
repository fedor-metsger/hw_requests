import json
import requests

JSON_URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
HEROUS_TO_CHECK = {"Hulk", "Captain America", "Thanos"}

def main():
    herous = requests.get(JSON_URL).json()

    name, intell = None, 0
    for h in herous:
        if h["name"] in HEROUS_TO_CHECK:
            if not name or h["powerstats"]["intelligence"] > intell:
                name = h["name"]
                intell = h["powerstats"]["intelligence"]

    print(f"Самый умный супергерой - {name} с \"intelligence\" = {intell}")

if __name__ == "__main__":
    main()