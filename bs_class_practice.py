from urllib import request  #引入套件urllib用來request
from bs4 import BeautifulSoup #引入bs4將html標籤進行定位

url = 'https://www.ptt.cc/bbs/joke/index.html' #我們要訪問的網站

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

req = request.Request(url = url, headers=headers) #要把header跟我們的request一起送出

res = request.urlopen(req).read().decode('utf8') #取得送出的回應，得到html的原始碼

soup = BeautifulSoup(res,'html.parser')#用html.parser的形式處理回傳的html原始碼

title = soup.findAll('div',class_ = 'title') #在物件導向中，變數前面底線為封裝的意思。把div這個標籤結構找出來
print(title)  #找出來的標題會印出一個list

#把每個標題的字串從list取出來
'''findAll('a')的意思
print(title[0])
each_title = title[0].findAll('a')
print(each_title[0].text)
'''
for title_html in title:
    try:
        print(title_html.findAll('a')[0].text)
    except IndexError as e:
        print(e.args)
    print('=========') #分隔