import requests
import json
from urllib import request
import os
if not os.path.exists(r'./dcard_img'): #r 所有跳脫字元皆無效
    os.mkdir(r'./dcard_img')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232802588'
res = requests.get(url=url, headers=headers)
print(res.text)
tmp_json = json.loads(res.text)  # 對內容轉置成json格式，為一個字典的資料格式
#print(tmp_json[0])
#for k in tmp_json[0]:
#   print(k)  # 對字典使用for迴圈，列印出來的只會出現key值

#for i in tmp_json[0]['mediaMeta']:  # 找出可能對應照片的 key值
#    print(i)

for each_title in tmp_json:  # 找出第0項的圖片網址  #取出json字典的key值
    article_title = each_title['title'].replace('/','')
    if not os.path.exists(r'/dcard_img/%s'%(article_title)):
        os.mkdir(r'./dcard_img/%s'%(article_title))
    print(each_title['title'])
    print('https://www.dcard.tw/f/photography/p/' + str(each_title['id']))
    for img_url_dict in each_title['mediaMeta']: #圖片的網址 mediaMeta字串內取出的每個 img_url_dict字典
        img_url = img_url_dict['url']
        try:
            request.urlretrieve(img_url,r'./dcard_img/%s/%s'%(article_title,img_url.split('/')[-1]))
        except:
            pass
        print('\t%s' % (img_url))

    print() 



