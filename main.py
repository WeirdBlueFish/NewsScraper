#_______________
# Imports:

from bs4 import BeautifulSoup
import asyncio
import httpx
import csv

#_______________
# Setting:

websites = [
    {
        "category" : "Football",
        "url" : "https://www.skysports.com/football/news"
    },
    {
        "category" : "F1",
        "url" : "https://www.skysports.com/f1/news"
    },
    {
        "category" : "Golf",
        "url" : "https://www.skysports.com/golf/news"
    },
    {
        "category" : "Racing",
        "url" : "https://www.skysports.com/racing/news"
    },
    {
        "category" : "NFL",
        "url" : "https://www.skysports.com/nfl/news"
    },
    {
        "category" : "Tennis",
        "url" : "https://www.skysports.com/tennis/news"
    },
]

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

#_______________
# Base:

async def fetch_data(url):
    async with httpx.AsyncClient(headers=headers ,timeout=10.0) as c:
        try:
            print(f"🔄 Fetching data from: {url}")

            response = await c.get(url)

            response.raise_for_status()

            return response.text

        except httpx.HTTPError as exc:
            print(f"Http Error: {exc}")
        
        except httpx.RequestError as exc:
            print(f"Connection Error: {exc}") 
        
        except httpx.NetworkError as exc:
            print(f"Network Error: {exc}")

    return None
    

def scrape_data(response, category):
    if not response:
        return []
    
    data = BeautifulSoup(response, 'html.parser')

    newses = data.find_all('div', class_='sdc-site-tile')

    news = []
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

            news.append([category, headline, link])

    return news            

#_______________
# Run:

async def main():
    with open("news.csv", 'w', newline='', encoding='utf-8') as writer:
        writer = csv.writer(writer)
        writer.writerow(['Categorycategory' ,'Title', 'Link'])

        tasks = [fetch_data(site['url']) for site in websites]

        html_responses = await asyncio.gather(*tasks)

        for site, html in zip(websites, html_responses):
            if html:
                extracted_news = scrape_data(html, site['category'])
                for news_item in extracted_news:
                    writer.writerow(news_item)

        print(f"all data saved in news.csv")

if __name__ == "__main__":
    asyncio.run(main())