# Library Used
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


#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Prediction",
    page_icon="",
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
   if st.button("Company's Balance Sheet"):
      st.switch_page("pages/Balance Sheet.py")
    
with col5:
   
   if st.button("Technical Analysis"):
      st.switch_page("pages/Technicals.py")
   st.text("")
   if st.button("Home Page \n Profit Pulse"):
      st.switch_page("ProfitPulse.py")


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
st.sidebar.button(f"More Information About \n { st.session_state.tickermain }.LTD")

# Prediction Model
def convert_timestamps(data):
    if isinstance(data, pd.DataFrame):
        for column in data.columns:
            if pd.api.types.is_datetime64_any_dtype(data[column]):
                data[column] = data[column].dt.strftime('%Y-%m-%d')  # Convert to string format
    elif isinstance(data, pd.Series):
        if pd.api.types.is_datetime64_any_dtype(data):
            data = data.dt.strftime('%Y-%m-%d')  # Convert to string format
    elif isinstance(data, dict):
        for key, value in data.items():
            data[key] = convert_timestamps(value)
    return data

#Stocks Data From Yahoo
def get_stock_data(stock_name):
    stock = yf.Ticker(stock_name)
    
    # Extracting fundamental data
    try:
        info = stock.info
        
        shareholding_pattern = info.get('shareholderEquity', 'Not Available')

        data = {
            'Name': info.get('longName', 'Not Available'),
            'PE': round(info.get('trailingPE', 0), 2),
            'PB': round(info.get('priceToBook', 0), 2),
            'ROE': round(info.get('returnOnEquity', 0), 2),
            'ROCE': round(info.get('returnOnCapitalEmployed', 0), 2),
            'Debt_to_Equity': round(info.get('debtToEquity', 0), 2),
            'Profit_Growth': round(info.get('earningsQuarterlyGrowth', 0) * 100, 2),
            'Sales_Growth': round(info.get('revenueGrowth', 0) * 100, 2),
            'Dividend_Yield': round(info.get('dividendYield', 0) * 100, 2),
            'Market_Cap': round(info.get('marketCap', 0) / 1e7, 2),
            'Current_Price': round(info.get('currentPrice', 0), 2),
            '52wk_High': round(info.get('fiftyTwoWeekHigh', 0), 2),
            '52wk_Low': round(info.get('fiftyTwoWeekLow', 0), 2),
            'Shareholding_Pattern': shareholding_pattern
        }
        return data
    except Exception as e:
        st.error(f"Error fetching data for {stock_name}: {e}")
        return None

# Function for investment recommendation
def investment_advice(stock_data, investment_type, investment_years, num_shares):
    if not stock_data:
        return "Stock data is not available. Please try again."

    # Extract stock data
    pe = stock_data['PE']
    pb = stock_data['PB']
    roe = stock_data['ROE']
    roce = stock_data['ROCE']
    debt_to_equity = stock_data['Debt_to_Equity']
    profit_growth = stock_data['Profit_Growth']
    sales_growth = stock_data['Sales_Growth']
    dividend_yield = stock_data['Dividend_Yield']
    market_cap = stock_data['Market_Cap']
    current_price = stock_data['Current_Price']
    shareholding_pattern = stock_data['Shareholding_Pattern']

