## drop, shift, rename

---

```python
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
```

---

### drop

---

특정 행 컬럼 제거
이름 전달

---

```python
emp=pd.read_csv('C:/Users/nadai/code/data_bigdata_cert/emp.csv')
'''
   empno  ename  deptno   sal
0      1  smith      10  4000
1      2  allen      10  4500
2      3   ford      20  4300
3      4  grace      10  4200
4      5  scott      30  4100
5      6   king      20  4000
'''
```

- scott 퇴사

```python
emp.loc[emp['ename']=='scott'] #스캇 관련 기록
emp['ename']=='scott' #조건문
emp.loc[emp['ename']=='scott',:]
emp.loc[~(emp['ename']=='scott'),:]

emp.drop(4, axis=0) #행기준,4번째 idx 제외
```

예제: `emp 데이터 셋에서 sal 컬럼 제외(iloc)`

```python
emp.iloc[:,0:3]
emp.iloc[:,:-1]
emp.drop('sal', axis=1)
emp.loc[:,"empno":"deptno"]
emp.drop(['ename','deptno'],axis=1)
```

---

### shift

---

행 또는 열을 이동

전일자 대비 증감율

---

```python
emp['sal']
''' 
0    4000
1    4500
2    4300
3    4200
4    4100
5    4000
Name: sal, dtype: int64
'''
emp['sal'].shift()
'''
0       NaN
1    4000.0
2    4500.0
3    4300.0
4    4200.0
5    4100.0
Name: sal, dtype: float64
한칸씩 뒤로 밀린다.
'''
```

- 예제: `다음 데이터프레임에서 전일자 대비 증감율 출력`

``` python
s1=Series([3000,3500,4200,2800,3600],index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
'''
2021/01/01    3000
2021/01/02    3500
2021/01/03    4200
2021/01/04    2800
2021/01/05    3600
dtype: int64'''
#1dnjf 2일 증감율>>>(3500-3000)/3000
s1.shift()
(s1-s1.shift())/s1.shift()*100
'''
2021/01/01          NaN
2021/01/02    16.666667
2021/01/03    20.000000
2021/01/04   -33.333333
2021/01/05    28.571429
dtype: float64
'''
```

---

### rename

---

행, 열 이름 변경

---

```python
emp.columns=['emptno','ename','deptno','salary']
emp.rename({'salsry':'sal','deptno':'dept_no'},axis=1)
```

- 예제: `emp 데이터에서 ename을 index로 설정후 scott을 scoot변경`

```python
emp.set_index('ename').rename({'scott':'SCOTT'})

emp.index = emp['ename']
emp.rename({'scott':'SCOTT'}, axis = 0)
```

