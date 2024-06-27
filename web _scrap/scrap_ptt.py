import requests
import os
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/Python/index.html'
response = requests.get(url)

# 寫入爬下來的檔案
# with open('ptt.html','w', encoding="utf-8") as file:
#     file.write(response.text)

# 計算檔案大小 (1024 bytes => 1kb)
path ='ptt.html'
size= os.path.getsize(path) # 單位為bytes
ksize = round(size/1024)
print('%s = %d kbytes' % (path, ksize))


# 讀取檔案內容
with open('ptt.html','r',encoding="utf-8") as file:
    data = file.read(size * 1024 *10) # 原來檔案大小的10倍

    #g實體化 + 用html.parser解析檔案
    soup = BeautifulSoup(data, 'html.parser')
    q={'class':"r-ent"}
    ques=soup.find_all(attrs=q)
    for que in ques:
        print(que.find('a').text)

        

# print(f'PTT Python版近期前{len(ques)}個主題:{result}')