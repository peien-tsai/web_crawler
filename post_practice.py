import requests
from bs4 import  BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url='http://8f7c891f.ngrok.io/hello_post'

post_data = {'username':'adasfewfafds'}  #為一個字典,value會改變,所以value先隨便輸入

res = requests.post(url, headers=headers, data=post_data) #要多一個參數,跟他說data
soup = BeautifulSoup(res.text,'html.parser')
print(soup)