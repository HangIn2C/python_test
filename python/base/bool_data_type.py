# 불 자료형 =====
# bool 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
# bool 자료형은 다음 2가지 값만을 가질 수 있다.
# True : 참
# False : 거짓

a = True
b = False

type(a) # <class 'bool'>
type(b) # <class 'bool'>
# type(x)는 x의 자료형을 확인하는 파이썬의 내장 함수

1 == 1 # True
2 > 1 # True
2 < 1 # False

# 자료형의 참과 거짓 =====
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면("", [], (), {})
# 거짓이 되고 비어 있지 않으면 참이 된다. 숫자에서는 그 값이 0일 때 거짓이 된다.
# None은 거짓

a = [1,2,3,4]
while a:
    print(a.pop()) #pop은 리스트에서 마지막 값을 꺼내고 삭제함
# 4
# 3
# 2
# 1
# 위의 예는 a가 참인 경우, a.pop()를 계속 실행하여 출력하라는 의미

if [1,2,3]:
    print("참")
else:
    print("거짓")
# 참
# 만약 [1,2,3]이 참이면 "참"이라는 문자열을 출력하고, 그렇지 않으면 "거짓"이라는
# 문자열을 출력하라
# [1,2,3]은 요솟값이 있는 리스트이므로 참이다. 따라서 "참"을 출력한다.

# 불 연산

bool('python') # True

bool('') # False

bool([1,2,3]) # True
bool([]) # False
bool(0) # False
bool(3) # True
bool(None) # False





