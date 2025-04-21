#Library Used
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
import plotly.graph_objects as go
from datetime import datetime


#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Fundamental Analysis",
    page_icon="fundamental.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Dark Green 
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

if st.sidebar.button("About Fundamental Analysis \n Indicators"):
   st.switch_page("pages/Teaching_Fundamental.py")

# 4 Buttons in sidebar
col4, col5 = st.sidebar.columns(2)
with col4:
   if st.button("Home Page \n Profit Pulse"):
      st.switch_page("ProfitPulse.py")
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
if st.sidebar.button(f"\u2003 Fundamental Mutual Fund Analysis"):
    st.switch_page("pages/Mutual_Fund.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

 #News Button
if st.sidebar.button(f"Keep Updated by Latest News by \n Money Pulse"):
    st.switch_page("pages/News.py")


st.sidebar.markdown("<hr>", unsafe_allow_html=True)


#Information Page
st.sidebar.button(f"More Information About \n { st.session_state.tickermain }.LTD")


#Heading STOCK data from Yahoo
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


if ticker_list:
    for ticker in ticker_list:
        stock_data = get_stock_data(ticker)
        if stock_data:
            col1, col900, col2,  col100 = st.columns(4) 
            
            # Stock name as header
            col1.markdown(f"# {stock_data['name']}")
            
            price_text = f"{stock_data['price']:.2f}"
            change_text = f"({stock_data['change']:+.1f}%)"  
            
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


st.header("")
st.text("")


# Fundamental Values of Stock
Fundamental_stock = st.session_state.tickermain 
url = f'https://ticker.finology.in/company/{Fundamental_stock}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all(class_="col-6 col-md-4 compess")

col50, col51, col52 = st.columns(3)

with col50 :
 ROCE = elements[14].text
 Roce = " ".join(ROCE.strip().split())
 st.markdown(f"### {Roce}")

 ROE = elements[13].text
 Roe = " ".join(ROE.strip().split())
 st.markdown(f"### {Roe}")

 sales_Growth = elements[12].text
 sales = " ".join(sales_Growth.strip().split())
 st.markdown(f"### {sales}")

with col51 :
 pb_Ratio = elements[4].text
 pb = " ".join(pb_Ratio.strip().split())
 st.markdown(f"### {pb}")

 pe_Ratio = elements[3].text
 pe = " ".join(pe_Ratio.strip().split())
 st.markdown(f"### {pe}")
 
 profit_Growth = elements[15].text
 profit = " ".join(profit_Growth.strip().split())
 st.markdown(f"### {profit}")

with col52 :

 EPS = elements[11].text
 Eps = " ".join(EPS.strip().split())
 st.markdown(f"### {Eps}")

 DEBT = elements[9].text
 Debt = " ".join(DEBT.strip().split())
 st.markdown(f"### {Debt}")

 promoter_Holding = elements[10].text
 promoter = " ".join(promoter_Holding.strip().split())
 st.markdown(f"### {promoter}")


st.markdown("<hr>", unsafe_allow_html=True)


# plot the P/E ratio and closing price
def plot_stock_data(stock_symbol, start_date, end_date):
    stock = yf.Ticker(stock_symbol)

    data = stock.history(start=start_date, end=end_date)

    if data.empty:
        st.error(f"No data available for {stock_symbol} between {start_date} and {end_date}.")
        return
    
    pe_ratio = stock.info.get('trailingPE', None)

    if pe_ratio is None:
        st.error(f"P/E ratio data is not available for {stock_symbol}.")
        return
    
    # chart using Plotly
    fig = go.Figure()

    # Add stock's closing price to the chart
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price'))

    # Add the P/E ratio as a horizontal line 
    fig.add_trace(go.Scatter(x=data.index, y=[pe_ratio] * len(data), mode='lines', name=f'P/E Ratio: {pe_ratio}', line=dict(dash='dash')))

    fig.update_layout(
        title=f'{stock_symbol} Stock Price and P/E Ratio',
        xaxis_title='Date',
        yaxis_title='Value',
        xaxis_rangeslider_visible=True, 
        template='plotly_dark',  
        autosize=True,
    )

    # streamlit display
    st.plotly_chart(fig)


stock_symbol = (f"{st.session_state.tickermain}.NS")

col41, col42 = st.columns(2)
with col41 :
    start_date = st.date_input("Start Date", value=datetime(2023, 1, 1))
with col42 :
    end_date = st.date_input("End Date", value=datetime.today())

if stock_symbol:
        plot_stock_data(stock_symbol, start_date, end_date)

#Sales And Profit Growth Bar Chart
col1, col2 = st.columns(2)
with col1:

 def plot_sales_growth(stock_symbol):
    stock = yf.Ticker(stock_symbol)

    earnings_data = stock.quarterly_financials.T  

    if 'Total Revenue' not in earnings_data.columns:
        st.error(f"Total revenue data is not available for {stock_symbol}.")
        return

    # revenue values for the last 3 years
    revenues = earnings_data['Total Revenue'].head(12)  
    revenues = revenues[::-1]  
    
    sales_growth = revenues.pct_change() * 100  

    fig = go.Figure()

    # sales growth data as a bar chart 
    fig.add_trace(go.Bar(x=sales_growth.index, y=sales_growth, name='Sales Growth (%)', marker=dict(color='royalblue')))

    fig.update_layout(
        title=f'{stock_symbol} Sales Growth (Last 3 Years)',
        xaxis_title='Date',
        yaxis_title='Sales Growth (%)',
        template='plotly_dark',  
        autosize=True,
    )

    st.plotly_chart(fig)

 # Stock Data from main page
 stock_symbol = (f"{st.session_state.tickermain}.NS")

 if stock_symbol:
    plot_sales_growth(stock_symbol)


with col2:
 def plot_profit_growth(stock_symbol):
    stock = yf.Ticker(stock_symbol)

    earnings_data = stock.quarterly_financials.T  

    if 'Net Income' not in earnings_data.columns:
        st.error(f"Net income data is not available for {stock_symbol}.")
        return

    net_income = earnings_data['Net Income'].head(12)  
    net_income = net_income[::-1]  

    profit_growth = net_income.pct_change() * 100  

    fig1 = go.Figure()

    fig1.add_trace(go.Bar(x=profit_growth.index, y=profit_growth, name='Profit Growth (%)', marker=dict(color='green')))

    # Update layout for better interactivity
    fig1.update_layout(
        title=f'{stock_symbol} Profit Growth (Last 3 Years)',
        xaxis_title='Date',
        yaxis_title='Profit Growth (%)',
        template='plotly_dark', 
        autosize=True,
    )

    # Show the plot
    st.plotly_chart(fig1)

 # Validate if the user has entered the stock symbol
 if stock_symbol:
    plot_profit_growth(stock_symbol)


st.header("")
st.text("")


#Fundamental Analysis Description Information
url = f'https://ticker.finology.in/company/{st.session_state.tickermain}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all(class_="card cardscreen")
PE_Ratio = elements[5].text.replace('[', '')
PE = PE_Ratio.split('\n')[5:8]
PE_filtered_list = [s for s in PE if s.strip()]
PE_cleaned_list = [s.replace('\xa0', ' ').strip() for s in PE_filtered_list]
PE_final_text = ' '.join(PE_cleaned_list)
Pointer = "--"
PP = Pointer + " " + " " + PE_final_text
st.subheader(PP)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Share_Price = elements[5].text.replace('[', '')
Share = Share_Price.split('\n')[10:11]
Share_filtered_list = [s for s in Share if s.strip()]
Share_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Share_filtered_list]
Share_final_text = ' '.join(Share_cleaned_list)
PP1 = Pointer + " " + " " + Share_final_text
st.subheader(PP1)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Return_on_Investment = elements[5].text.replace('[', '')
ROA = Return_on_Investment.split('\n')[13:15]
ROA_filtered_list = [s for s in ROA if s.strip()]
ROA_cleaned_list = [s.replace('\xa0', ' ').strip() for s in ROA_filtered_list]
ROA_final_text = ' '.join(ROA_cleaned_list)
PP2 = Pointer + " " + " " + ROA_final_text
st.subheader(PP2)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Current_Raio = elements[5].text.replace('[', '')
Ratio = Current_Raio.split('\n')[15:17]
Ratio_filtered_list = [s for s in Ratio if s.strip()]
Ratio_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Ratio_filtered_list]
Ratio_final_text = ' '.join(Ratio_cleaned_list)
PP3 = Pointer + " " + " " + Ratio_final_text
st.subheader(PP3)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Return_on_Equity = elements[5].text.replace('[', '')
ROE = Return_on_Equity.split('\n')[19:22]
ROE_filtered_list = [s for s in ROE if s.strip()]
ROE_cleaned_list = [s.replace('\xa0', ' ').strip() for s in ROE_filtered_list]
ROE_final_text = ' '.join(ROE_cleaned_list)
PP4 = Pointer + " " + " " + ROE_final_text
st.subheader(PP4)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Debt_to_Equity_Raio = elements[5].text.replace('[', '')
Debt = Debt_to_Equity_Raio.split('\n')[21:23]
Debt_filtered_list = [s for s in Debt if s.strip()]
Debt_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Debt_filtered_list]
Debt_final_text = ' '.join(Debt_cleaned_list)
PP5 = Pointer + " " + " " + Debt_final_text
st.subheader(PP5)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Sales_Growth = elements[5].text.replace('[', '')
Sales = Sales_Growth.split('\n')[25:27]
Sales_filtered_list = [s for s in Sales if s.strip()]
Sales_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Sales_filtered_list]
Sales_final_text = ' '.join(Sales_cleaned_list)
PP6 = Pointer + " " + " " + Sales_final_text
st.subheader(PP6)

