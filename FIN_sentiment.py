#!/usr/bin/env python
# coding: utf-8




import requests
import time
from bs4 import BeautifulSoup as bs
import re
import string
from textwrap import wrap
from nltk.sentiment import SentimentIntensityAnalyzer



companies='https://www.livemint.com/companies/news'
commodity='https://www.livemint.com/market/commodities'
stock='https://www.livemint.com/market/stock-market-news'
ipo='https://www.livemint.com/market/ipo'
mark='https://www.livemint.com/market/mark-to-market'
res1=requests.get(url=companies)
res2=requests.get(url=commodity)
res3=requests.get(url=stock)
res4=requests.get(url=ipo)
res5=requests.get(url=mark)
links=[]
check1=bs(res1.text,'html.parser')
ra1=check1.find_all('div',{'class':'listtostory clearfix'})
for i in ra1:
    links.append(i.find('a')['href'])
check2=bs(res2.text,'html.parser')
ra2=check2.find_all('div',{'class':'listtostory clearfix'})
for i in ra2:
    links.append(i.find('a')['href'])
check3=bs(res3.text,'html.parser')

ra3=check3.find_all('div',{'class':'listtostory clearfix'})
for i in ra3:
    links.append(i.find('a')['href'])

check4=bs(res4.text,'html.parser')

ra4=check4.find_all('div',{'class':'listtostory clearfix'})
for i in ra4:
    links.append(i.find('a')['href'])

check5=bs(res5.text,'html.parser')

ra5=check5.find_all('div',{'class':'listtostory clearfix'})
for i in ra5:
    links.append(i.find('a')['href'])

            
            
links_final=[]
for i in links:
    i=i.replace('[','')
    i=i.replace(']','')
    i=i.replace('"','')
    s='https://www.livemint.com/'
    s=s+i
    s=s.replace("'",'')
    links_final.append(s)
    

articles=[]
for link in links_final:
    result=requests.get(url=link)
    check=bs(result.text,'html.parser')
    string=''
    for i in range(2):
        i=check.find('p')
        #print(i.text)
        if 'Never miss a story!' in i.text:
            break
        else:
            remove=i.text.replace('\n','')
            remove=remove.replace('\t',' ')
            string+=remove

    articles.append([string,link])
    

dics=[]
rank=[]
for article in articles:
    a=sia.polarity_scores(article[0])
    a['text']=article[0]
    a['link']=article[1]
    dics.append(a)

new_dics=sorted(dics, key=lambda x:x['compound'])


least=new_dics[0:5]
most=new_dics[-5:]

show=True

while show==True:

    text='The following are the most positive financial news for today: (Score is ranked from -1 to 1 with 1 being extremely positive)'
    print(text.upper())
    print('\n')
    for i in most:
        print('SCORE:-',i['compound'],'\t','HEADLINE:-',i['text'],'\t','LINK OF ARTICLE:-',i['link'])
        print('************************************************************************************')
        print('\n')

    print('Most Negative Financial News')
    print('\n')

    for i in least:
        print('SCORE:-',i['compound'],'\t','HEADLINE:-',i['text'],'\t','LINK OF ARTICLE:-',i['link'])
        print('************************************************************************************')
        print('\n')
    show_temp=input('Do you want to run it again? (y/n)')
    if show_temp=='y':
        show=True
    else:
        show=False
