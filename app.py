#_____________________
# Imports:

import streamlit as st
import pandas as pd
from main import *

#______________________
# App:

st.set_page_config(page_title="Sky Sports News", page_icon="⚽", layout="wide")

st.markdown("""
<style>
    .news-card {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }
    .news-card:hover {
        transform: translateY(-5px);
    }
    .news-category {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .news-title {
        color: #ffffff !important;
        font-size: 18px;
        font-weight: 600;
        text-decoration: none;
        line-height: 1.4;
    }
    .news-title:hover {
        color: #ff4b4b !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Sky Sports Live News Hub")
st.markdown("Newses scraped by beautifulsoup & httpx")
st.divider()


@st.cache_data
def load_data():
    return pd.read_csv("news.csv")


try:

    df = load_data()

    st.sidebar.header("Filter")

    unique_categories = df['Category'].unique().tolist()

    options = ["All"] + unique_categories

    selected_category = st.sidebar.selectbox("Select Category:", options)

    if selected_category != "All":
        df = df[df['Category'] == selected_category]

    st.sidebar.success(f"📌 {len(df)} News Found")

    cols = st.columns(3)

    for index, (_, row) in enumerate(df.iterrows()):
        with cols[index % 3]: 
            card_html = f"""
            <div class="news-card">
                <div class="news-category">{row['Category']}</div>
                <a href="{row['Link']}" target="_blank" class="news-title">{row['Title']}</a>
            </div>
            """
            st.image(row['Image'], use_container_width=True)
            st.markdown(card_html, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("News file not found!")