# ⚡ Sky Sports Async Scraper & Live Dashboard

A complete data pipeline that asynchronously scrapes the latest sports news from Sky Sports and displays them in a modern, interactive web dashboard using Streamlit.

## ✨ Features

- **Lightning-Fast Scraping**: Utilizes `httpx.AsyncClient` and `asyncio` for concurrent HTTP requests.
- **Deep Extraction**: Extracts headlines, URLs, categories, and cover images using `BeautifulSoup4`.
- **Interactive Dashboard**: A beautiful, dark-themed UI built with `Streamlit`.
- **Dynamic Filtering**: Filter news by category (e.g., Football, F1) via the sidebar using `Pandas`.
- **Ready for Deployment**: Includes all configurations (`requirements.txt`) needed for Streamlit Community Cloud deployment.

## 🛠️ Prerequisites

Make sure you have Python 3.7+ installed. First, install the required dependencies:

`pip install httpx beautifulsoup4 streamlit pandas`

*(Alternatively, if you have a requirements.txt file: `pip install -r requirements.txt`)*

## 🚀 How to Run Locally

1. **Clone the repository:**
   `git clone https://github.com/WeirdBlueFish/NewsScraper.git`
   `cd NewsScraper`

2. **Run the Scraper (Data Collection):**
   This will fetch the latest news and generate a `news_async.csv` file.
   `python main.py`

3. **Run the Streamlit Dashboard (UI):**
   This will launch the interactive web app in your default browser.
   `streamlit run app.py`

## 📂 Project Structure

- `main.py` - The asynchronous web scraper script.
- `app.py` - The Streamlit web application.
- `news_async.csv` - The extracted data (auto-generated).
- `requirements.txt` - List of Python dependencies.

## ⚠️ Disclaimer

This project is created for **educational purposes only**. Please respect the website's `robots.txt` and Terms of Service. Do not use this script to overload their servers with excessive requests.