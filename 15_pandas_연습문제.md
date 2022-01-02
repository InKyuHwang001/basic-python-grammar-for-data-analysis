## 연습문제

---

```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import csv
import matplotlib.pyplot as plt
from datetime import datetime
```

---

```python
df1=pd.read_csv("../data/cancer_test.csv")
df1.columns
df1.dtypes
df1.head()
df1.info()
df1.describe()
```

---

### 1.radius_mean, texture_mean, texture_se, smoothness_se

``` python
# NA인 행을 제거한 후 총 행의 수 리턴
df1['radius_mean'].isnull().sum()       #NA--->4
df1['texture_mean'].isnull().sum()       #NA--->4
df1['texture_se'].isnull().sum()       #NA--->4
df1['smoothness_se'].isnull().sum()       #NA--->4

vbool=df1['radius_mean'].isnull().sum() & df1['texture_mean'].isnull().sum() & df1['texture_se'].isnull().sum() & df1['smoothness_se'].isnull().sum() 
vbool.sum()

df1.loc[vbool,:] #컬럼 4개가 모두 NA인 행 확인
df1.shape #(569,32)
df1.shape[0]
df1.shape[1]

df1.shape[0]-vbool.sum() #565--> not null행 수

#
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all')
nrow=df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'],how='all').shape[0]
```

---

### 2. concavity_mean 의 standard scaling(표준화) 후, 결과가 0.1 이상인 값의 개수 출력해줘

---

```python
# standard scaling(표준화) = (원 데이터 - 평균) / 표준편차
#minmax scailling=(원 데이터 -최소)/(최대-최소)
df1.columns
(df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean'].std()
vsc=(df1['concavity_mean']-df1['concavity_mean'].mean())/df1['concavity_mean'].std()
(vsc>0.1).sum()

#이상치 건 수 확인
```

---

### 3.texture_se의 상위 10%값(NA제외)을 이상치로 가정한다.

---

```python
# 10%를 제외한 값을 최대값으로 수정한 하고 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건수 확인
df1['texture_se'].dropna()
df1['texture_se'].dropna().shape[0]
nx=int(np.trunc(df1['texture_se'].dropna().sshape[0]*0.1))
#이상치를 제외한 나머지>>평균
df1['texture_se'].rank(ascending=False,method='first')
vrank=df1['texture_se'].rank(ascending=False,method='first')

# 참고----- 
_df = pd.DataFrame(
    {'name': ['KIM', 'LEE', 'SMITH','BROWN', 'MILLER'],
     'age': [24, 32, 43, 24, np.nan]})

'''
     name   age
0     KIM  24.0
1     LEE  32.0
2   SMITH  43.0
3   BROWN  24.0
4  MILLER   NaN

'''
# 동점자 처리 기준5개
_df['rank_average'] = _df['age'].rank(method='average') #평균값
_df['rank_min'] = _df['age'].rank(method='min')
_df['rank_max'] = _df['age'].rank(method='max')
_df['rank_first'] =_df['age'].rank(method='first')
_df['rank_dense'] = _df['age'].rank(method='dense')
#dense 는 min과 유사, 그룹간 순위 1씩증가
#---------------
vrank=df1['texture_se'].rank(ascending=False,method='first')
vrank

df1.loc[vrank>nx,'texture_se'] #정상치 데이터
vmax=df1.loc[vrank>nx,'texture_se'].max()#정상치 데이터 최대값
df1.loc[vrank<=nx,'texture_se'] #이상치 데이터
df1['texture_se'].sort_values(ascending=False)[:nx]

#이상치 데이터를 vmax 치환
df1.loc[vrank<=nx,'texture_se']=vmax
round(df1['texture_se'].mean(),2)
```

---

### 4. symmetry_mean의 결측치를 최솟값으로 수정한 후 평균을 소수점 둘째라리로 반올림 하여 출력

---

```python
df1['symmetry_mean'].mean() # '-'어라 문자값이 있네

from numpy import nan as NA
df1['symmetry_mean'].replace('-',NA)
df1['symmetry_mean']=df1['symmetry_mean'].replace('-',NA)
df1['symmetry_mean']=df1['symmetry_mean'].replace('.',NA)
df1['symmetry_mean']=df1['symmetry_mean'].replace('pass',NA)
df1['symmetry_mean']=df1['symmetry_mean'].replace('<=',NA)
df1['symmetry_mean']=df1['symmetry_mean'].astype('float')

#최솟값 확인
vmin=df1['symmetry_mean'].min()
#결측치 수정
vmin=df1['symmetry_mean'].fillna(vmin)
vmin=df1['symmetry_mean']=vmin=df1['symmetry_mean'].fillna(vmin)

#평균 확인
print(round(df1['symmetry_mean'].mean(),2))  # 0.18
```



