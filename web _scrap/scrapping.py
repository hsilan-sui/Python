import requests
import os
from bs4 import BeautifulSoup
import csv
import time
# import libraries => pip3 install libraries || 有時下載的python環境不同 要注意一下

results=[]
url='https://rate.bot.com.tw/xrt?Lang=zh-TW'


response = requests.get(url) #下載網頁內容
# print(response.text) # 輸出網頁html內容

# 從BeautifulSoup 說明書建立一個物件(實體化)
# soup = BeautifulSoup(response.text, 'html.parser') # 接收兩個參數(解析的網頁內容, '解析方法') | 'html.parser'=> 相容性不好
#soup = BeautifulSoup(response.text, 'lxml') 

# 將抓下來的網頁存取起來
#with open('bank_currency.html', 'w', encoding="utf-8") as file:
    #file.write(response.text) 

# soup = BeautifulSoup(response.text, 'html5lib')

# print(soup.title) #<title>臺灣銀行牌告匯率</title>

# path ='index.html'
# size= os.path.getsize(path) # 單位為bytes
# print('%s = %d bytes' % (path, size))


# 解析剛剛存取起來的網頁
with open('bank_currency.html','r', encoding="utf-8") as file:
    data = file.read(135 * 1024 * 1000) # 1k => 1024

    # 從BeautifulSoup 說明書建立一個物件(實體化)
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup.body.form.label.text)
    trs = soup.tbody.find_all('tr') # tbody標籤下的tr 成為一組LIST元素
    
    for val in trs:
         rate=[]
         currency=val.td.div.find_all('div')[1].text.strip()
        #  print(val.td.div.find_all('div')[1].text.strip()) # 幣別
         rate.append(currency)

         condition={"data-table": "本行現金買入"}
         flag = val.find(attrs=condition) # 當前"data-table": "本行現金買入"
         rate.append(flag.text)

         condition={'data-table': '本行現金賣出'}
         flag = val.find(attrs=condition) # 當前"data-table": "本行現金買入"
         rate.append(flag.text)  

         condition={'data-table': '本行即期買入'}
         flag = val.find(attrs=condition) # 當前"data-table": "本行現金買入"
         rate.append(flag.text.strip())

         condition={'data-table': '本行即期賣出'}
         flag = val.find(attrs=condition) # 當前"data-table": "本行現金買入"
         rate.append(flag.text.strip())
         results.append(rate)

print(results)
    
filename=time.strftime('%Y%m%d_%H%M%S.csv')

with open(filename, 'w', encoding='utf-8',newline='\n') as file:
     writer=csv.writer(file)
     writer.writerows(results)