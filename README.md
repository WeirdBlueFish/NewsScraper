# ⚡ Sky Sports Async Web Scraper

A fast and efficient asynchronous web scraper built with Python. This script extracts the latest news headlines and links from the Sky Sports website (Football and F1 sections) and exports them into a clean CSV file.

By utilizing `asyncio` and `httpx`, this scraper performs concurrent HTTP requests, making it significantly faster than traditional synchronous scrapers.

## ✨ Features

- **Asynchronous Scraping**: Uses `httpx.AsyncClient` and `asyncio` to fetch multiple pages concurrently.
- **HTML Parsing**: Uses `BeautifulSoup4` to accurately navigate the DOM and extract specific elements.
- **Categorized Data**: Automatically tags scraped news with its corresponding category (e.g., Football, F1).
- **CSV Export**: Saves the extracted data (Category, Title, URL) into a standard UTF-8 encoded `.csv` file.
- **Robust Error Handling**: Safely manages HTTP, connection, and network errors without crashing.

## 🛠️ Prerequisites

Before running the script, make sure you have Python 3.7+ installed. Then, install the required third-party libraries:

`pip install httpx beautifulsoup4`

## 🚀 How to Run

1. Clone this repository to your local machine:
   `git clone https://github.com/yourusername/sky-sports-scraper.git`
   `cd sky-sports-scraper`

2. Run the Python script:
   `python main.py`
   *(Note: Replace `main.py` with the actual name of your Python file if it's different).*

3. Once the execution is complete, a file named `news_async.csv` will be generated in the root directory.

## 📊 Output Example

The generated CSV file will look like this:

| Category | Title | Link |
| :--- | :--- | :--- |
| Football | Tuchel frustrated by 'freestyling' as NZ boss says... | `https://www.skysports.com/football/...` |
| Football | Kane goal masks 'poor England performance' | `https://www.skysports.com/football/...` |
| F1 | Latest F1 news and race updates... | `https://www.skysports.com/f1/...` |

## ⚙️ Configuration

You can easily add more categories or change the target URLs by modifying the `websites` list inside the script:

`websites = [`
    `{`
        `"category" : "Football",`
        `"url" : "https://www.skysports.com/football/news"`
    `},`
    `{`
        `"category" : "F1",`
        `"url" : "https://www.skysports.com/f1/news"`
    `}`
`]`

## ⚠️ Disclaimer

This project is created for **educational purposes only**. Please respect the website's `robots.txt` and Terms of Service. Do not use this script to overload their servers with excessive requests.