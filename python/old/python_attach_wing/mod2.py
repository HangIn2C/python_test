# mod2.py
# # 클래스나 변수 등을 포함한 모듈
PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r**2)
    
def add(a,b):
    return a + b

"""
# mod2.py에 있는 Math 클래스를 사용하는 방법
>>> import mod2
>>> print(mod2.PI)

# mod2.py의 add 함수 사용하는 방법
>>> print(mod2.add(mod2.PI, 4.4))
"""

