#對其他頁的網址也取得request

from urllib import request  #引入套件urllib用來request
from bs4 import BeautifulSoup #引入bs4將html標籤進行定位
import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'
for i in range(0,10): #假設我們要爬10頁

    req = request.Request(url = url, headers=headers) #要把header跟我們的request一起送出

    res = request.urlopen(req).read().decode('utf8') #取得送出的回應，得到html的原始碼

    soup = BeautifulSoup(res,'html.parser')#用html.parser的形式處理回傳的html原始碼

    title = soup.select('div[class="title"] a') #在物件導向中，變數前面底線為封裝的意思。把div這個標籤結構找出來

    for each_title in title:
        print(each_title.text)
        try:
            article_url = 'https://www.ptt.cc/'+each_title['href'] #抓文章內容
            print(article_url)
            res_article = requests.get(article_url,headers = headers)
            article_soup = BeautifulSoup(res_article.text, 'html.parser')
        except KeyError as e:
            print(e.args)
        print()


    # 如果上下頁網址編碼沒有規律，下兩行取得網址
    url_list = soup.select('div[class="btn-group btn-group-paging"] a[class="btn wide"] ')  #我要取得<上頁 按鈕的網址  div[class="btn-group btn-group-paging"] 裡的a標籤的東西，然後再取得裡面的網址
    url = 'https://www.ptt.cc/'+url_list[1]['href'] #因上行取得的網址不完整，所以前面再加上https://www.ptt.cc/


