import streamlit as st
import requests
import yfinance as yf
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
img=Image.open("P-LOGO.png")
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
   if st.button("Home Page \n Profit Pulse"):
      st.switch_page("ProfitPulse.py")
    
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
if st.sidebar.button(f"Keep Updated by Latest News by \n Money Pulse"):
    st.switch_page("pages/News.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)


#Information Page
st.sidebar.button(f"More Information About \n { st.session_state.tickermain }.LTD")

#Heading STOCK data
stock = st.session_state.tickermain 
tickers = f"{stock}.NS"
ticker_list = [t.strip() for t in str(tickers).split(',') if t.strip() != '']

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        if not data.empty:
            current_price = data['Close'][-1]
            previous_close = data['Close'][-2] if len(data) > 1 else current_price
            percent_change = ((current_price - previous_close) / previous_close) * 100
            return {
                'name': stock.info.get('shortName', ticker),
                'price': current_price,
                'change': percent_change
            }
        return None
    except:
        return None

# Display stock data side by side
if ticker_list:
    for ticker in ticker_list:
        stock_data = get_stock_data(ticker)
        if stock_data:
            col1, col900, col2,  col100 = st.columns(4) 
            
            with col100:
             st.text("")
             if st.button("Profit Pulse home Page"):
              st.switch_page("ProfitPulse.py")

            # Stock name as header
            col1.markdown(f"# {stock_data['name']}")
            
            price_text = f"{stock_data['price']:.2f}"
            change_text = f"({stock_data['change']:+.1f}%)" 
            
            #color to percentage change 
            if stock_data['change'] > 0:
                change_text = f'<span style="color: green;">{change_text}</span>'
            elif stock_data['change'] < 0:
                change_text = f'<span style="color: red;">{change_text}</span>'
            
            col2.markdown(
                f"<div style='font-size: 40px; font-weight: bold; margin-top: 10px;'>{price_text} {change_text}</div>", 
                unsafe_allow_html=True
            )
        else:
            st.error(f"Unable to fetch data for {ticker}")
else:
    st.warning("No valid stock tickers found in tickermain")

st.markdown("<hr>", unsafe_allow_html=True)

stock = st.session_state.tickermain 
url = f'https://www.google.com/finance/quote/{stock}:NSE'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elements = soup.find_all(class_="Yfwt5")




news = [element.text for element in elements[:10]]

# Print the news items
for i, item in enumerate(news, start=1):
    st.subheader(f"News : {i} ")
    st.subheader(f"{item}")
