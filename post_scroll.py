#網頁向下滾動會一直出現新的東西

import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://buzzorange.com/techorange/'
post_url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

#post_data_str = """action: fm_ajax_load_more
#nonce: 0b336c2ae9
#page: 10"""

post_data ={'action': 'fm_ajax_load_more','nonce': '51a5129162','page': '0'}

#for i in post_data_str.split('\n'):
#    post_data[i.split(':')[0]] = i.split(':')[1]

#post_data['page'] ='0'
#print(post_data)

for p in range(0,5):
    post_data['page'] = str(p)
    res = requests.post(post_url,headers=headers,data=post_data)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)