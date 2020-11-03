import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
url='https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'

post_data_str="""method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/01/03
awardAnnounceEndDate: 109/01/03
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

#將字串處理成字典的形式
post_data ={}
for i in post_data_str.split('\n'):
    post_data[i.split(':')[0]] =i.split(':')[1]
#print(post_data)

res =requests.post(url,headers=headers,data=post_data)
soup =BeautifulSoup(res.text,'html.parser')
print(soup.prettify())

title = soup.select('div[id="print_area"] td[align="left"]')
for n, i in enumerate(title):  #n是i的index
    if (n+1) % 4 == 2:
        print(i.u.text)
    else:
        print(i.text)
    if (n+1) % 4 == 0:
        print('=' * 20)

