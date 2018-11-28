'''History
    ==========================================================================================
    * 2018 /09 /26 
    project name : Team Project
    function : Crawling
    Target : E mart (https://www.emart24.co.kr/0)
    Lib : requests / bs4

    contents : This Program is Web Crawer, We take E mart Product and insert DB.

    maker : Zion_Youn

    * 2018 /11 /03
    project name : ForS24 Project
    function : Crawling
    Target : E mart (https://www.emart24.co.kr/0)
    Lib : requests / bs4 / dbMgr (Connection Pool)

    Revise : JC kim 
    note : Fixed sending part of crawled data to 'dbMgr'. (Line 61)
    ===========================================================================================
'''


import requests  
from bs4 import BeautifulSoup
from models import dbMgr

p_name = [] # 상품이름을 담을 리스트 선언
p_image =[] #상품 이미지 url를 가져오는 리스트를 선언 
p_price =[] #상품 가격을 가져오는 리스트 선언 

# 상품리스트가 존재하는 URL을 로딩 
req = requests.get('https://www.emart24.co.kr/product/eventProduct.asp')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

#상품이름 태그를 가져오는 변수 (이름태그)
rst = soup.findAll("p",{"class":"productDiv"})
for i in range(len(rst)):
    A = []
    A = rst[i].text.strip()
    p_name.append(A)

#상품이미를 가져온다
rst2 = soup.find_all("img")
for k in range(len(rst2)):
    a = None
    a = "https://www.emart24.co.kr" + rst2[k].get("src")
    if "eventProduct" in a :
        p_image.append(a)

#상품가격을 가져온다 
rst = soup.findAll("p",{"class":"price"})
for i in range(len(rst)):
    A = []
    A = rst[i].text.strip()
    p_price.append(A)

#크롤링한 데이터를 dbMgr로 넘긴다. 
for l in range(len(p_name)):
    data = (p_name[l], p_price[l], p_image[l], 'E-Mart',0,0)
    print(data)
    dbMgr.insert_product(data)
