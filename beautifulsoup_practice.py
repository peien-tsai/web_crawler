from urllib import request  #引入套件urllib用來request
from bs4 import BeautifulSoup #引入bs4將html標籤進行定位

url = 'https://www.ptt.cc/bbs/joke/index.html' #我們要訪問的網站

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
#↑這台電腦的授權
req = request.Request(url = url, headers=headers) #要把header跟我們的request一起送出
res = request.urlopen(req).read().decode('utf8') #取得送出的回應，得到html的原始碼

soup = BeautifulSoup(res,'html.parser')#用html.parser的形式處理回傳的html原始碼
# print(soup)

logo = soup.findAll('a', {'id':'logo'})
print(logo)
print('')
print(logo[0])
print('')
print(logo[0].text)
print('')
print(logo[0].string)
print('')
print(logo[0]['href'])

