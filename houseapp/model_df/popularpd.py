import pandas as pd
import cx_Oracle

def get_populpd():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
Select prod_name as 제품명, prod_sale as 가격
From orders 
    Inner Join prod
    On(prod_code = ord_code)
Where Rownum <= 3
Group By prod_name, prod_sale
Order By Count(ord_num) Desc


"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    ppd = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return ppd