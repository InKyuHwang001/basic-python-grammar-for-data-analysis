## groupby

---

`python pandas groupby`

그룹연산

성별 성적평균, 학년별 성적 최고점수, 부서별 평균 연봉

---

```python
import pandas as pd
from pandas import Series, DataFrame
kimchi=pd.read_csv("C:/Users/nadai/code/data_bigdata_cert/kimchi_test.csv", encoding='cp949')
```

```
    판매년도  판매월    제품   판매처     수량       판매금액
0    2013    1  총각김치  대형마트  27916  233968900
1    2013    1  총각김치   백화점  11971   99796735
2    2013    1  총각김치   편의점   1603    2264200
3    2013    2  총각김치  대형마트  23057  194593960
4    2013    2  총각김치   백화점  11678  103106940
..    ...  ...   ...   ...    ...        ...
427  2016   11   무김치   백화점  16818  213580462
428  2016   11   무김치   편의점   1849    2718207
429  2016   12   무김치  대형마트  40806  351917006
430  2016   12   무김치   백화점  11877  139476205
431  2016   12   무김치   편의점   1890    2767080

[432 rows x 6 columns]
```

---

``` python
kimchi.groupby(by=None,       그룹핑 할 컬럼(기준)
               axis= 0,       그룹핑 연산 방향
               level = None)  멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용
```

- 예제) 제품별, 판매처별 수량 총 합

  ```python
  kimchi.groupby(by=['제품'])
  kimchi.groupby(by=['제품']).sum()
  kimchi.groupby(by=['제품','판매처'])['수량'].sum()
  kimchi.groupby(by='제품')[['수량','판매금액']].sum()
  ```

---

### 멀티인덱스

---

​	`kimchi_2=kimchi.groupby(by=['제품','판매처'])['수량'].sum()`

- 예제)제품별 판매처별 수량 총합, 평균

```python
kimchi.groupby(by=['제품','판매처'])['수량'].agg('sum','maen')
```

agg: 여러함수를 동시에 전달

- 예제) 제품별, 판매처별 수량 판매금액, 총합과, 평균

```python
kimchi.groupby(['제품','판매처'])[['수량','판매금액']].agg('sum','mean')
```

- 예제) 제품별, 판매처별 수량은 총합, 판매금액은 평균

```python
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum', '판매금액':'mean'})
```

---

### 멀티 레벨을 갖는 경우의 groupby 연산

---

```python
kimchi_2    
type(kimchi_2)
kimchi_2.groupby(level=0).sum()
kimchi_2.groupby(level='제품').sum()
kimchi_2.groupby(level=1).sum()
```

