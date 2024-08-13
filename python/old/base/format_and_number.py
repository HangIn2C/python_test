# 1. 정렬과 공백 =====
# %10s 는 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로
# 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미이다.
"%10s" % "hi"

# 반대쪽인 왼쪽 정렬은 %-10s
"%-10s" % "hi"

# 10개의 자리값중 hi 2글자를 빼고 8글자는 공백으로 채움

# 2. 소수점 표현하기 =====
"%0.4f" % 3.42134234
# .4f : 소수점 네 번째 자리까지만 표시 '3.4213'
"%10.4f" % 3.42134234
# %10 : 총 자릿수 10개 나머지는 공백으로표시 '    3.4213'

# format 함수를 사용한 포매팅 =====
# 문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열
# 포맷을 지정할 수 있다. 앞에서 살펴본 문자열 포매팅 예제를
# format 함수를 사용해서 바꾸면 다음과 같다.

# 숫자 바로 대입하기
"I eat {0} apples".format(3)

# 문자열 바로 대입하기
"I eat {0} apples".format("five")

# 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days".format(number,day)

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)

# ===================================================

# 왼쪽 정렬
"{0:<10}".format("hi")
# 'hi        '

# 오른쪽 정렬
"{0:>10}".format("hi")
# '        hi'

# 가운데 정렬
"{0:^10}".format("hi")
# '    hi    '

# 공백 채우기
"{0:=^10}".format("hi") # '====hi===='
"{0:!<10}".format("hi") # 'hi!!!!!!!!'
"{0:!>10}".format("hi") # '!!!!!!!!hi'

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) # '3.4213'
"{0:10.4f}".format(y) # '    3.4213'

# { 또는 } 문자 표현하기
"{{ and }}".format() # { and }

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

# 표현식이란 중괄호 안의 변수를 계산식과 함께 사용하는 것을 말한다.
age = 30
f'나는 내년이면 {age + 1}살이 된다.'

# 딕셔너리는 key와 value라는 것을 한 쌍으로 가지는 자료형이다.

# 정렬은 다음과 같이 할 수 있다.
f'{"hi": <10}' # 왼쪽 정렬
f'{"hi": >10}' # 오른쪽 정렬
f'{"hi": ^10}' # 가운데 정렬

# 공백 채우기는 다음과 같이 할 수 있다.
f'{"hi":=^10}' # 가운데 정렬하고 '=' 문자로 공백 채우기
f'{"hi":!<10}' # 왼쪽 정렬하고 '!' 문자로 공백 채우기

# 소수점은 다음과 같이 표현할 수 있다.
y = 3.42134234
f'{y:0.4f}' # 소수점 4자리까지만 표현
f'{y:10.4f}' # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

# f 문자열에서 {}를 문자 그대로 표시하려면 다음과 같이 2개를 동시에 사용해야한다.
f'{{ and }}'

# 문자열 관련 함수들
# 문자 개수 세기 - count
a = "hobby"
a.count("b")

# 위치 알려 주기 1 - find
a = "python is the best choice"
a.find("b") # 14
a.find("k") # -1 # 문자를 못 찾으면 -1을 반환

# 위치 알려 주기 2 - index
a = "Life is too short"
a.index("t") # 8
a.index("k") # error # 문자를 못 찾으면 에러 발생

# 문자열 삽입 - join
",".join('abcd') # 각각의 문자 사이에 ','를 삽입
",".join(['a', 'b', 'c', 'd']) # 위와 동일

# 소문자를 대문자로 바꾸기 - upper
a = 'hi'
a.upper() # HI

# 대문자를 소문자로 바꾸기 - lower
a = "HELLO"
a.lower() # hello

# 왼쪽 공백 지우기 - lstrip
a = " hi "
a.lstrip()

# 오른쪽 공백 지우기 - rstrip
a = " hi "
a.rstrip()

# 양쪽 공백 지우기 - strip
a = " hi "
a.strip()

# 문자열 바꾸기 - replace
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기 - split
a = "Life is too short"
a.split() # ['Life', 'is', 'too', 'short']

b = "a:b:c:d"
b.split(":") # ['a', 'b', 'c', 'd']


