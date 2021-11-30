# import psycopg2
#
# def File_insert(filename,tablename):
#     try:
#         # 파일명 받아와서 열기
#         f = open(filename,'r',encoding='cp949')
#         cur.copy_from(f, tablename, sep='|') # 받아온 데이터를 입력받은 테이블에 넣기 sep: 구분자.
#     except FileNotFoundError as fileError:
#         print(fileError,"파일이없습니다.")
#     except Exception as e:
#         print(e)
#     finally:
#         f.close()
#         connection.commit()
#
# # read  ( select 결과를 리턴)
# def readDB(schema, table):
#     sql = " SELECT * from {schema}.{table}".format(schema=schema, table=table)
#     try:
#         cur.execute(sql)
#         result = cur.fetchall()
#     except Exception as e:
#         result = (" read DB err", e)
#     return result
# # db 연결
# try:
#     connection = psycopg2.connect(host="172.30.6.41", dbname="geoproject", user="postgres"
#                               , password="all4land", port=5432, options="-c search_path=lsn")
# except Exception as conError:
#         print("연결실패")
# else:
#     cur = connection.cursor()
#     File_insert('/Users/isangnam/PycharmProjects/geoproject/road_code_Sejong.txt', 'road_code')
#
#     # rows = readDB("lsn", "road_code")
#     # for i in rows:
#     #     print(i)
# finally:
#     cur.close()
#     connection.close()
#
# ## V2
# from psycopg2 import connect
#
# # postgresql 접속
# conn = connect(host='172.30.6.41',
#
#                port=5432,
#
#                database='geoproject',
#
#                user='postgres',
#
#                password='all4land')
#
# # query를 실행하기 위해 connect에 있는 cursor()를 선언
# cur = conn.cursor()
#
# # query 변수에는 postgresql에서 txt파일로 데이터를 넣을 때 사용하는 'COPY'를 선언
# query = """
#
#     COPY sye.address_infor FROM STDIN DELIMITER '|' ;
#
# """
#
# # 파일읽기 모드로 열어서 copy_expert()에 넣음
# with open('C:/Users/tjsdpdms/Desktop/all4land/address_infor.txt', 'r') as f:
#     cur.copy_expert(query, f)
#
# conn.commit()
#
# conn.close()