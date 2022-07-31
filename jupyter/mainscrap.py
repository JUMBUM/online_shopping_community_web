{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3c88509b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 데이터 처리하는 라이브러리 사용하기\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c9dc90b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 오라클 연결, 접속, SQL구문 처리 라이브러리\n",
    "# 먼저 prompt에서 설치 : conda install -c conda-forge cx_Oracle\n",
    "# pip은 무조건 최신버전 설치, conda(install -c conda-)로 설치하면 버전 적합성을 체크한 후 설치됨 \n",
    "import cx_Oracle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a43dbcdd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=xe)))\n"
     ]
    }
   ],
   "source": [
    "# 오라클 연결하기\n",
    "dsn=cx_Oracle.makedsn('localhost',1521,'xe')    # makedsn : 오라클과 연결하기. 오라클의 주소에 통로 만드는 것\n",
    "print(dsn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "180c19f8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<cx_Oracle.Connection to house@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=xe)))>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 오라클 접속하기\n",
    "conn=cx_Oracle.connect('house','dbdb',dsn)\n",
    "conn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4c3134c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# <데이터베이스 사용방법>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "abe3eed6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<cx_Oracle.Cursor on <cx_Oracle.Connection to house@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=xe)))>>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1. 데이터베이스와 소통할 객체 생성\n",
    "cursor=conn.cursor()\n",
    "cursor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8d4fb86c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<cx_Oracle.Cursor on <cx_Oracle.Connection to house@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=xe)))>>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. SQL구문을 커서에 실어서 오라클에 전달(execute)하면,\n",
    "# 3. 오라클이 SQL구문을 처리한 후.\n",
    "\n",
    "sql = \"\"\"\n",
    "select post_id, post_name, Cast(replace(post_scarp,'-',0) as number(20)) as scrap\n",
    "from post\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "cursor.execute(sql)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c8ed3472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('apple@naver.com', '이것은 최고의 집들이입니다', 6), ('dog@nate.com', '나의 첫 집들이', 15), ('orange@naver.com', '가구 문의 드립니다', 0), ('cat@gmail.com', '핑크빛으로 물든 러블리한 나의 공간', 416), ('apple@naver.com', '낮에는 화이트톤 밤에는 술톤 신혼집', 882)]\n"
     ]
    }
   ],
   "source": [
    "# 4. 결과값을 커서에 실어서 보내준다.\n",
    "# 리스트 형태로 모든 데이터 읽어오기..\n",
    "row = cursor.fetchall()\n",
    "print(row)\n",
    "# 전체 리스트 안에 튜플 형태로 행단위로 들어있다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc2bb869",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('POST_ID', <cx_Oracle.DbType DB_TYPE_VARCHAR>, 20, 20, None, None, 0), ('POST_NAME', <cx_Oracle.DbType DB_TYPE_VARCHAR>, 50, 50, None, None, 0), ('SCRAP', <cx_Oracle.DbType DB_TYPE_NUMBER>, 21, None, 20, 0, 1)]\n"
     ]
    }
   ],
   "source": [
    "# 컬럼 이름 확인하기\n",
    "colname=cursor.description\n",
    "print(colname)\n",
    "# 데이터베이스의 역할은 끝남 (모든 정보를 다 가져옴) -> 접속을 끊어줘야 함"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "33f28cec",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. cursor를 닫은 다음, DB와의 연결을 끊어준다\n",
    "# 커서 반납하기\n",
    "cursor.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9a99934f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# DB와의 접속 끊기\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1c621b4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['POST_ID', 'POST_NAME', 'SCRAP']\n"
     ]
    }
   ],
   "source": [
    "col = []\n",
    "for i in colname :\n",
    "    col.append(i[0])\n",
    "print(col)\n",
    "# 위의 colname은 리스트형태. 거기에서 0번째 값이 모두 이름이었기 때문에 가져옴"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "80524146",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            POST_ID            POST_NAME  SCRAP\n",
      "0   apple@naver.com       이것은 최고의 집들이입니다      6\n",
      "1      dog@nate.com             나의 첫 집들이     15\n",
      "2  orange@naver.com           가구 문의 드립니다      0\n",
      "3     cat@gmail.com  핑크빛으로 물든 러블리한 나의 공간    416\n",
      "4   apple@naver.com  낮에는 화이트톤 밤에는 술톤 신혼집    882\n"
     ]
    }
   ],
   "source": [
    "# pandas를 사용한 데이터 프레임 형식으로 변환\n",
    "emp = pd.DataFrame(row, columns=col)   # row는 리스트 형태 그 안에 튜플형식으로 존재.\n",
    "print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "731d7001",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "jangminhee_kernel",
   "language": "python",
   "name": "jangminhee"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
