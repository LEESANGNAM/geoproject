import psycopg2

def File_insert(filename,tablename):
    try:
        # 파일명 받아와서 열기
        f = open(filename,'r',encoding='cp949')
        cur.copy_from(f, tablename, sep='|') # 받아온 데이터를 입력받은 테이블에 넣기 sep: 구분자.
    except FileNotFoundError as fileError:
        print(fileError,"파일이없습니다.")
    except Exception as e:
        print(e)
    finally:
        f.close()
        connection.commit()

# read  ( select 결과를 리턴)
def readDB(schema, table):
    sql = " SELECT * from {schema}.{table}".format(schema=schema, table=table)
    try:
        cur.execute(sql)
        result = cur.fetchall()
    except Exception as e:
        result = (" read DB err", e)
    return result
# db 연결
try:
    connection = psycopg2.connect(host="172.30.6.41", dbname="geoproject", user="postgres"
                              , password="all4land", port=5432, options="-c search_path=lsn")
except Exception as conError:
        print("연결실패")
else:
    cur = connection.cursor()
    File_insert('/Users/isangnam/PycharmProjects/geoproject/road_code_Sejong.txt', 'road_code')

    # rows = readDB("lsn", "road_code")
    # for i in rows:
    #     print(i)
finally:
    cur.close()
    connection.close()