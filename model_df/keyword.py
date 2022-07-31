import pandas as pd
import cx_Oracle
from scipy.fft import hfft2

def get_keyword():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select tag_name as "HASH TAG"
from tag
group by tag_name
having count(tag_name)>(select avg(count(tag_name))
                 		from tag
                    	group by tag_name)
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    kw = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return kw

def get_hashtag():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from pprod, (select tag_code as tagcode
                    from tag
                    where tag_name='#심플함'), prod
where pprod_post=tagcode
    and prod_code=pprod_code

"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    ht = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return ht

def get_hashtag2():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail, prod_sale
from pprod, (select tag_code as tagcode
                    from tag
                    where tag_name='#나홀로족'), prod
where pprod_post=tagcode
    and prod_code=pprod_code

"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    ht2 = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return ht2