import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import time
import seaborn as sns
import matplotlib.gridspec as gridspec
import talib



#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Technical Analysis",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Dark Green and 
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


#Image Specification
img=Image.open("P-LOGO.png")
img_resized = img.resize((100,100))
st.sidebar.image(img,use_container_width=False)


st.sidebar.markdown("<hr>", unsafe_allow_html=True)


st.sidebar.text(" ")
st.sidebar.text(" ")


# Remove Dile Navigation in Sidebar
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
   
   if st.button("Home Page \n Profit Pulse"):
      st.switch_page("ProfitPulse.py")
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
            
            # Stock name as header
            col1.markdown(f"# {stock_data['name']}")
            
            # Plain text price and percentage change (without box)
            price_text = f"{stock_data['price']:.2f}"
            change_text = f"({stock_data['change']:+.1f}%)"  
            
            # Add color to percentage change (green for positive, red for negative)
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


# --- User input ---
ticker = (f"{st.session_state.tickermain}.NS")
start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

# --- TA-Lib Indicator options ---
indicators = {
    "Simple Moving Average (SMA)": "SMA",
    "Exponential Moving Average (EMA)": "EMA",
    "Relative Strength Index (RSI)": "RSI",
    "Moving Average Convergence Divergence (MACD)": "MACD",
    "Bollinger Bands": "BBANDS",
    "Stochastic Oscillator": "STOCH",
    "Average Directional Index (ADX)": "ADX",
    "On Balance Volume (OBV)": "OBV",
    "Average True Range (ATR)": "ATR",
    "Commodity Channel Index (CCI)": "CCI"
}

selected_indicators = st.multiselect("Select Technical Indicators", list(indicators.keys()))

# --- Load stock data ---
if ticker and start_date and end_date:
    df = yf.download(ticker, start=start_date, end=end_date)

    if df.empty:
        st.warning("No data found for the selected stock and date range.")
    else:
        st.subheader(f"{ticker} Stock Data")

        # --- Prepare data for TA-Lib (flatten and cast to float64) ---
        close = df['Close'].astype('float64').values.ravel()
        high = df['High'].astype('float64').values.ravel()
        low = df['Low'].astype('float64').values.ravel()
        volume = df['Volume'].astype('float64').values.ravel()

        # --- Plot price and indicators ---
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(df.index, df['Close'], label='Close Price', linewidth=2)

        ax2 = ax.twinx()
        has_ax2 = False

        for name in selected_indicators:
            func = indicators[name]
            try:
                if func == "SMA":
                    sma = pd.Series(talib.SMA(close, timeperiod=14), index=df.index)
                    ax.plot(df.index, sma, label='SMA 14')

                elif func == "EMA":
                    ema = pd.Series(talib.EMA(close, timeperiod=14), index=df.index)
                    ax.plot(df.index, ema, label='EMA 14')

                elif func == "RSI":
                    rsi = pd.Series(talib.RSI(close, timeperiod=14), index=df.index)
                    has_ax2 = True
                    ax2.plot(df.index, rsi, label='RSI', linestyle='--')

                elif func == "MACD":
                    macd, signal, _ = talib.MACD(close)
                    macd = pd.Series(macd, index=df.index)
                    signal = pd.Series(signal, index=df.index)
                    has_ax2 = True
                    ax2.plot(df.index, macd, label='MACD', linestyle='--')
                    ax2.plot(df.index, signal, label='Signal', linestyle=':')

                elif func == "BBANDS":
                    upper, middle, lower = talib.BBANDS(close)
                    ax.plot(df.index, pd.Series(upper, index=df.index), label='BB Upper', linestyle='--')
                    ax.plot(df.index, pd.Series(middle, index=df.index), label='BB Middle', linestyle=':')
                    ax.plot(df.index, pd.Series(lower, index=df.index), label='BB Lower', linestyle='--')

                elif func == "STOCH":
                    slowk, slowd = talib.STOCH(high, low, close)
                    ax2.plot(df.index, pd.Series(slowk, index=df.index), label='Stoch %K', linestyle='--')
                    ax2.plot(df.index, pd.Series(slowd, index=df.index), label='Stoch %D', linestyle=':')
                    has_ax2 = True

                elif func == "ADX":
                    adx = pd.Series(talib.ADX(high, low, close), index=df.index)
                    ax2.plot(df.index, adx, label='ADX', linestyle='--')
                    has_ax2 = True

                elif func == "OBV":
                    obv = pd.Series(talib.OBV(close, volume), index=df.index)
                    ax2.plot(df.index, obv, label='OBV', linestyle='--')
                    has_ax2 = True

                elif func == "ATR":
                    atr = pd.Series(talib.ATR(high, low, close, timeperiod=14), index=df.index)
                    ax2.plot(df.index, atr, label='ATR', linestyle='--')
                    has_ax2 = True

                elif func == "CCI":
                    cci = pd.Series(talib.CCI(high, low, close, timeperiod=14), index=df.index)
                    ax2.plot(df.index, cci, label='CCI', linestyle='--')
                    has_ax2 = True

            except Exception as e:
                st.error(f"❌ Error computing {name}: {e}")

        ax.set_title(f"{ticker} Stock Price with Selected Indicators")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc='upper left')

        if has_ax2:
            ax2.legend(loc='upper right')

        st.pyplot(fig)

st.markdown("<hr>", unsafe_allow_html=True)


