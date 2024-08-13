# mod1.py
# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

"""
import의 사용법
import 모듈_이름

mod1.add, mod1.sub 처럼 쓰지 않고, add, sub처럼 모듈 이름없이 함수 이름만 쓰고 싶은 경우
from 모듈_이름 import 모듈_함수
위와 같이 하면 모듈이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다.

# add 함수 하나만 사용하는 방법
from dmo1 import add 
add(3,4)
7

# add, sub 함수 사용하는 방법
# 1. 쉼표로 구분
from mod1 import add, sub

# 2. * 문자 사용(mod1의 모든함수를 불러와 사용)
from mod1 import *
"""

# # if __name__=="__main__":의 의미
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
# print(add(1,4))
# print(add(4,2))
"""
위와 같이 사용하는 경우 print도 실행이 되므로 add와 sub 함수만 사용하려는 경우
다음과 같이 수정
"""
if __name__=="__main__":
    print(add(1,4))
    print(sub(4,2))

"""
__name__ 변수란
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름
만약 c:\doit\~ mod1.py 처럼 파일을 직접 실행할 경우, mod1.py의 __name__ 변수에는
__main__ 값이 저장된다. 하지만 파이썬 셀이나 다른 파이썬 모듈에서 mod1을 import 할
경우에는 mod1.py의 __name__ 변수에 mod1.py의 모듈 이름인 mod1이 저장된다.

>>> import mod1
>>> mod1.__name__
'mod1'
"""
