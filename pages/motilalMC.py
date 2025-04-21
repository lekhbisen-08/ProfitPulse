from re import S
import requests
from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd

# This hides the sidebar on load
st.set_page_config(
    page_title="Your Page Title",
    layout="wide",
    initial_sidebar_state="collapsed"  
)

url = f'https://groww.in/mutual-funds/motilal-oswal-most-focused-midcap-30-fund-direct-growth'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

elements = soup.find_all(class_="pc543Links")
elementdata = soup.find_all(class_="fd12Header contentSecondary bodyLarge")
data = soup.find_all(class_="fd12Cell contentPrimary bodyLargeHeavy")

name =  "Motilal Oswal Midcap Fund Direct Growth"
col1, col2 = st.columns([4,2])
with col1 :
    st.header(name)
with col2:
 if st.button("Return Back") :
  st.switch_page("pages/Mutual_Fund.py")

st.text("")

space = " "
colon = " : "

#INFO PAGE
col1, col2, col3, col4 = st.columns(4)


nav = elementdata[0].text
navdata = soup.find(class_="fd12Cell contentPrimary bodyLargeHeavy").text
with col1:
    st.subheader(nav + colon + navdata)

rating = elementdata[2].text
ratingdata = soup.find(class_="fd12Cell valign-wrapper contentPrimary fd12Ratings bodyLargeHeavy").text
with col2:
    st.subheader(rating + colon + ratingdata + space + "Star")

sipamt = elementdata[1].text
sipamtdata = data[1].text
with col3:
    st.subheader(sipamt + colon + sipamtdata)

fundsize = elementdata[3].text
fundsizedata = data[2].text
with col4:
    st.subheader(fundsize + colon + fundsizedata)


st.text("")
st.text("")

#RETURNS 1y 3y 5y All PAGE
returndata = soup.find_all(class_="contentSecondary")
alldata = soup.find_all(class_="tb10Td")

fund = returndata[21].text
fund1 = alldata[0].text
fund3 = alldata[1].text
fund5 = alldata[2].text
fundall = alldata[3].text

category = returndata[22].text
cat1 = alldata[4].text
cat3 = alldata[5].text
cat5 = alldata[6].text
catall = alldata[7].text

rank = returndata[23].text
rank1 = alldata[8].text
rank3 = alldata[9].text
rank5 = alldata[10].text
rankall = alldata[11].text

data = {
    "Category": [fund, category, rank],
    "1Y": [fund1, cat1, rank1 + "%"],
    "3Y": [fund3, cat3, rank3 + "%"],
    "5Y": [fund5, cat5, rank5 + "%"],
    "All": [fundall, catall, rankall]
}
df = pd.DataFrame(data)
st.subheader("Annualised Returns")
st.data_editor(df, hide_index=True, use_container_width=True)

st.text("")
st.text("")

# TOP 10 Holding Page
holding = soup.find_all(class_="pc543Links")
sector = soup.find_all(class_="bodyBase")
c1 = holding[5].text
s1 = sector[28].text
a1 = sector[30].text
c2 = holding[6].text
s2 = sector[32].text
a2 = sector[34].text
c3 = holding[7].text
s3 = sector[36].text
a3 = sector[38].text
c4 = holding[8].text
s4 = sector[40].text
a4 = sector[42].text
c5 = holding[9].text
s5 = sector[44].text
a5 = sector[46].text
c6 = holding[10].text
s6 = sector[48].text
a6 = sector[50].text
c7 = holding[11].text
s7 = sector[52].text
a7 = sector[54].text
c8 = holding[12].text
s8 = sector[56].text
a8 = sector[58].text
c9 = holding[13].text
s9 = sector[60].text
a9 = sector[62].text
c10 = holding[14].text
s10 = sector[64].text
a10 = sector[66].text
companies = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
sectors = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
assets = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
df = pd.DataFrame({
    "Company": companies,
    "Sector": sectors,
    "Asset %": assets
})
st.subheader("Top 10 Holdings")
st.data_editor(df, hide_index=True, use_container_width=True)

st.text("")
st.text("")

#Peer Comparision Page
peer = soup.find_all(class_="pc543Links")
peer1 = peer[0].text
peer2 = peer[1].text
peer3 = peer[2].text
peer4 = peer[3].text
peer5 = peer[4].text
peer1y3y = soup.find_all(class_="left-align bodyBase")
p1y1 = peer1y3y[0].text
p3y2 = peer1y3y[1].text
p1y3 = peer1y3y[2].text
p3y4 = peer1y3y[3].text
p1y5 = peer1y3y[4].text
p3y6 = peer1y3y[5].text
p1y7 = peer1y3y[6].text
p3y8 = peer1y3y[7].text
p1y9 = peer1y3y[8].text
p3y10 = peer1y3y[9].text
peerfund = soup.find_all(class_="right-align bodyBase")
pf1 = peerfund[0].text
pf2 = peerfund[1].text
pf3 = peerfund[2].text
pf4 = peerfund[3].text
pf5 = peerfund[4].text
peers = [peer1, peer2, peer3, peer4, peer5]
returns_1y = [p1y1, p1y3, p1y5, p1y7, p1y9]
returns_3y = [p3y2, p3y4, p3y6, p3y8, p3y10]
fund_types = [pf1, pf2, pf3, pf4, pf5]
peer_df = pd.DataFrame({
    "Peer Name": peers,
    "1Y Return": returns_1y,
    "3Y Return": returns_3y,
    "Fund Type": fund_types
})
st.subheader("Peer Comparison")
st.data_editor(peer_df, hide_index=True, use_container_width=True)

st.text("")
st.text("")

#Expense Ratio, Exit Load and Tax
expenseratio = soup.find_all(class_="ot654subHeading bodyLargeHeavy")
er = expenseratio[0].text
st.subheader(er)

st.text("")

col6, col7 = st.columns(2)

exitload = soup.find_all(class_="bodyLarge")
el = exitload[10].text
with col6:
    st.subheader(el)

stampduty = soup.find_all(class_="ot654subHeading bodyLargeHeavy")
std = soup.find_all(class_="bodyLarge")
sd = stampduty[2].text
std = std[11].text
with col7:
    st.subheader(sd + space + colon + space + std)

st.text("")

taximplication = soup.find_all(class_="ot654subHeading bodyLargeHeavy")
taxim = soup.find_all(class_="bodyLarge")
tax = taximplication[3].text
taxim = taxim[12].text
st.subheader(tax + space + colon + space + taxim)



