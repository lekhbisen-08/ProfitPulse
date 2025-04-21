import streamlit as st
import requests
from PIL import Image
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
import time
import seaborn as sns
import matplotlib.gridspec as gridspec
import datetime


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

if st.sidebar.button("Return back Profit Pulse Home Page"):
   st.switch_page("ProfitPulse.py")

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
            
            # Stock name as header
            col1.markdown(f"# {stock_data['name']}")
            price_text = f"{stock_data['price']:.2f}"
            change_text = f"({stock_data['change']:+.1f}%)" 
            
            # Add color to percentage change 
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

#Stock fundamental
st.title("Stock Fundamental Indicators Analysis :")

# Indicator: Price-to-Earnings (P/E) Ratio
st.header("1. Price-to-Earnings (P/E) Ratio")
st.subheader("Definition:")
st.write("""
    The Price-to-Earnings (P/E) ratio is a valuation metric for a company. It is calculated by dividing the market price per share by the earnings per share (EPS). 
    The P/E ratio helps assess whether a stock is overvalued or undervalued compared to its earnings.
""")
st.subheader("Usage:")
st.write("""
    - A high P/E ratio suggests that the market has high expectations for future growth and may be overvalued.
    - A low P/E ratio could indicate that the stock is undervalued or that the company is not performing well.
""")
st.subheader("How to Analyze:")
st.write("""
    - Compare the P/E ratio with industry peers or historical P/E ratios to gauge valuation.
    - Check the growth rate of the company. High-growth companies typically have higher P/E ratios.
""")
st.markdown("---")

# Indicator: Price-to-Book (P/B) Ratio
st.header("2. Price-to-Book (P/B) Ratio")
st.subheader("Definition:")
st.write("""
    The Price-to-Book (P/B) ratio is a financial measure used to compare a company's market value (price) to its book value (net asset value). 
    It is calculated by dividing the stock price by the book value per share.
""")
st.subheader("Usage:")
st.write("""
    - A P/B ratio below 1 may indicate that the stock is undervalued, suggesting a potential investment opportunity.
    - A ratio higher than 1 could indicate that the stock is overvalued.
""")
st.subheader("How to Analyze:")
st.write("""
    - A low P/B ratio suggests that the market is undervaluing the company compared to its assets.
    - Compare the P/B ratio of companies within the same industry to determine relative valuation.
""")
st.markdown("---")

# Indicator: Dividend Yield
st.header("3. Dividend Yield")
st.subheader("Definition:")
st.write("""
    Dividend yield is the ratio of a company's annual dividend payments compared to its stock price. It is expressed as a percentage.
    It is calculated by dividing the annual dividend by the current stock price.
""")
st.subheader("Usage:")
st.write("""
    - A high dividend yield could be attractive to income-focused investors.
    - A very high dividend yield may be a red flag, indicating the company might be struggling.
""")
st.subheader("How to Analyze:")
st.write("""
    - Compare dividend yields within the same industry.
    - Ensure the company has a stable or growing dividend history.
    - A sustainable dividend yield indicates that the company can continue to pay out the dividends.
""")
st.markdown("---")

# Indicator: Debt-to-Equity (D/E) Ratio
st.header("4. Debt-to-Equity (D/E) Ratio")
st.subheader("Definition:")
st.write("""
    The Debt-to-Equity (D/E) ratio measures a company's financial leverage by comparing its total liabilities to its shareholders' equity.
    It is calculated by dividing the total debt by total equity.
""")
st.subheader("Usage:")
st.write("""
    - A high D/E ratio means that a company is financing a large portion of its operations with debt, which could be risky.
    - A low D/E ratio suggests a conservative approach to leverage and lower financial risk.
""")
st.subheader("How to Analyze:")
st.write("""
    - A high D/E ratio might indicate potential financial difficulties during market downturns.
    - A low D/E ratio typically suggests stability, but could also imply the company is not using leverage to fuel growth.
""")
st.markdown("---")

# Indicator: Return on Equity (ROE)
st.header("5. Return on Equity (ROE)")
st.subheader("Definition:")
st.write("""
    Return on Equity (ROE) measures the profitability of a company in relation to shareholders' equity. It is calculated by dividing net income by average shareholders' equity.
""")
st.subheader("Usage:")
st.write("""
    - A high ROE indicates that the company is efficiently using its equity base to generate profit.
    - A low ROE suggests that the company might not be using its equity capital effectively.
""")
st.subheader("How to Analyze:")
st.write("""
    - Compare ROE with industry peers to evaluate relative performance.
    - Look at the company's ability to maintain or grow ROE over time.
""")
st.markdown("---")

