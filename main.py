#_______________
# Imports:

import httpx
from bs4 import BeautifulSoup

#_______________
# Setting:

websites = [
    {
        "name" : "Sky Sports",
        "url" : "https://www.skysports.com/football/news"
    }
]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

#_______________
# Base:

def fetch_data(url):
    with httpx.Client(headers=headers ,timeout=10.0) as c:
        try:
            print(f"fetching data...")

            response = c.get(url)

            response.raise_for_status()

            print(f"html successfully fetched.")
            
            return response.text

        except httpx.HTTPError as exc:
            return f"Http Error: {exc}"
        
        except httpx.RequestError as exc:
            return f"Connection Error: {exc}"
        
        except httpx.NetworkError as exc:
            return f"Network Error: {exc}"
    

def scrape_data(response):
    data = BeautifulSoup(response, 'html.parser')

    newses = data.find_all('div', class_='sdc-site-tile')
    print(f"{len(newses)} news found.")
    print(f"Scraped News: \n")

    for index, item in enumerate(newses, 1):
        # پیدا کردن تگ تیتر داخل این کارت خبر
        headline_tag = item.find('span', class_='sdc-site-tile__headline-text')
        # پیدا کردن تگ لینک داخل این کارت خبر
        link_tag = item.find('a', class_='sdc-site-tile__headline-link')

        if headline_tag and link_tag:
            headline = headline_tag.text.strip()
            link = link_tag.get('href')

            if link.startswith('/'):
                link = 'https://www.skysports.com' + link

            print(f"{index}. ⚽ {headline}")
            print(f"🔗 Link: {link}")
            print("-" * 40)

#_______________
# Run:

if __name__ == "__main__":
    r = fetch_data(websites[0]['url'])
    scrape_data(r)