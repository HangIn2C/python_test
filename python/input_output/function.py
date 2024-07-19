# 함수를 사용하는 이유
# 반복되는 부분이 있을 경우, '반복적으로 사용되는 가치 있는 부분'을
# 한 뭉치로 묶어 '어떤 입력값을 주어을 때 어떤 결괏값을 리턴해 준다.'
# 라는 식의 함수로 작성하는 것이다.

# 자신이 작성한 프로그램을 기능 단위의 함수로 분리해 놓으면 프로그램 흐름을
# 일목요연하게 볼 수 있기 때문

# 파이썬 함수의 구조
""" 
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2
    ...
"""
# def는 함수를 만들 때 사용하는 예약어

def add(a,b) :
    return a + b

a = 3
b = 4
c = add(a,b)
print(c) # 7

# 매개변수와 인수 =====
# 매개변수(parameter)와 인수(arguments)는 혼용해서 사용하는 용어
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수
# 인수는 함수를 호출할 때 전달하는 입력값을 의미

# 일반적인 함수 =====
# 입력값이 있고 리턴값이 있는 함수가 일반적인 함수이다.

""" 
def 함수_이름(매개변수) :
    수행할_문장
    ...
    return 리턴값
"""

def add(a,b) :
    result = a + b
    return result

a = add(3,4)
print(a)

# 리턴값을_받을_변수 = 함수_이름(입력_인수1, 입력_인수2, ...)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 리턴값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))

add(3,4)

# 입력값도 리턴값도 없는 함수
def say():
    print("Hi")

say()

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

result = sub(a = 7, b = 3)
print(result)

result = sub(b = 5, a = 3)
print(result)

# 입력값이 몇 개가 될지 모를 때
""" 
def 함수_이름(*매개변수)
    수행할_문장
    ...
"""
# 매개변수 부분이 *매개변수 로 바뀌었다.

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# =================================================================

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

# ==================================================================
# 키워드 매개변수, kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1) # {'a':1}
print_kwargs(name='foo', age = 3) # {'name':'foo', 'age':3}
# **kwargs 처럼 매개변수 이름 앞에 ** 을 붙이면 매개변수 kwargs는 딕셔너리가 되고
# 모든 key=value 형태의 입력값이 그 딕셔너리에 저장된다는 것을 알 수 있다.
# - kwargs는 'keyword arguments'의 약자이며 args와 마찬가지로 관례적으로 사용한다.

# 함수의 리턴값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4) # (7, 12) 튜플 값으로 표현됨
result1, result2 = add_and_mul(4,5)
print(result)
print(result1, result2) # 9, 20 각자의 값으로 표현됨 
# return을 여러개써도 처음 return 으로 함수를 빠져나간다. return은 하나만 쓴다.

# return 의 또 다른 쓰임새
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져
# 나갈수 있다.

def say_nick(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s입니다.' % nick)

say_nick('야호')
say_nick('바보')
# 리턴값이 없는 함수에서 return으로 함수를 빠져나가는 방법은 실제 프로그래밍에서 자주 사용됨

# 매개변수에 초깃값 미리 설정하기
# default1.py
def say_myself(name, age, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살입니다.' % age)
    if man :
        print('남자')
    else :
        print('여자')

say_myself('박응용', 27) # 초기에 저장된 man = True로 동작됨
say_myself('박응선', 32, False)

# default2.py
""" def say_myself(name, man=True, age):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살입니다.' % age)
    if man :
        print('남자')
    else :
        print('여자')
say_myself('박응용', 27) """
# 에러 발생, 매개 변수의 위치가 맞지 않아 에러가 발생

# ===================================================================
# 함수 안에서 선언한 변수의 효력 범위

# vartest.py
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# ======================================================================
# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)  
print(a) # a 라는 변수를 생성하지 않았기에 오류가 생김

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
# vartest_return.py
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기
# vartest_global.py
a = 1
def vartest():
    global a # 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
    a = a + 1
# 프로그래밍을 할때 global 명령어는 사용하지 않는 것이 좋다.
# 함수는 독립적으로 존재하는 것이 좋기 때문, 외부 변수에 종속적인 함수는
# 그다지 좋은 함수가 아니다. 따라서 위의 return 방법을 사용하기 권장한다.

vartest()
print(a)

# lambda 예약어
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다.

# 사용법
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식

add = lambda a, b: a + b
result = add(3,4)
print(result)




