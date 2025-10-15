from enum import nonmember

import requests
from bs4 import BeautifulSoup
import csv
import time
import random
from fake_useragent import UserAgent
from urllib.parse import urljoin

# Konfiguration
input = input("nach welchem Artikel suchst du?: ")

START_URL = "https://www.amazon.de/s?k="+input  # Beispiel-Suche; ersetzen
OUTPUT_CSV = "amazon_products.csv"
DELAY_MIN = 2.0
DELAY_MAX = 10.0
HEADERS = {"User-Agent": UserAgent().random, "Accept-Language": "de-DE,de;q=0.9,en;q=0.8"}

def fetch(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print("Fehler beim Laden:", e)
        return None

def parse_search_page(html, base_url="https://www.amazon.de/"):
    soup = BeautifulSoup(html, "html.parser")
    results = []

    # Amazon nutzt unterschiedliche Container; hier ein allgemein brauchbarer Ansatz
    items = soup.select("div.s-result-item[data-asin]")  # s-result-item mit data-asin
    for it in items:
        asin = it.get("data-asin", "").strip()
        if not asin:
            continue
        # Link & Titel aus dem <a> Tag extrahieren
        link_tag = it.select_one("a.a-link-normal.a-text-normal")

        if link_tag:
            link = urljoin(base_url, link_tag.get("href"))

            # Titeltext ist im <span> innerhalb des <a>
            title_span = it.select_one("span .a-link-normal.a-text-normal")
            title = title_span.get_text(strip=True) if title_span else None
        else:
            link = None
            title = None

        # Preis (verschiedene Layouts)
        price_whole = it.select_one("span.a-price > span.a-offscreen")
        price = price_whole.get_text(strip=True) if price_whole else None
        #img
        img_tag = it.select_one("img.s-image")
        if img_tag:
            img_url = img_tag.get("src") or img_tag.get("data-src") or img_tag.get("data-old-hires")
        else:

            img_tag2 = it.find("img")
            img_url = img_tag2.get("src") if img_tag2 and img_tag2.get("src") else None

        # Fallbacks
        if not title and it.select_one("span.a-size-medium"):
            title = it.select_one("span.a-size-medium").get_text(strip=True)

        results.append({
            "asin": asin,
            "title": title,
            "price": price,
            "link": link,
            "img_url": img_url
        })
    return results

def save_to_csv(rows, filename):
    keys = ["asin", "title", "price", "link", "img_url"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print(f"Gespeichert: {filename}")

def main():
    print("Starte Crawl:", START_URL)
    html = fetch(START_URL)
    if not html:
        return

    results = parse_search_page(html)
    print(f"Gefundene Items auf Seite: {len(results)}")

    save_to_csv(results, OUTPUT_CSV)

    time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))

if __name__ == "__main__":
    main()
