import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html' #我們要訪問的網站
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

res =requests.get(url, headers=headers)
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
