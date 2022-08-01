import pandas as pd
import cx_Oracle

def get_deal():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select TO_DATE(eve_edate) - TO_DATE(sysdate)||'일 남음' as "d-day", 
        prod_name as "제품명", sal_ratio||'%' as "할인율", To_char(prod_sale,'999,999,999') as "판매가", 
        (Case when del_fee in '0' then '무료배송'
                    else '유료배송'
                    END) as "배송방법"
From seller, prod, delivery, event, sale
Where sel_id = prod_id
AND prod_code = del_code
AND prod_event = eve_code
AND prod_code = sal_code
and eve_name = '오늘의 딜'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    dl = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return dl