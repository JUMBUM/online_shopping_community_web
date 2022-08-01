import pandas as pd
import cx_Oracle

def getCart_list():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """select post_id, post_name as "제목", maxscrap as "스크랩 수"
from post, (select max(post_scarp) as maxscrap
            from post) A
where maxscrap = post_scarp
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    df = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return df