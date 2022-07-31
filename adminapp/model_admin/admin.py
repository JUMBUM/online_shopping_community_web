# 데이터 처리하는 라이브러리 사용하기
import pandas as pd
import cx_Oracle

def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row

def get_admin_payment():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select distinct ord_num, ord_id, prod_name, To_char(prod_sale,'999,999,999') as total_cost, 
        ord_qty, To_char(del_fee,'999,999,999') as total_delfee,       
        To_char((prod_sale * ord_qty + del_fee),'999,999,999') as total_pay , pay_mathde as total_paymathode,
        (case when pay_mathde like '%대기%' then '결제대기'
                else '결제완료'
                END) as "pay_status"
    From prod, cart, delivery, orders, payment
    Where prod_code = cart_code
    And prod_code = del_code
    AND prod_code = ord_code
    AND ord_num = pay_num
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adf = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adf

def get_admin_product():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select prod_code, prod_name, sel_name, sel_id, prod_approval
    from prod, seller
    Where prod_id = sel_id
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adp = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adp

def get_admin_stock():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select A.prod_code,A.prod_name,B.sel_name, B.sel_id, A.prod_approval, A.prod_totalstock as total_stock, A.prod_qtysale as total_sale_qty, B.buy_insqty as tota_insqty, sum(B.ord_qty) as total_saleqty 
    From prod A,(select prod_code, prod_name, sel_name, sel_id, prod_approval,ord_num,ord_qty, buy_insqty
                    from prod, seller, orders, buyprod
                    Where prod_id = sel_id
                    And prod_code = ord_code
                    And prod_code = buy_code
                    AND prod_approval in '승인완료'
                    Order by ord_num DESC) B
    Where A.prod_code = B.prod_code
    Group by A.prod_code,A.prod_name,B.sel_name, B.sel_id, A.prod_approval, A.prod_totalstock, A.prod_qtysale,B.buy_insqty
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    ads = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return ads

def get_admin_delivery():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select ord_num, ord_id, ord_qty, prod_name, pay_mathde, prod_totalstock,
       (case when pay_mathde like '%대기%' 
                OR prod_totalstock = '0' then '출고대기'
             else '출고완료'
             END) as "release_status"
    from prod, orders, payment
    Where prod_code = ord_code
    AND ord_num = pay_num

    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    add = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return add

def get_admin_mem_info():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select *
    from member
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    admi = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return admi

def get_admin_sel_info():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select *
    from seller
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adsi = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adsi

def get_admin_post():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select post_id, post_code, post_name, post_contents2, nvl(post_report,0) as report
    from post
    Where post_report != 0
    order by post_report desc
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adpost = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adpost

def get_admin_comments():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select com_id, com_code, com_contents,com_report
    from comments
    Where com_report != 0
    order by com_report desc
    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adcom = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adcom

def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row

def get_admin_notice():
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select post_id, post_code, post_name, post_contents
    from post
    Where post_gu = '공지사항'
    order by post_report desc

    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchone()

    # 컬럼 이름 확인하기
    colname=cursor.description

    # 5. cursor를 닫은 다음, DB와의 연결을 끊어준다
    # 커서 반납하기
    cursor.close()

    # DB와의 접속 끊기
    conn.close()

    col = []
    for i in colname :
        col.append(i[0])

    # 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴

    # pandas를 사용한 데이터 프레임 형식으로 변환
    adnot = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    return adnot

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

