import requests
from bs4 import BeautifulSoup

BASE_URL = "https://dramacool.com.tr/"

def scrape_dramacool():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {"dramas": [], "kshows": [], "movies": []}

    # Extract recently added dramas
    for item in soup.select(".left-tab-1 .list-episode-item li"):
        data["dramas"].append({
            "name": item.find("h2", class_="title").text.strip(),
            "status": item.find("span", class_="type").text.strip(),
            "episode": item.find("span", class_="ep").text.strip(),
            "link": item.a["href"],
            "updated_time": item.find("span", class_="time").text.strip()
        })

    # Extract recently added KShows
    for item in soup.select(".left-tab-3 .list-episode-item li"):
        data["kshows"].append({
            "name": item.find("h2", class_="title").text.strip(),
            "status": item.find("span", class_="type").text.strip(),
            "episode": item.find("span", class_="ep").text.strip(),
            "link": item.a["href"],
            "updated_time": item.find("span", class_="time").text.strip()
        })

    # Extract recently added movies
    for item in soup.select(".left-tab-2 .list-episode-item li"):
        data["movies"].append({
            "name": item.find("h2", class_="title").text.strip(),
            "status": item.find("span", class_="type").text.strip(),
            "link": item.a["href"],
            "updated_time": item.find("span", class_="time").text.strip()
        })

    return data