st.text("")

elements = soup.find_all(class_="card cardscreen")
operating_Margin = elements[5].text.replace('[', '')
Margin = operating_Margin.split('\n')[28:29]
Margin_filtered_list = [s for s in Margin if s.strip()]
Margin_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Margin_filtered_list]
Margin_final_text = ' '.join(Margin_cleaned_list)
PP7 = Pointer + " " + " " + Margin_final_text
st.subheader(PP7)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Dividend_Yield = elements[5].text.replace('[', '')
Dividend = Dividend_Yield.split('\n')[30:32]
Dividend_filtered_list = [s for s in Dividend if s.strip()]
Dividend_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Dividend_filtered_list]
Dividend_final_text = ' '.join(Dividend_cleaned_list)
PP8 = Pointer + " " + " " + Dividend_final_text
st.subheader(PP8)

st.text("")

elements = soup.find_all(class_="card cardscreen")
Earning_per_Share = elements[5].text.replace('[', '')
Earning = Earning_per_Share.split('\n')[33:35]
Earning_filtered_list = [s for s in Earning if s.strip()]
Earning_cleaned_list = [s.replace('\xa0', ' ').strip() for s in Earning_filtered_list]
Earning_final_text = ' '.join(Earning_cleaned_list)
PP9 = Pointer + " " + " " + Earning_final_text
st.subheader(PP9)

