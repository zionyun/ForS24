import pymysql

''' 
    2018/11/03 FOR S 24 PROJECT 
    MADE IN JC KIM
    DB Infomation:
        host : local host 
        port : 3306
        user : root 
        database : fors
    DEBRGE : NO (18/11/03) 

    *SQL with Python Process
        01. SQL Modul import 
        02. Using connect Method, Connected SQL & Python
        03. Call the 'Cusor' Method from Cennection object.  
        04. The DB cursor is used to manage the fetching operation.
        05. Fetch performs several functions of SQL.
'''

#Connection DATA BASE
def getConnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='0504', db='fors', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return conn

#Insert Product (Crawling)
def insert_product(data):
    result = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "INSERT INTO product(p_name, p_price, p_image, p_brand, p_event, c_card) VALUES(%s,%s,%s,%s,%s,%s)"
        result = cursor.execute(sql,data)
        cursor.close()
    except Exception as e :
        print("=================================INPUT DATA ERROR====================================",e)
    finally:
        conn.close()
    return result

#Select Product (List)
def product_list():
    rows = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql2 = "SELECT * FROM product"
        cursor.execute(sql2)
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print("===============================SELECT DARA ERROR==================================",e)
    finally:
        conn.close()
    return rows

''' Remark ==============================================================================================
    * insert_product function (by. JC kim /2018/11/03 20:15)
      - Put the crawled data in the database.
      - try/except/finally term : 
                It is a TEF syntax that you use to avoid errors.
                If an error occurs in 'Try', the 'Except' syntax works and displays the error history. 
                Otherwise, 'Finally' works normally.
      - Connection Pool Process :             
                The process is the process of using the resources and then returning them. 
                Effective use of resources in the database is important. 
                In practice, we use 'Connection Pool' to reuse resources without throwing them away.
      
'''
