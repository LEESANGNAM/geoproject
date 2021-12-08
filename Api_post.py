import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# 1. URL 파라미터 분리하기.
# Service URL
xmlUrl = 'https://www.koreapost.go.kr/koreapost/openapi/searchPostAreaList.do'

My_API_Key = unquote('z2210426855ek64394gd911123846')    # 아래 내가 받은 인증키가 안 되서 수업용 인증키 사용.
queryParams = '?' + urlencode(    # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
    {
        quote_plus('serviceKey') : My_API_Key,    # 필수 항목 1 : 서비스키 (본인의 서비스키)
        quote_plus('postOffiId') : 339,          # 필수 항목 2 : 지역코드
        quote_plus('nowPage') : 2,      #  page number
        quote_plus('pageCount') : 50     # 한페이지당 데이터의 갯수
     }
)
 #  url
response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# xmlobj    # 디버깅용.

rows = xmlobj.findAll('postItem') # postItem을 찾아 rows에 넣기 (row 갯수 구할 때 사용)
rows

columns = rows[0].find_all() # 1개의 로우당 가지는 데이터를 columns 에 넣기 (column 갯수 구할때 사용)
columns

rowList = []
nameList = []
columnList = []

rowsLen = len(rows)  # rows(총 행의 갯수) 의 길이를 대입
for i in range(0, rowsLen):  # 0부터 row수 만큼 반복
    columns = rows[i].find_all()  # row의 항목을 전부찾아서 대입

    columnsLen = len(columns)  # (column갯수 대입)
    for j in range(0, columnsLen):  # column 수 만큼 반복
        # 첫 번째 행 데이터 값 수집 시에만 컬럼 값을 저장한다. (어차피 rows[0], rows[1], ... 모두 컬럼헤더는 동일한 값을 가지기 때문에 매번 반복할 필요가 없다.)
        if i == 0:
            nameList.append(columns[j].name)
        # 컬럼값은 모든 행의 값을 저장해야한다.
        eachColumn = columns[j].text  # 1개 row 당 column갯수만큼 반복하면서 텍스트만 뽑는다
        columnList.append(eachColumn)  # 뽑은 텍스트를 배열에 넣어준다.
    rowList.append(columnList)  # 1개의 row를 배열에 넣어준다.
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다. (매우 중요!!)

resultDf = pd.DataFrame(rowList, columns=nameList)  # rowList를 데이터프레임으로 만들어 resultDf에 넣어준다. 컬럼명은 0번째에 뽑아놓은 nameList로 한다.
print(resultDf.head())  # 앞에서 5개의 정보를 본다.
