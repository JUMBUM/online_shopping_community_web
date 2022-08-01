import pandas as pd
import cx_Oracle

def get_today():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
    Select *
From (
    Select post_name as "제목", post_id, post_date, post_hits as "스크랩 수"
    From post
    Order by post_hits Desc
)
Where Rownum <= 3
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    td = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return td