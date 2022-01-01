## 판다스 문자열 메소드

---

### 기본 메서드:벡터 연산 불가능(매 원소마다 반복 불가)

---

``` python
'abc'.upper()
'a/b/c'.split('/')

l1=['abc','def']
l2=['a/b/c','d/e/f']

l1.upper()  #불가
l2.upper()  #불가

list(map(lambda x: x.upper(),l1))
list(map(lambda x: x.split('/'),l2)
```

---

### pandas 메서드

---

- 벡터화 내장(매 원소마다 반복 가능)
- Series DataFrame 적용가능

---

```python
from pandas import Series, DataFrame

# 1)split
Series(l1)
# 0    abc
# 1    def
# dtype: object

s1=Series(l1)
s2=Series(l2)

s2
# 0    a/b/c
# 1    d/e/f
# dtype: object

s2.split('/')  #불가
s2.str.split('/') #가능
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

#대소치환
s1.str.upper()     #대문자
s1.str.lower()     #소문자
s1.str.title()
# 0    Abc
# 1    Def
# dtype: object

#replace(치환)
s1.str.replace('a','A') #문자열 치환
s1.str.replace('a','')  #문자열 삭제
# 0     bc
# 1    def
# dtype: object
```

```python
#[예제] 천단위 구분기호 처리
s3=Series(['1,200','3,000','4,000'])
# 0    1,200
# 1    3,000
# 2    4,000
# dtype: object
s3.str.replace(',','').astype(int).sum()
```

```python
#패턴 확인: startswith, endswith, contains

s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')] #s1 각 원소에서 a로 시작하는 원소 추출
s1[s1.str.endswith('c')]   #s1 각 원소에서 c로 끝나는 원소 추출
s1[s1.str.contains('c')]   #s1 각 원소에서 c를 포함하는 원소 추출

#문자열 크기 len()
s1.str.len()      #각 원소의 크기
#count
Series(['aabca','abcsa']).str.count('a')
#문자열 제거
Series(['     cd     ','          df ']).str.strip()
Series(['     cd     ','          df ']).str.strip().str.len()

s1.str.strip('a') #문자열 제거
Series(['aasdadsaasd','abaaaaabaaaas']).str.strip('a')       #문자열 제거(중간값 삭제 불가)
Series(['aasdadsaasd','abaaaaabaaaas']).str.replace('a','')  #all a 제거

#find: 위치값 리턴
s3=Series(['abc@nave.com','nadaink@naver.com'])
s3.str.find('@')

#문자열 색인(추출)
'abcdef'[0:3]
s3[0:1]
# 0    abc@nave.com
# dtype: object
s3.str[0:3] #Series 에서 각 원소마다 1~3번까지의 문자열 추출
# 0    abc
# 1    nad
# dtype: object
```

```python
#[예제]: 이메일 아이디 추출
s3=Series(['abc@nave.com','nadaink@naver.com'])

list(s3.map(lambda x: x[:x.find('@')]))
list(map(lambda x,y: x[0:y],s3,s3.str.find('@')))
```

```python
#문자열 삽입 pad

s1.str.pad(5,            #문자열수
           'left',       #위치
           '!')          #삽입 문자
# 0    !!abc
# 1    !!def
# dtype: object

#문자열 결합 cat
'a'+'b'
'a'*3

s4=Series(['abc','def','123'])
s4.str.cat()        #Series 내 서로 다른 원소 결합
s4.str.cat(sep='/') #Series 내 서로 다른 원소 /로 구분 결합

s5=Series([['a','b','c'],['d','e','f']])
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object
s5.str.join(sep='') #Series 내 각 원소 내부의 문자열 결합
# 0    abc
# 1    def
# dtype: object
s5.str.join(sep='\'')
# 0    a'b'c
# 1    d'e'f
# dtype: object
```

