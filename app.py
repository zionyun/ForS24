from flask import Flask, render_template, redirect, request 
from models import dbMgr

app = Flask(__name__)

#Main Page
@app.route("/")
def main():
    return render_template('main.html')

#Login Page
@app.route("/login")
def login():
    return render_template('login.html')

#Event Page
@app.route("/event")
def event():
    rows = dbMgr.product_list()
    return render_template('event.html', rows=rows)

#Explain Page
@app.route("/explain")
def explain():
    return render_template('explain.html')

#index Page
@app.route("/index")
def index():
    return render_template('index.html')

#price Page
@app.route("/price")
def price():
    return render_template('price.html')

#cart Page
@app.route("/cart")
def cart():
    return render_template('cart.html')

#search Page
@app.route("/search")
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

'''
    2018/11/03 20:00
    project name : ForS24 Project
    function : Controller
    Default URL : Localhost (127.0.0.1:5000)
    Lib : Flask / render_template / redirect / dbMgr (Connection Pool)

    * URL (used template)
      - main : Main Page 
      - event : Event Page
      - login : Login Page 

    * Variable name
      - card Table 
        c_card : 제휴카드
        c_brand : 제휴회사
        c_rate : 할인율

      - member Table 
        num : 회원번호
        id : 회원 아이디
        pwd : 회원 비밀번호
        name : 회원 이름
        gender : 회원 성별
        birthdate : 생년월일 

      - product Table
        p_num : 상품 번호
        p_name : 상품 이름
        p_price : 상품 가격 
        p_image : 상품 이미지 (URL)
        p_brand : 상품 브랜드(편의점)
        p_event : 상품 할인정보

    Maker : JC kim 
    note : 
'''