# --- Display information about selected indicators ---
if selected_indicators:
    st.markdown("## 📘 Indicator Reference Guide")

    indicator_info = {
        "Simple Moving Average (SMA)": {
            "name": "Simple Moving Average (SMA)",
            "description": """
<b>What is it?</b><br>
The <b>Simple Moving Average (SMA)</b> is the average of a security’s closing price over a specific period. 
It smooths out price data to identify trends over time, helping traders avoid reacting to short-term volatility. 
It is one of the most commonly used and beginner-friendly indicators.<br><br>

<b>Example Use:</b> A 14-day SMA calculates the average closing price over the past 14 days.<br><br>

<b>Common Strategy:</b> If the current price moves above the SMA, it may signal a buying opportunity. 
If the price falls below the SMA, it could be a bearish signal.
"""
        },
        "Exponential Moving Average (EMA)": {
            "name": "Exponential Moving Average (EMA)",
            "description": """
<b>What is it?</b><br>
The <b>Exponential Moving Average (EMA)</b> gives more weight to recent prices compared to the SMA, 
allowing it to respond more quickly to price changes.<br><br>

<b>Use Case:</b> Traders often use EMA to identify short-term trends and signals faster than SMA.<br><br>

<b>Common Strategy:</b> A bullish signal may occur when a short-term EMA crosses above a long-term EMA 
(e.g., 12-EMA crossing above 26-EMA).
"""
        },
        "Relative Strength Index (RSI)": {
            "name": "Relative Strength Index (RSI)",
            "description": """
<b>What is it?</b><br>
The <b>Relative Strength Index (RSI)</b> is a momentum oscillator that measures the speed and magnitude of recent price changes 
to evaluate overbought or oversold conditions.<br><br>

<b>Scale:</b> Ranges from 0 to 100.<br><br>

<b>Common Signals:</b><br>
- RSI above 70 = Overbought (potential reversal or sell zone)<br>
- RSI below 30 = Oversold (potential reversal or buy zone)
"""
        },
        "Moving Average Convergence Divergence (MACD)": {
            "name": "Moving Average Convergence Divergence (MACD)",
            "description": """
<b>What is it?</b><br>
<b>MACD</b> is a trend-following momentum indicator that shows the relationship between two EMAs 
(typically 12-day and 26-day).<br><br>

<b>Visual Components:</b><br>
- MACD Line<br>
- Signal Line<br>
- Histogram (difference between the two)<br><br>

<b>Common Strategy:</b> A bullish crossover occurs when the MACD line crosses above the signal line.
"""
        },
        "Bollinger Bands": {
            "name": "Bollinger Bands",
            "description": """
<b>What is it?</b><br>
<b>Bollinger Bands</b> consist of a middle band (SMA) with two outer bands (±2 standard deviations). 
They reflect price volatility — the bands widen during high volatility and contract during low volatility.<br><br>

<b>Use Case:</b><br>
- Price touching upper band = potentially overbought<br>
- Price touching lower band = potentially oversold
"""
        },
        "Stochastic Oscillator": {
            "name": "Stochastic Oscillator",
            "description": """
<b>What is it?</b><br>
This momentum indicator compares a stock’s closing price to its price range over a certain period. 
It generates two lines: %K and %D.<br><br>

<b>Common Interpretation:</b><br>
- Above 80 = Overbought<br>
- Below 20 = Oversold<br>
- A bullish signal occurs when %K crosses above %D.
"""
        },
        "Average Directional Index (ADX)": {
            "name": "Average Directional Index (ADX)",
            "description": """
<b>What is it?</b><br>
<b>ADX</b> measures the strength of a trend — not its direction.<br><br>

<b>Value Ranges:</b><br>
- ADX < 20 = Weak/No trend<br>
- ADX > 25 = Strong trend<br><br>

Often used with +DI and -DI for directional context.
"""
        },
        "On Balance Volume (OBV)": {
            "name": "On Balance Volume (OBV)",
            "description": """
<b>What is it?</b><br>
<b>OBV</b> combines price and volume to show how volume is flowing in or out of a stock.<br><br>

<b>Interpretation:</b><br>
- Rising OBV confirms an uptrend<br>
- Falling OBV confirms a downtrend<br>
- Divergence between OBV and price can signal reversal
"""
        },
        "Average True Range (ATR)": {
            "name": "Average True Range (ATR)",
            "description": """
<b>What is it?</b><br>
<b>ATR</b> measures market volatility by decomposing the range of price movement. 
It does not indicate price direction — only volatility.<br><br>

<b>Use Case:</b><br>
- Higher ATR = Greater volatility<br>
- Used to set stop-loss levels or breakout triggers
"""
        },
        "Commodity Channel Index (CCI)": {
            "name": "Commodity Channel Index (CCI)",
            "description": """
<b>What is it?</b><br>
<b>CCI</b> identifies overbought and oversold conditions based on the relationship between price and its average.<br><br>

<b>Signals:</b><br>
- CCI > +100 = Overbought<br>
- CCI < -100 = Oversold<br><br>

<b>Note:</b> CCI can stay in overbought/oversold territory during strong trends.
"""
        }
    }

    for indicator in selected_indicators:
        info = indicator_info.get(indicator)
        if info:
            with st.expander(f"📖 {info['name']} - Learn More"):
                st.markdown(
                    f"""<div style='font-size:22px; line-height:1.8; text-align: justify; padding: 10px 0;'>{info['description']}</div>""",
                    unsafe_allow_html=True
                )
