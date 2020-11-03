#對其他頁的網址也取得request

from urllib import request  #引入套件urllib用來request
from bs4 import BeautifulSoup #引入bs4將html標籤進行定位

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


page = 8660
for i in range(0,10): #假設我們要爬10頁
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page) #我們要訪問的網站  ---%s作為變數

    req = request.Request(url = url, headers=headers) #要把header跟我們的request一起送出

    res = request.urlopen(req).read().decode('utf8') #取得送出的回應，得到html的原始碼

    soup = BeautifulSoup(res,'html.parser')#用html.parser的形式處理回傳的html原始碼

    title = soup.select('div[class="title"] a') #在物件導向中，變數前面底線為封裝的意思。把div這個標籤結構找出來

    for each_title in title:
        print(each_title.text)
        try:
            print('https://www.ptt.cc/' + each_title['href']) #抓網址
        except KeyError as e:
            print(e.args)
        print()

    page -= 1
