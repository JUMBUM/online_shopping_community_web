# 데이터 처리하는 라이브러리 사용하기
import pandas as pd
import cx_Oracle

def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        # 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
        dict_row[col_name[i].lower()] = row_one[i]
        
    return dict_row

def get_pay2() :
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select To_char(sum(B.prod_sale*B.cart_qty),'999,999,999') as tot_cost, 
        To_char(sum(B.del_fee),'999,999,999') as tot_del, 
        To_char(sum(B.amounts),'999,999,999') as tot_pay
    From (select prod_code, prod_name, prod_sale, cart_qty, cart_id, del_fee,(del_fee + (prod_sale * cart_qty)) as amounts 
            From prod, cart, delivery
            Where prod_code = cart_code
            And prod_code = del_code
            and cart_id = 'apple@naver.com') B
    """

    cursor.execute(sql)

    row = cursor.fetchone()

    colname=cursor.description

    # 데이터베이스의 역할은 끝남 (모든 정보를 다 가져옴) -> 접속을 끊어줘야 함


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
    #df = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.
    row_list = getDictType_FetchOne(col, row)
    return row_list

def getList_DictType_FetchAll(col_name, row) :
    list_row = []
    for columns in row :
        dict_row = {}
        
        for i in range(0, len(columns), 1) :
            # 위에 조회된 컬럼명은 대문자로 처리되기 때문에 소문자로 변환하여 사용..
            dict_row[col_name[i].lower()] = columns[i]
            
        list_row.append(dict_row)  
        
    return list_row

def get_cartlist() :
    # 오라클 연결하기
    dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것

    # 오라클 접속하기
    conn=cx_Oracle.connect('house','dbdb',dsn)

    # 1. 데이터베이스와 소통할 객체 생성
    cursor=conn.cursor()

    # 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,
    # 3. 오라클이 SQL구문을 처리한 후.

    sql = """
    select prod_code, prod_name, To_char(prod_sale,'999,999,999') as tot_price, 
        cart_qty, cart_id, To_char(del_fee,'999,999,999') as tot_delfee
    From prod, cart, delivery
    Where prod_code = cart_code
    And prod_code = del_code
    and cart_id = 'apple@naver.com'

    """

    cursor.execute(sql)

    # 4. 결과값을 커서에 실어서 보내준다.
    # 리스트 형태로 모든 데이터 읽어오기..
    row = cursor.fetchall()
    # 전체 리스트 안에 튜플 형태로 행단위로 들어있다.


    # 컬럼 이름 확인하기
    colname=cursor.description
    # 데이터베이스의 역할은 끝남 (모든 정보를 다 가져옴) -> 접속을 끊어줘야 함


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
    row_list = getList_DictType_FetchAll(col, row)
    
    return row_list


