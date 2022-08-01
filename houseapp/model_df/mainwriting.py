import pandas as pd
import cx_Oracle
from scipy.fft import hfft2

def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row

def get_postname_mw():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    sql = """
select post_name, post_contents2, post_id
from post, (select max(post_scarp) as maxscrap
            from post) A
where maxscrap = post_scarp
"""

    cursor.execute(sql)
    
    row=cursor.fetchone()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    #pnmw = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    
    row_dict=getDictType_FetchOne(col, row)

    return row_dict



def get_postcomm_mw():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    # sql = """select nvl(mem_name,'없음')as mem_name, sel_name, com_contents
    # from act, comments, member, seller
    # where act_id=mem_id(+)
    # and com_id(+)=act_id
    # and sel_id(+)=act_id
    # and com_code='gk1236'
    # and sel_name='박바나'"""
    
    sql = """ select nvl(mem_name,'없음')as mem_name, 
                sel_name, com_contents
                from act left outer join member
                on(act_id=mem_id)
                left outer join comments
                on(com_id=act_id)
                left outer join seller
                on(sel_id=act_id)     
                where com_code='gk1236'
                and sel_name='박바나' """

    # sql = """
    # select post_name as mem_name, 
    # post_contents2 as sel_name, post_id as com_contents
    # from post, (select max(post_scarp) as maxscrap
    #             from post) A
    # where maxscrap = post_scarp
    # """

    cursor.execute(sql)
    
    row=cursor.fetchone()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    #row_dict = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    
    row_dict=getDictType_FetchOne(col, row)

    return row_dict

def get_postcomm_mw2():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    # sql = """select nvl(mem_name,'없음')as mem_name, sel_name, com_contents
    # from act, comments, member, seller
    # where act_id=mem_id(+)
    # and com_id(+)=act_id
    # and sel_id(+)=act_id
    # and com_code='gk1236'
    # and sel_name='박바나'"""
    
    sql = """ select nvl(mem_name,'없음')as mem_name, 
                sel_name, com_contents
                from act left outer join member
                on(act_id=mem_id)
                left outer join comments
                on(com_id=act_id)
                left outer join seller
                on(sel_id=act_id)     
                where com_code='gk1236'
                and sel_name='심판다' """

    # sql = """
    # select post_name as mem_name, 
    # post_contents2 as sel_name, post_id as com_contents
    # from post, (select max(post_scarp) as maxscrap
    #             from post) A
    # where maxscrap = post_scarp
    # """

    cursor.execute(sql)
    
    row=cursor.fetchone()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    #row_dict = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    
    row_dict=getDictType_FetchOne(col, row)

    return row_dict





def get_postcomm_mw3():
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')  

    conn=cx_Oracle.connect('house','dbdb',dsn)
    
    cursor=conn.cursor()


    # sql = """select nvl(mem_name,'없음')as mem_name, sel_name, com_contents
    # from act, comments, member, seller
    # where act_id=mem_id(+)
    # and com_id(+)=act_id
    # and sel_id(+)=act_id
    # and com_code='gk1236'
    # and sel_name='박바나'"""
    
    sql = """select nvl(mem_name,'없음')as mem_name, 
                sel_name, com_contents
                from act left outer join member
                on(act_id=mem_id)
                left outer join comments
                on(com_id=act_id)
                left outer join seller
                on(sel_id=act_id)     
                where com_code='gk1236'
                and mem_name='김사과' """

    # sql = """
    # select post_name as mem_name, 
    # post_contents2 as sel_name, post_id as com_contents
    # from post, (select max(post_scarp) as maxscrap
    #             from post) A
    # where maxscrap = post_scarp
    # """

    cursor.execute(sql)
    
    row=cursor.fetchone()


    colname=cursor.description

    cursor.close()

    conn.close()

    col = []
    for i in colname :
        col.append(i[0])
    

    #row_dict = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    
    row_dict=getDictType_FetchOne(col, row)

    return row_dict