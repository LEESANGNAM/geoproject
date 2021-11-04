import psycopg2

# db 연결
connection = psycopg2.connect(host="172.30.6.41", dbname="geoproject", user="postgres", password="all4land", port=5432)

cur = connection.cursor()
# 커서에 객체가 있다면 연결성공
if cur != None:
    print("연결성공")

f = open(r'C:UsersnDesktopdata.csv', 'r')
cur.copy_from(f, temp_unicommerce_status, sep=',')


#
# # insert
# def insertDB(schema, table,data):
#     sql = " INSERT INTO {schema}.{table} VALUES ({data}) ;".format(schema=schema, table=table,
#                                                                                data=data)
#     try:
#         cur.execute(sql)
#         connection.commit()
#     except Exception as e:
#         print(" insert DB err ", e)
# # read  ( select 결과를 리턴)
# def readDB(schema, table):
#     sql = " SELECT * from {schema}.{table}".format(schema=schema, table=table)
#     try:
#         cur.execute(sql)
#         result = cur.fetchall()
#     except Exception as e:
#         result = (" read DB err", e)
#
#     return result
# insertDB("lsn","road_code","'4','2','3','7','5','6','7','8','9','0','1','2','3','4','5','6','7'")
# print(readDB("lsn","road_code"),end=" ")
#
# cur.close()
# connection.close()
#
