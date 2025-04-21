import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import time
import seaborn as sns
import matplotlib.gridspec as gridspec
import plotly.graph_objs as go

#     *******use this in place of ticker main******* 
#              st.session_state.tickermain   


# Page Configuration
st.set_page_config(
    page_title="Profit Pulse",
    page_icon="balance.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page Theme
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
img=Image.open("pages/mutuallogo.png")
img_resized = img.resize((100,100))

st.sidebar.image(img,use_container_width=True)

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Finology API Insertion
tickermain = st.session_state.tickermain

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
   
   if st.button("Technical Analysis"):
      st.switch_page("pages/Technicals.py")
   st.text("")
   if st.button("Stock \n Prediction"):
      st.switch_page("pages/Prediction.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Mutual Fund Search tag
if st.sidebar.button(f"\u2003\u2003Home Page -- Profit Pulse\u2003\u2003"):
    st.switch_page("ProfitPulse.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

 #News Button
if st.sidebar.button(f"Keep Updated by Latest News by \n Money Pulse"):
    st.switch_page("pages/News.py")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

#Information Page
st.sidebar.button(f"More Information About \n {tickermain}.LTD")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.button("\u2003\u2003\u2003\u00A0\u00A0\u00A0\u00A0\u00A0About Profit Pulse \u00A0\u2003\u2003\u2003")

st.title("📊 Mutual Fund Investment Dashboard")

mf_type = st.radio(
    "Select a Mutual Fund Category",
    ("Large Cap", "Mid Cap", "Small Cap", "Flexi Cap", "Multi Cap"),
    horizontal=True
)

fund_pages = {
    "Large Cap": {
        "Nippon India Large Cap Fund": "pages/nipponLC.py",
        "ICICI Pudential Bluechip Fund": "pages/iciciLC.py",
        "SBI Bluechip Direct Plan Growth":"pages/sbiLC.py",
        "UTI Nifty 50 Index Fund":"pages/utiLC.py",
        "Navi Nifty 50 Index Fund":"pages/naviLC.py"
    },
    "Mid Cap": {
        "Motilal Oswal Midcap Fund Direct Growth":"pages/motilalMC.py",
        "HDFC Mid Cap Opportunities Fund Direct Growth":"pages/hdfcMC.py",
        "SBI Magnum Mid Cap Direct Plan Growth":"pages/sbiMC.py",
        "Quant Mid Cap Fund Direct Growth":"pages/quantMC.py",
        "Kotak Emerging Equity Fund Direct Growth":"pages/kotakMC.py"
    },
    "Small Cap": {
        "Nippon India Small Cap Fund": "SmallCap_Nippon"
    },
    "Flexi Cap": {
        "Parag Parikh Flexi Cap Fund": "FlexiCap_Parag"
    },
    "Multi Cap": {
        "Motilal Oswal Multi Cap Fund": "MultiCap_Motilal"
    }
}

st.markdown(f"### 🏆 Top {mf_type} Funds")
selected_fund = st.selectbox("Select Fund", list(fund_pages[mf_type].keys()))

if st.button("🔁 Go to Fund Page"):
    st.switch_page(fund_pages[mf_type][selected_fund])

# You can keep the educational info below...

st.divider()

# Informational section
st.header("📚 About Mutual Funds")

st.markdown("""
**What are Mutual Funds?**  
A mutual fund is a pool of money collected from multiple investors, managed by professionals, and invested in stocks, bonds, or other assets. It's ideal for those who want exposure to markets without selecting individual stocks.

---

### 💡 Why Invest in Mutual Funds?
- 🛡️ **Diversification**: Lowers your risk by spreading investments.
- 👨‍💼 **Expert Management**: Run by experienced fund managers.
- 🧱 **Low Entry Point**: Start with as little as ₹500.
- 💰 **Tax Benefits**: ELSS schemes offer tax deductions under Section 80C.
- 🔓 **Liquidity**: Easy to redeem anytime (except lock-in funds).
- 🔍 **Transparency**: NAV and holdings published regularly.

---

### 🏦 Types of Mutual Fund Categories

#### 🔵 Large Cap
- Invests in top 100 companies by market capitalization.
- Stable and less volatile.
- Great for long-term and conservative investors.

#### 🟠 Mid Cap
- Companies ranked 101–250.
- Balance between risk and reward.
- Best for medium-term investors.

#### 🔴 Small Cap
- Invests in companies ranked 251 and below.
- High growth potential but more volatile.
- Suitable for aggressive investors with longer horizons.

#### 🟢 Flexi Cap
- Dynamic allocation across large, mid, and small cap.
- Fund manager adjusts based on market condition.
- Great for those seeking diversification and flexibility.

#### 🟣 Multi Cap
- Minimum 25% in each of large, mid, and small caps.
- Diversified across all segments.
- Balanced option for varied risk appetite.

---

🧭 *Choose a category based on your goals, risk profile, and investment duration.*
""")



