# 딕셔너리 자료형 =====

""" 
딕셔너리란
딕셔너리는 단어 그대로 '사전'이라는 뜻, 즉 "people"이라는 단어에
"사람", "baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 딕셔너리는
Key와 Value를 한 쌍으로 가지는 자료형이다. 예컨대 Key가 "baseball" 이라면
Value는 "야구"가 될것이다.

딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지
않고 Key를 통해 Value를 얻는다. 이것이 바로 딕셔너리의 가장 큰 특징이다.
baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는
것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.
"""

# 딕셔너리는 어떻게 만들까
# 다음은 딕셔너리의 기본 모습이다.
# {key1:value1, key2:value2, key3:value3, ...}

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1111'}
dic

a = {1: 'hi'}
a = {'a': [1,2,3]}

# 딕셔너리 쌍 추가, 삭제하기 =====

# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a # {1: 'a', 2: 'b'}

a['name'] = 'pey'
a # {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
a # {1: 'a', 2: 'b', 'name': 'pey', 3: [1,2,3]}

# 딕셔너리 요소 삭제하기
del a[1]
a

# 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey' : 10, 'julliet' : 99}
grade['pey'] # 10
grade['julliet'] # 99

a = {1:'a', 2:'b'}
a[1] # a
a[2] # b

a = {'a':1, 'b':2}
a['a'] # 1
a['b'] # 2

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
dic['name'] # pey
dic['phone'] # 010-9999-1234
dic['birth'] # 1118

# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 
# 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다.
# 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우, 1:'a'쌍이 무시된다.

a = {1:'a', 1:'b'}
a # {1:'b'}

a = {[1,2] : 'hi'} # 에러
# Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다.
# 딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지,
# 변하지 않는(immutable) 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기
# 때문에 Key로 쓸 수 없다. 다음 예처럼 리스트를 Key로 설정하면 리스트를
# 키 값으로 사용할 수 없다는 오류가 발생한다.

# 딕셔너리 관련 함수 =====
# Key 리스트 만들기 - Keys
a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1110'}
a.keys() # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)
# name
# phone
# birth

for k in a.values():
    print(k)

list(a.keys()) # ['name', 'phone', 'birth']

# Value 리스트 만들기 - values
a.values() # dict_values(['pey', '010-9999-1234', '1110'])

# Key, Value 쌍 얻기 - items
a.items() # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1110')])

# Key : Value 쌍 모두 지우기 - clear
a.clear()
a

# Key로 Value 얻기 - get
a = {'name':'pey','phone':'010-9999-1234','birth':'1118'}
a.get('name') # 'pey'
a.get('phone') # '010-9999-1234'

a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a.get('nokey')) # None

print(a['nokey']) # 오류

# 딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게
# 하고 싶을 때는 get(x, '디폴트 값')

a.get('nokey', 'foo') # foo

# 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name':'pey','phone':'010-9999-1234','birth':'1118'}
'name' in a # True
'email' in a # False

