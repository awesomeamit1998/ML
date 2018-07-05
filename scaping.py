
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:19:26 2018

@author: Amit Jena
"""

# ML
#web scraping of hotel lee reviews
import requests
from bs4 import BeautifulSoup
a=[]
b=[]
#base_url="https://www.tripadvisor.in/Hotel_Review-g503703-d1179487-Reviews-or{}-Lee_Garden_Hotel-Puri_Puri_District_Odisha.html"
for page in range(0,65,5):
    c=requests.get("https://www.tripadvisor.in/Hotel_Review-g503703-d1179487-Reviews-or"+str(page)+"-Lee_Garden_Hotel-Puri_Puri_District_Odisha.html")
    t=c.content
    soup=BeautifulSoup(t,"html.parser")
    right_table=soup.find("div",class_="content_column ui_column is-8-desktop is-12")
    for row in right_table.findAll("div",class_="quote"):
        print("Scraping please wait", ,end=' ')
        cells=row.findAll("span",class_="noQuotes")
        b.append(cells[0].find(text=True))
        print('.')
import pandas as pd
df=pd.DataFrame()
df['sl no']=a
df['Reviews']=b
print(df)
df.to_csv('amit1st.csv')
