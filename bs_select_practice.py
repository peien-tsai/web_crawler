from urllib import request  #引入套件urllib用來request
from bs4 import BeautifulSoup #引入bs4將html標籤進行定位

url = 'https://www.ptt.cc/bbs/joke/index.html' #我們要訪問的網站

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

req = request.Request(url = url, headers=headers) #要把header跟我們的request一起送出

res = request.urlopen(req).read().decode('utf8') #取得送出的回應，得到html的原始碼

soup = BeautifulSoup(res,'html.parser')#用html.pars  er的形式處理回傳的html原始碼

title = soup.select('div[class="title"] a') #在物件導向中，變數前面底線為封裝的意思。把div這個標籤結構找出來

print(title)
'''迴圈的結果要像這個
soup.select('div[class="title"]')[0]
soup.select('div[class="title"] a')
soup.select('div[class="title"] a')[0]
soup.select('div[class="title"] a')[0].text
'''
for each_title in title:
    print(each_title.text)
    print('https://www.ptt.cc/' + each_title['href']) #抓網址
    print()


#對其他頁的網址也取得request
