import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# 1. URL 파라미터 분리하기.
# Service URL
xmlUrl = 'https://www.koreapost.go.kr/koreapost/openapi/searchPostAreaList.do'

My_API_Key = unquote('z2210426855ek64394gd911123846')    # 아래 내가 받은 인증키가 안 되서 수업용 인증키 사용.
# My_API_Key = unquote('Agq7hySmyMi1FFU9kYibP%2BEnxYepQ%2FB6Dn%2Bw9lsYKVSCDjTwIdvpjmuhJrtyQrhipg3F3a4jbSq%2FLxHi%2FdUIoQ%3D%3D')    # 사용자 인증키
queryParams = '?' + urlencode(    # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
    {
        quote_plus('serviceKey') : My_API_Key,    # 필수 항목 1 : 서비스키 (본인의 서비스키)
        quote_plus('postOffiId') : 339,          # 필수 항목 2 : 지역코드 (법정코드목록조회에서 확인)
        quote_plus('nowPage') : 2,      # 픽수 항목 3 : 계약월
        quote_plus('pageCount') : 50
     }
)

response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# print(xmlobj)    # 디버깅용.

rows = xmlobj.findAll('postItem')
# print(rows[1])
columns = rows[0].find_all()
# print(columns)

rowList = []
nameList = []
columnList = []

rowsLen = len(rows)
for i in range(0, rowsLen):
    columns = rows[i].find_all()

    columnsLen = len(columns)
    for j in range(0, columnsLen):
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행의 값을 저장해야한다.
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)

result = pd.DataFrame(rowList, columns=nameList)
print(result)

