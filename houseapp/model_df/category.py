import pandas as pd
import cx_Oracle

def get_category_gagu():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='가구'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    categg = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return categg

def get_category_gaju():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='가전'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    categj = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return categj

def get_category_deco():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='데코식물'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    catedc = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return catedc

    
def get_category_jomy():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='조명'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    catejo = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return catejo

def get_category_juba():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='주방용품'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    cateju = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return cateju

def get_category_fabr():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='패브릭'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    catefa = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return catefa

def get_category_sang():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='생필품'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    catesa = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return catesa

def get_category_suna():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select prod_name, prod_datail as prod_detail, prod_sale
from prod, sprod
where prod_sgu=sprod_gu
    and sprod_lgu='수납정리'
"""

    cursor.execute(sql)
    
    row=cursor.fetchall()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    catesn = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.

    return catesn