import pandas as pd
import cx_Oracle
def getList_DictType_FetchAll(col_name, row) :
    list_row = []
    for columns in row :
        dict_row = {}
        
        for i in range(0, len(columns), 1) :
            # 위에 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
            dict_row[col_name[i].lower()] = columns[i]
            
        list_row.append(dict_row)  
        
    return list_row

def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row
def posttop1() :

    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1235'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df = pd.DataFrame(row, columns=col)
    df = getDictType_FetchOne(col, row)

    return df

def postmid1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select sel_name, prod_name, prod_sale
From post
    Inner Join pprod
    On (pprod_post = post_code)
    Inner Join prod
    On (pprod_code = prod_code)
    Inner Join seller
    On (sel_id = prod_id)
Where post_code = 'gk1234'"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df1_1 = getDictType_FetchOne(col, row)
    return df1_1

def postbot1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1235'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df1 = getDictType_FetchOne(col, row)
    return df1

def posttop2() :
    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1237'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df = pd.DataFrame(row, columns=col)
    df2 = getDictType_FetchOne(col, row)

    return df2

def postbot2() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1237'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df3 = getDictType_FetchOne(col, row)
    return df3

def posttop3() :
    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1234'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df = pd.DataFrame(row, columns=col)
    df4 = getDictType_FetchOne(col, row)

    return df4

def postbot3() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1234'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df5 = getDictType_FetchOne(col, row)
    return df5

def posttop4() :
    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1238'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df = pd.DataFrame(row, columns=col)
    df6 = getDictType_FetchOne(col, row)

    return df6

def postbot4() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select post_id, post_code, mem_id, tag_code, mem_profile, post_date, post_name, Listagg(Distinct tag_name)
from post, member,tag, (select fo_follwing as ffollower
                        from follow
                        where fo_follow = 'orange@naver.com')
where post_id=ffollower
    and post_id=mem_id
    and tag_code=post_code
    And post_code = 'gk1238'
Group by post_id, post_code,mem_id, tag_code, mem_profile, post_date, post_name"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df7 = getDictType_FetchOne(col, row)
    return df7

def gal1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1234'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    df8 = getDictType_FetchOne(col, row)
    return df8

def gal2() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1235'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df9 = getDictType_FetchOne(col, row)
    return df9

def gal3() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1237'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df10 = getDictType_FetchOne(col, row)
    return df10

def gal4() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1238'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df11 = getDictType_FetchOne(col, row)
    return df11

def gal5() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1238'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    df12 = getDictType_FetchOne(col, row)
    return df12

def gal6() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1237'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df13 = getDictType_FetchOne(col, row)
    return df13

def gal7() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1235'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df14 = getDictType_FetchOne(col, row)
    return df14

def gal8() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1234'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df15 = getDictType_FetchOne(col, row)
    return df15

def gk1234main() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field, Listagg(Distinct tag_name)
    From post
    Inner Join tag
    On (post_code = tag_code)
Where post_code = 'gk1234'
Group by post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df16 = getDictType_FetchOne(col, row)
    return df16

def gk1234prod() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1234'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df17 = getDictType_FetchOne(col, row)
    return df17

def gk1234com1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select mem_name, sel_name, com_contents
from act, comments, member, seller
where act_id=mem_id(+)
    and com_id(+)=act_id
    and sel_id(+)=act_id
    and com_code='gk1234'"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df18 = getDictType_FetchOne(col, row)
    return df18

def gk1235main() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field, Listagg(Distinct tag_name)
    From post
    Inner Join tag
    On (post_code = tag_code)
Where post_code = 'gk1235'
Group by post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df19 = getDictType_FetchOne(col, row)
    return df19

def gk1235prod() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1235'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df20 = getDictType_FetchOne(col, row)
    return df20

def gk1235com1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select mem_name, sel_name, com_contents
from act, comments, member, seller
where act_id=mem_id(+)
    and com_id(+)=act_id
    and sel_id(+)=act_id
    and com_code='gk1235'"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df21 = getDictType_FetchOne(col, row)
    return df21

def gk1237main() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field, Listagg(Distinct tag_name)
    From post
    Inner Join tag
    On (post_code = tag_code)
Where post_code = 'gk1237'
Group by post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df22 = getDictType_FetchOne(col, row)
    return df22

def gk1237prod() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1237'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df23 = getDictType_FetchOne(col, row)
    return df23

def gk1237com1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select mem_name, sel_name, com_contents
from act, comments, member, seller
where act_id=mem_id(+)
    and com_id(+)=act_id
    and sel_id(+)=act_id
    and com_code='gk1237'"""

    cursor.execute(sql) 
    row=cursor.fetchall() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df24 = getList_DictType_FetchAll(col, row)
    return df24

def gk1238main() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field, Listagg(Distinct tag_name)
    From post
    Inner Join tag
    On (post_code = tag_code)
Where post_code = 'gk1238'
Group by post_gu, post_name, post_contents2, post_id, post_type, post_size, post_budget, post_family, post_style, post_color, post_detail, post_field"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df25 = getDictType_FetchOne(col, row)
    return df25

def gk1238prod() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """Select post_name, post_id, post_hits, post_like
From post
Where post_gu = '온라인 집들이'
And post_code = 'gk1238'
order by post_date desc"""

    cursor.execute(sql) 
    row=cursor.fetchone() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df26 = getDictType_FetchOne(col, row)
    return df26

def gk1238com1() :    
    dsn=cx_Oracle.makedsn('localhost',1521,'xe') 
    conn=cx_Oracle.connect('house','dbdb', dsn)
    cursor=conn.cursor() 

    sql = """select mem_name, sel_name, com_contents
from act, comments, member, seller
where act_id=mem_id(+)
    and com_id(+)=act_id
    and sel_id(+)=act_id
    and com_code='gk1238'"""

    cursor.execute(sql) 
    row=cursor.fetchall() 
    colname=cursor.description

    cursor.close()
    conn.close()

    col=[] 
    for i in colname: 
        col.append(i[0])
    #df1 = pd.DataFrame(row, columns=col)
    df27 = getList_DictType_FetchAll(col, row)
    return df27

