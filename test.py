#!/usr/bin/env python
# coding: utf-8

# In[83]:

import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

# 1. URL 파라미터 분리하기.
# Service URL
xmlUrl = 'https://www.koreapost.go.kr/koreapost/openapi/searchPostAreaList.do'

My_API_Key = unquote('z2210426855ek64394gd911123846')  # 아래 내가 받은 인증키가 안 되서 수업용 인증키 사용.
# My_API_Key = unquote('Agq7hySmyMi1FFU9kYibP%2BEnxYepQ%2FB6Dn%2Bw9lsYKVSCDjTwIdvpjmuhJrtyQrhipg3F3a4jbSq%2FLxHi%2FdUIoQ%3D%3D')    # 사용자 인증키
queryParams = '?' + urlencode(  # get 방식으로 쿼리를 분리하기 위해 '?'를 넣은 것이다. 메타코드 아님.
    {
        quote_plus('serviceKey'): My_API_Key,  # 필수 항목 1 : 서비스키 (본인의 서비스키)
        quote_plus('postOffiId'): 339,  # 필수 항목 2 : 지역코드 (법정코드목록조회에서 확인)
        quote_plus('nowPage'): 2,  # 픽수 항목 3 : 계약월
        quote_plus('pageCount'): 50
    }
)
response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
# xmlobj    # 디버깅용.


# In[84]:


rows = xmlobj.findAll('postItem')
rows[1]

# In[85]:


columns = rows[0].find_all()
columns

# In[86]:


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
    columnList = []  # 다음 row의 값을 넣기 위해 비워준다.
resultDf = pd.DataFrame(rowList, columns=nameList)
resultDf.tail()

# In[127]:

resultDf2 = resultDf[["postId", "postDiv", "postNm", "postAddr"]]
# 필요한 아이디 우체국이름, 주소와, 우체국인지를 판별하는 div 컬럼 가져와 새로운 데이터프레임 생성
isPost = resultDf2["postDiv"].str.contains("1|0")
# div컬럼에서 0:총괄 1: 우체국  이므로 두개중에 하나라도 일치하는 값을 저장
resultDf3 = resultDf2[isPost].drop(['postDiv'], axis=1).reset_index().drop(['index'], axis=1)
# 트루인 값들로 새로운 데이터프레임을 생성한 후 div컬럼을 삭제. , 인덱스도 33부터 시작하기때문에 0 부터시작하기 위해 삭제.
resultDf3

# In[135]:


resultDf3.loc[0]['postAddr'] = resultDf3.loc[0]['postAddr'].split('(')[0]
resultDf3

# In[140]:


for i in range(0, len(resultDf3)):
    resultDf3.loc[i]['postAddr'] = resultDf3.loc[i]['postAddr'].split('(')[0].rstrip()
    resultDf3.loc[i]['postAddr'] = resultDf3.loc[i]['postAddr'].split(',')[0].rstrip()
resultDf3

# In[136]:


# 내가 짠 코드


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
