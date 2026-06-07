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

#_______________
# Base:

def fetch_data(url):
    response = httpx.get(url)
    
    return response.status_code


#_______________
# Run:

if __name__ == "__main__":
    r = fetch_data(websites[0]['url'])
    print(r)