#recommendatin function
    recommendation = ""

    # New Investment 
    if investment_type.lower() == 'new investment':
        if pe < 20 and pb < 3 and roe > 15 and roce > 15 and profit_growth > 10 and sales_growth > 10 and debt_to_equity < 1.0:
            recommendation = f"Buy : The company appears undervalued, with a PE ratio is {pe} and PB ratio is {pb}. It boasts solid fundamentals, with both ROE and ROCE exceeding 15%, and demonstrates strong growth potential, with projections above 10%."
        elif dividend_yield > 3 and profit_growth > 10:
            recommendation = f"Buy : The company is appealing for long-term investment, offering a solid dividend yield is {dividend_yield}, along with consistent growth, as sales is {sales_growth} and profit growth is {profit_growth}."
        else:
            recommendation = "Hold : The stock shows potential, but its current valuation may not be the best for investment. The company’s fundamentals are not very strong, and its growth isn't impressive enough to make it a good choice for new investments at the moment. While there might be future opportunities, it's better to wait until the situation improves.."

    # Existing Investment 
    elif investment_type.lower() == 'existing investment':
        if profit_growth < 0 or sales_growth < 0 or debt_to_equity > 2:
            recommendation = f"Sell: The company shows weak growth and high debt, with a debt-to-equity ratio is {debt_to_equity}, which could pose a risk for long-term holdings. This is compounded by low profit and sales growth of {profit_growth} and {sales_growth}, making it a potentially risky to be hold further.."
        elif roe < 5 or roce < 5:
            recommendation = f"Sell: A low return on equity (ROE) of {roe} and return on capital employed (ROCE) is {roce}suggest poor financial performance, indicating that the company may not be efficiently utilizing its resources to generate profits."
        elif pe > 30 or pb > 5:
            recommendation = f"Sell: The stock seems overvalued, with its PE ratio {pe} and PB ratio {pb}, both significantly higher than its historical levels. This could indicate a potential risk of price correction."
        else:
            recommendation = f"Hold: The stock is stable, but it's important to carefully analyze your entry point. The return on investment is currently {roe}, though the PE Ratio and PB Ratio {pe} and {pb}. Consider waiting for a better opportunity to maximize your returns."

    # Investment Year
    if investment_years > 5:
        recommendation += f" Given that you're holding for {investment_years} more years, consider monitoring the stock’s quarterly earnings, debt levels, and overall market conditions."

    if shareholding_pattern != 'Not Available':
        recommendation += f"\nShareholding Pattern: The shareholder equity is: {shareholding_pattern}. You may want to watch for any large changes in promoter holdings or institutional investors."

    #Total investment by user
    total_investment = current_price * num_shares if num_shares else 0
    return recommendation, total_investment

st.title(f"{st.session_state.tickermain} Stock Recommendation")

stock_name = f"{st.session_state.tickermain}.NS"

#User Intraction
col10, col11, col12 = st.columns(3)
with col10 :
# new or already invested
 investment_type = st.selectbox("Is it your new Investment or you already own Shares?", ["New Investment", "Existing Investment"])
with col11 :
# yers to invest
 if investment_type.lower() == "new investment":
    investment_years = st.number_input("For How many years are you planning to Invest?", min_value=1, max_value=30, value=5)
 elif investment_type.lower() == "existing investment":
    investment_years = st.number_input("For how many years are you planning to be Invested", min_value=1, max_value=30, value=5)
with col12 :
# no. of shares buying
 num_shares = st.number_input("How many shares do you intend to purchase or currently hold?", min_value=1, value=1)

st.text("")
st.text("")


col100, col101, col102, col103, col104 = st.columns(5)
with col102 :
 if st.button("Plese Enter the Above Information Accordingly"):
     st.text("")
st.header("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

if stock_name:
        stock_data = get_stock_data(stock_name)
        recommendation, total_investment = investment_advice(stock_data, investment_type, investment_years, num_shares)

        # Recommendation
        if "Buy" in recommendation:
            st.success(recommendation)  
        elif "Sell" in recommendation:
            st.error(recommendation)  
        else:
            st.warning(recommendation)  
         
        st.header("")
        # Total Investment
        st.header(f" Total Investing: ₹{round(total_investment, 2)} for {num_shares} shares at the current price of ₹{stock_data['Current_Price']}.")

        if stock_data:
         st.subheader(" Stock Data:")
         
         #Stock Data
         col1, col2, col3 = st.columns(3) 
        
        with col1 :
            st.subheader(f"**52-week High**: ₹{stock_data['52wk_High']}")  
            st.subheader(f"**52-week Low**: ₹{stock_data['52wk_Low']}")
            st.subheader(f"**Current Price**: ₹{stock_data['Current_Price']}")
            st.subheader(f"**Debt to Equity Ratio**: {stock_data['Debt_to_Equity']}")
        with col2 :
            st.subheader(f"**Profit Growth (Quarterly)**: {stock_data['Profit_Growth']}%")
            st.subheader(f"**Sales Growth (Yearly)**: {stock_data['Sales_Growth']}%")
            st.subheader(f"**Dividend Yield**: {stock_data['Dividend_Yield']}%")
            st.subheader(f"**Market Capitalization**: ₹{stock_data['Market_Cap']} Crores")
        with col3 :
            st.subheader(f"**PE Ratio**: {stock_data['PE']}")
            st.subheader(f"**PB Ratio**: {stock_data['PB']}")
            st.subheader(f"**ROE (Return on Equity)**: {stock_data['ROE']}%")
            st.subheader(f"**ROCE (Return on Capital Employed)**: {stock_data['ROCE']}%")

else:
        st.error("Please enter a valid stock symbol.")
