import streamlit as st
import yfinance as yf
import requests
import matplotlib.pyplot as plt
import pandas as pd
import time
import seaborn as sns
import matplotlib.gridspec as gridspec
import datetime
from bs4 import BeautifulSoup
from PIL import Image


#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Balance Sheet",
    page_icon="balance.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Dark Green and Red
st.markdown(f"""
    <style>
    /* CSS Variables for Trading Theme */
    :root {{
        --bullish: #2EB82E;  /* Green for bullish elements */
        --bearish: #FF4444;  /* Red for bearish elements */
        --background-image-main: url('https://example.com/green-background.jpg'); /* Green background image for main content */
        --background-image-sidebar: url('https://example.com/red-pattern.jpg'); /* Red background image for sidebar */
        --main-bg: linear-gradient(
            rgba(46, 184, 46, 0.85), 
            rgba(14, 17, 23, 0.95)
        ), var(--background-image-main);  /* Greenish gradient for the main page */
        --sidebar-bg: linear-gradient(
            rgba(23, 28, 36, 0.95),
            rgba(23, 28, 36, 0.98)
        ), var(--background-image-sidebar);  /* Red sidebar gradient */
    }}

    /* Button Styles (Red for Bearish) */
    button {{
        background: rgba(255, 68, 68, 0.15) !important;
        color: var(--bearish) !important;
        border: 1px solid var(--bearish) !important;
        border-radius: 8px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    button:hover {{
        background: rgba(255, 68, 68, 0.3) !important;
        box-shadow: 0 0 15px rgba(255, 68, 68, 0.3);
        transform: translateY(-1px);
    }}

    button:active {{
        transform: translateY(0);
    }}

    /* Sidebar Styles - Red Theme with Background Image */
    [data-testid="stSidebar"] {{
        background: var(--sidebar-bg) !important;
        border-right: 2px solid var(--bearish);
        box-shadow: 8px 0 30px rgba(255, 68, 68, 0.15);
        padding: 15px;
        font-weight: bold;
    }}

    /* Sidebar Links and Text in Red */
    [data-testid="stSidebarNav"] a {{
        color: var(--bearish) !important;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        transition: color 0.3s ease;
    }}

    [data-testid="stSidebarNav"] a:hover {{
        color: #ff0000 !important;
        background-color: rgba(255, 68, 68, 0.2);
    }}

    /* Main Page Styles - Green Theme with Background Image */
    .main {{
        background: var(--main-bg);
        color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 5px 30px rgba(46, 184, 46, 0.2);
    }}

    /* Main content header - Green */
    .dashboard-header {{
        color: var(--bullish);
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px 8px rgba(46, 184, 46, 0.6);
    }}

    /* Green Borders & Shadows for Charts and Metrics */
    [data-testid="stMetric"],
    .stPlotlyChart,
    .news-card {{
        border-color: rgba(46, 184, 46, 0.5) !important;
        box-shadow: 0 0 30px rgba(46, 184, 46, 0.2);
        border-radius: 10px;
    }}

    /* Green Tabs for Bullish Indicators */
    [data-baseweb="tab"] {{
        border-color: rgba(46, 184, 46, 0.3) !important;
    }}

    /* Active Tab (Bullish - Green) */
    [aria-selected="true"] {{
        background: linear-gradient(
            45deg,
            var(--bullish),
            #1A5C1A
        ) !important;
        box-shadow: 0 4px 15px rgba(46, 184, 46, 0.3) !important;
    }}

    /* Card styles for news and metrics */
    .news-card {{
        background: rgba(46, 184, 46, 0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(46, 184, 46, 0.2);
    }}

    .stMetric {{
        background: rgba(46, 184, 46, 0.15) !important;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(46, 184, 46, 0.3) !important;
        box-shadow: 0 0 20px rgba(46, 184, 46, 0.2);
    }}

    /* Additional Animations */
    @keyframes bounce {{
        0% {{
            transform: translateY(0);
        }}
        50% {{
            transform: translateY(-5px);
        }}
        100% {{
            transform: translateY(0);
        }}
    }}
    </style>
""", unsafe_allow_html=True)

#LOGO Specification
img=Image.open("pages/moneypulse.png")
img_resized = img.resize((100,100))
st.sidebar.image(img,use_container_width=False)

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.text(" ")
st.sidebar.text(" ")

# Removes the Page Configuration
st.markdown(
    """
    <style>
        /* Hide the alphabetical navigation menu */
        div[data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# 4 Buttons in sidebar
col4, col5 = st.sidebar.columns(2)
with col4:
   if st.button("Fundamental Analysis"):
      st.switch_page("pages/Fundamental.py")
   st.text(" ")
   if st.button("Company's Balance Sheet"):
      st.switch_page("pages/Balance Sheet.py") 
    
with col5:
   
   if st.button("Technical Analysis"):
      st.switch_page("pages/Technicals.py")
   st.text("")
   if st.button("Stock Prediction"):
      st.switch_page("pages/Prediction.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Mutual Fund Search tag
if st.sidebar.button(f"Fundamental Mutual Fund Analysis"):
    st.switch_page("pages/Mutual_Fund.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

 #News Button
if st.sidebar.button("Return back Home Page Profit Pulse"):
    st.switch_page("ProfitPulse.py")    

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Information Page
st.sidebar.button(f"More Information About \n { st.session_state.tickermain }.LTD")

# Function to fetch news data
def fetch_news(url, count=20):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = []
    
    for i in range(1, count+1):
        news_id = f"newslist-{i}"
        news_item = soup.find(id=news_id)
        if news_item:
            news_items.append({"content": news_item.text})
        else:
            # Try alternative selectors if the default ID doesn't work
            news_item = soup.select_one(f"li#newslist-{i} > h2 > a")
            if news_item:
                news_items.append({"content": news_item.text})
    
    return news_items

# Fetch all news data
@st.cache_data(ttl=3600)  
def get_all_news():
    news_data = {}
    
    # Company News
    company_url = "https://www.moneycontrol.com/news/business/companies/"
    news_data["Company Headlines"] = fetch_news(company_url, 20)
    
    # Economy News
    economy_url = "https://www.moneycontrol.com/news/business/economy/"
    news_data["Economy Headlines"] = fetch_news(economy_url, 20)
    
    # Stock News (default)
    stocks_url = "https://www.moneycontrol.com/news/business/stocks/"
    news_data["Stock Headlines"] = fetch_news(stocks_url, 20)
    
    # Finance News
    finance_url = "https://www.moneycontrol.com/news/business/personal-finance/"
    news_data["Finance Headlines"] = fetch_news(finance_url, 20)
    
    # Banking News
    banking_url = "https://www.moneycontrol.com/news/business/banking/"
    news_data["Banking Headlines"] = fetch_news(banking_url, 20)
    
    return news_data

# Main app
def main():
    st.title("Money Pulse")
    st.write("Click the buttons below to view headlines for each category:")
    
    # Get all news data
    all_news = get_all_news()
    
    columns = st.columns(5)
    
    # Create buttons in each column for each news category
    selected_category = None
    for idx, option in enumerate(all_news.keys()):
        col = columns[idx % 5]  
        if col.button(option):
            selected_category = option
    
    # Display selected news category
    if selected_category:
        st.header(f"📰 {selected_category}")
        
        # Show all 20 items without numbering
        for item in all_news[selected_category][:20]:
            st.subheader(f"{item['content']}")

            st.markdown("---")
    else:
        st.info("Please click on a category button to view the news.")

if __name__ == "__main__":
    main()



