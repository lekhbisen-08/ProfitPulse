import streamlit as st
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.gridspec as gridspec
import plotly.graph_objs as go
import webbrowser
from PIL import Image
import time

#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Profit Pulse",
    page_icon="balance.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page Decoration
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



#Logo Specification
img=Image.open("P-LOGO.png")
img_resized = img.resize((100,100))
st.sidebar.image(img,use_container_width=True)

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Finology API Insertion
tickermain = st.sidebar.text_input('Stocks','TATASTEEL').upper()
url = f'https://ticker.finology.in/company/{tickermain}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Stock Name in other Web Page
st.session_state.tickermain = tickermain

st.sidebar.text(" ")
st.sidebar.text(" ")

# Remove Sidebar Navigation 
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
   if st.button("Stock \n Prediction"):
      st.switch_page("pages/Prediction.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Mutual Fund Search tag
if st.sidebar.button(f"\u2003 Fundamental Mutual Fund Analysis"):
    st.switch_page("pages/Mutual_Fund.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

 #News Button
if st.sidebar.button(f"Keep Updated by Latest News by \n Money Pulse"):
    st.switch_page("pages/News.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Information Page
if st.sidebar.button(f"\u2003 More Information About \n {tickermain}.LTD\u2003"):
    webbrowser.open_new_tab(f"https://www.{tickermain}.com")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.button("\u2003\u2003\u2003\u00A0\u00A0\u00A0\u00A0\u00A0About Profit Pulse \u00A0\u2003\u2003\u2003")



#Data Call from BeautifulSOOP
elements = soup.find_all(class_="Number")
Current_Price = elements[0].text
Day_High = elements[1].text
Day_Low = elements[2].text
Current_Price = elements[0].text
Day_High = elements[1].text
Day_Low = elements[2].text
Market_cap = elements[5].text
Sales_Growth = elements[12].text
Profit_Growth = elements[15].text



#About Section incoader



#Heading STOCK data
stock = tickermain 
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
            col1, col900, col2,  col100 = st.columns([3, 1, 4, 2]) 
           
            with col100:
             st.text("")
             if st.button("Personalized News"):
              st.switch_page("pages/NewsPersonalised.py")

            col1.markdown(f"# {stock_data['name']}")
            
            price_text = f"{stock_data['price']:.2f}"
            change_text = f"({stock_data['change']:+.1f}%)" 
            
            if stock_data['change'] > 0:
                change_text = f'<span style="color: green;">{change_text}</span>'
            elif stock_data['change'] < 0:
                change_text = f'<span style="color: red;">{change_text}</span>'
            
            col2.markdown(
                f"<div style='font-size: 40px; font-weight: bold;margin-top: 10px;'>{price_text} {change_text}</div>", 
                unsafe_allow_html=True
            )
        else:
            st.error(f"Unable to fetch data for {ticker}")
else:
    st.warning("No valid stock tickers found in tickermain")

st.header("")

#day high low open data
def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.info
        return {
            'open': data.get('regularMarketOpen', 'N/A'),
            'high': data.get('regularMarketDayHigh', 'N/A'),
            'low': data.get('regularMarketDayLow', 'N/A')
        }
    except:
        return None
if tickers:
    stock_data = get_stock_data(ticker)

# STOCK Info Columns
col2, col3,col4 = st.columns(3)
with col2:
   st.subheader(f"Day High : {stock_data['high']}")
   st.subheader(f"Day Low : {stock_data['low']}")
with col3:
  st.subheader(f"Market Cap : ₹ {Market_cap} Cr")
  st.subheader(f"Open Price : {stock_data['open']}")
with col4 :
  st.subheader(f"Sales Growth : {Sales_Growth}%")
  st.subheader(f"Profit Growth : {Profit_Growth}%")

st.markdown("<hr>", unsafe_allow_html=True)

st.title("📊 Key Market Indices")

# 5 Major Indices
indices = {
    "SENSEX": "^NSEI",
    "BANK NIFTY": "^BSESN",
    "NIFTY FMCG": "^NSEBANK",
    "NIFTY IT": "^CNXIT",
    "NIFTY 50": "^CNXFMCG"
}

@st.cache_data(ttl=300)
def fetch_index_data(tickers):
    data = yf.download(list(tickers.values()), period="1d", interval="1m", progress=False)
    last_prices = data['Close'].ffill().iloc[-1]
    first_prices = data['Close'].ffill().iloc[0]
    change = last_prices - first_prices
    pct_change = (change / first_prices) * 100
    df = pd.DataFrame({
        "Name": list(tickers.keys()),
        "Ticker": list(tickers.values()),
        "Price": last_prices.values,
        "Change": change.values,
        "% Change": pct_change.values
    })
    return df

# Fetch and display
index_data = fetch_index_data(indices)
columns = st.columns(5)
for col, row in zip(columns, index_data.itertuples()):
    color = "#2f855a" if row.Change > 0 else "#b30000" 
    with col:
        st.markdown(f"""
        <div style="background-color: #2d2d2d; border-radius: 16px; padding: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="background-color: #bdbdbd; border: 1px solid #ffff; border-radius: 12px; padding: 1.2rem; text-align: center;">
                <h5 style="margin-bottom:0.5rem; color:#000000;">{row.Name}</h5>
                <h4 style="margin:0; color:#000000;">₹ {row.Price:.2f}</h4>
                <p style="color:{color}; font-weight:bold; margin-top:0.5rem;">
                    {row.Change:+.2f} ({row._5:+.2f}%)
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)


# NIFTY 50 Stocks
nifty_50_stocks = {
    "RELIANCE": "RELIANCE.NS", "TCS": "TCS.NS", "INFY": "INFY.NS", "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS", "KOTAKBANK": "KOTAKBANK.NS", "ITC": "ITC.NS", "LT": "LT.NS",
    "SBIN": "SBIN.NS", "HINDUNILVR": "HINDUNILVR.NS", "BHARTIARTL": "BHARTIARTL.NS", "ASIANPAINT": "ASIANPAINT.NS",
    "BAJFINANCE": "BAJFINANCE.NS", "HCLTECH": "HCLTECH.NS", "AXISBANK": "AXISBANK.NS", "WIPRO": "WIPRO.NS",
    "MARUTI": "MARUTI.NS", "SUNPHARMA": "SUNPHARMA.NS", "TITAN": "TITAN.NS", "ULTRACEMCO": "ULTRACEMCO.NS"
}

# Caching price data
@st.cache_data(ttl=300)
def fetch_price_data(tickers):
    data = yf.download(list(tickers.values()), period="1d", interval="1m", progress=False)
    last_prices = data['Close'].ffill().iloc[-1]
    first_prices = data['Close'].ffill().iloc[0]
    change = last_prices - first_prices
    pct_change = (change / first_prices) * 100
    df = pd.DataFrame({
        "Name": list(tickers.keys()),
        "Ticker": list(tickers.values()),
        "Price": last_prices.values,
        "Change": change.values,
        "% Change": pct_change.values
    })
    df = df.sort_values(by="% Change", ascending=False).reset_index(drop=True)
    return df

# Fetch NIFTY data
data = fetch_price_data(nifty_50_stocks)

# 🟩 Gainers - green box inside semi-transparent container
st.subheader("📈 Top 5 Gainers")
gainers = data.head(5)
g_col = st.columns(5)
for col, row in zip(g_col, gainers.itertuples()):
    with col:
        st.markdown(
            f"""
            <div style="
                background-color: rgba(0, 128, 0, 0.05);
                border-radius: 16px;
                padding: 1rem;
                box-shadow: 0 4px 10px rgba(0,128,0,0.1);
            ">
                <div style="
                    background-color: #d4f5dd;
                    border: 2px solid #48bb78;
                    border-radius: 12px;
                    padding: 1rem;
                    text-align: center;
                ">
                    <h5 style="margin-bottom:0.5rem; color:#2f855a;">{row.Name}</h5>
                    <h4 style="margin:0;color:#2f855a;">₹ {row.Price:.2f}</h4>
                    <p style="color:#2f855a; font-weight:bold; margin-top:0.5rem;">
                        {row.Change:+.2f} ({row._5:+.2f}%)
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# 🟥 Losers - red box inside semi-transparent container
st.subheader("📉 Top 5 Losers")
losers = data.tail(5).sort_values(by="% Change")
l_col = st.columns(5)
for col, row in zip(l_col, losers.itertuples()):
    with col:
        st.markdown(
            f"""
            <div style="
                background-color: rgba(255, 0, 0, 0.05);
                border-radius: 16px;
                padding: 1rem;
                box-shadow: 0 4px 10px rgba(255,0,0,0.08);
            ">
                <div style="
                    background-color: #ffd6d6;
                    border: 2px solid #f56565;
                    border-radius: 12px;
                    padding: 1rem;
                    text-align: center;
                ">
                    <h5 style="margin-bottom:0.5rem; color:#9b2c2c;">{row.Name}</h5>
                    <h4 style="margin:0;color:#9b2c2c;">₹ {row.Price:.2f}</h4>
                    <p style="color:#b30000; font-weight:bold; margin-top:0.5rem;">
                        {row.Change:+.2f} ({row._5:+.2f}%)
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


st.markdown("<hr>", unsafe_allow_html=True)

#About
url = f'https://www.screener.in/company/{tickermain}/consolidated/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find(class_="sub show-more-box about").text
st.subheader(f"About : {elements}")


st.markdown("<hr>", unsafe_allow_html=True)

#Graph Chart for Stock
def get_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period=period) 
    return stock_data
#Function plot Interactive Candlestick chart
def plot_candlestick(stock_data, ticker):
    trace = go.Candlestick(
        x=stock_data.index,
        open=stock_data['Open'],
        high=stock_data['High'],
        low=stock_data['Low'],
        close=stock_data['Close'],
        increasing=dict(line=dict(color='green')),
        decreasing=dict(line=dict(color='red'))
    )
    # Layout for the graph
    layout = go.Layout(
        title=f'{ticker} Candlestick Chart',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price in USD'),
        hovermode='x unified',  
        template='plotly_dark',  
        showlegend=False
    )
    #  Figure with trace and layout
    fig = go.Figure(data=[trace], layout=layout)
    # Figure in the Streamlit app
    st.plotly_chart(fig)

ticker = f"{tickermain}.NS"
period = st.selectbox("Select Time Period", ["1mo", "3mo", "6mo", "1y", "5y", "max"])
if ticker:
    try:
        # Get stock data
        stock_data = get_stock_data(ticker, period)
        # Plot interactive candlestick chart
        plot_candlestick(stock_data, ticker)
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")

st.markdown("<hr>", unsafe_allow_html=True)

#  historical stock data
def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period=period)
    return stock_data

st.title("Stock Historical Data Dashboard")

# Fetch and display data 
if ticker:
    st.write(f"Fetching historical data for {ticker} over the period of {period}...")
    
    try:
        stock_data = get_stock_data(ticker, period)
        
        if stock_data.empty:
            st.error(f"No data found for ticker {ticker} with the selected period {period}.")
        else:
            st.subheader(f"Historical Data for {ticker} ({period})")
            st.dataframe(stock_data)  
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")

st.markdown("<hr>", unsafe_allow_html=True)

