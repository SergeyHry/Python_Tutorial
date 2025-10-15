import html

from bs4 import BeautifulSoup
import requests
r = requests.get("https://python.beispiel.programmierenlernen.io/index.php")
doc = BeautifulSoup(r.text, "html.parser")
Emojis = {}
for card in doc.select(".card"):
    Emojis = (f"{card.select_one(".emoji").text}:{card.select_one(".card-text").text}")
    print(Emojis)
for i in doc:
    print(i)
    image = doc.select_one("img").attrs["src"]