# Indicator: Earnings Per Share (EPS)
st.header("6. Earnings Per Share (EPS)")
st.subheader("Definition:")
st.write("""
    Earnings Per Share (EPS) is the portion of a company's profit allocated to each outstanding share of common stock.
    It is calculated by dividing net income by the number of outstanding shares.
""")
st.subheader("Usage:")
st.write("""
    - A higher EPS indicates better profitability.
    - Investors often use EPS growth as an indicator of company growth potential.
""")
st.subheader("How to Analyze:")
st.write("""
    - Compare the company's EPS with past performance and industry peers.
    - Analyze the trend of EPS growth to understand the company's potential for future profitability.
""")
st.markdown("---")

# Indicator: Profit Growth
st.header("7. Profit Growth")
st.subheader("Definition:")
st.write("""
    Profit growth is the increase in a company's net profit over time. It is usually represented as a percentage increase in net income year-over-year.
""")
st.subheader("Usage:")
st.write("""
    - Consistent profit growth indicates strong operational performance.
    - Declining profit growth could signal potential trouble or decreasing business prospects.
""")
st.subheader("How to Analyze:")
st.write("""
    - Look for a trend of increasing profits over several quarters or years.
    - Compare profit growth rates to industry averages or peers to assess relative performance.
""")
st.markdown("---")

# Indicator: Sales Growth
st.header("8. Sales Growth")
st.subheader("Definition:")
st.write("""
    Sales growth measures the percentage increase in a company's sales/revenue over time, typically year-over-year.
""")
st.subheader("Usage:")
st.write("""
    - Strong sales growth usually indicates a company is expanding its market share.
    - Slow or negative sales growth could signal stagnation or a decrease in demand for products/services.
""")
st.subheader("How to Analyze:")
st.write("""
    - Analyze sales growth over multiple periods to detect trends.
    - Compare sales growth against industry peers to gauge relative performance.
""")
st.markdown("---")

# Indicator: Market Capitalization (Market Cap)
st.header("9. Market Capitalization (Market Cap)")
st.subheader("Definition:")
st.write("""
    Market capitalization is the total market value of a company's outstanding shares, calculated by multiplying the share price by the total number of shares.
""")
st.subheader("Usage:")
st.write("""
    - Large-cap stocks are generally considered more stable, while small-cap stocks may offer higher growth potential but come with more risk.
    - Market cap helps categorize companies into different segments (small, mid, large-cap).
""")
st.subheader("How to Analyze:")
st.write("""
    - Compare the market cap of a company with others in the same industry.
    - Understand the risk profile based on the market cap size: large-cap stocks are generally less volatile than small-cap stocks.
""")
st.markdown("---")

# Indicator: High & Low
st.header("10. High & Low")
st.subheader("Definition:")
st.write("""
    The high and low values represent the highest and lowest prices a stock has traded at during a specific time period, usually over the past 52 weeks.
""")
st.subheader("Usage:")
st.write("""
    - A stock's high and low indicate its price range over a given time frame.
    - Investors use this information to determine volatility and price levels of interest.
""")
st.subheader("How to Analyze:")
st.write("""
    - If the stock price is closer to its 52-week high, it could indicate an overbought condition.
    - If it's closer to the 52-week low, the stock might be undervalued or facing financial difficulties.
""")
st.markdown("---")

# Indicator: Types of Promoter Holdings
st.header("11. Types of Promoter Holdings")
st.subheader("Definition:")
st.write("""
    Promoter holdings refer to the percentage of a company's shares that are owned by its promoters, or the people who have a significant interest in the company, such as its founders or major stakeholders.
""")
st.subheader("Usage:")
st.write("""
    - High promoter holding indicates confidence in the business and long-term commitment.
    - Low promoter holding might suggest that the company's leadership does not have significant personal financial stake in the company.
""")
st.subheader("How to Analyze:")
st.write("""
    - Monitor changes in promoter holdings over time, as reductions could indicate a lack of confidence or issues within the company.
    - Compare promoter holdings across similar companies to determine if the ownership structure is typical or not.
""")
st.markdown("---")

# Conclusion
st.write("""
    These fundamental indicators are essential tools for analyzing a company's financial health and stock value.
    It is crucial to combine these indicators with other factors such as market conditions, industry trends, and macroeconomic factors for a comprehensive investment decision.
""")
