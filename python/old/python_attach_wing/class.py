# 클래스
"""
클래스는 왜 필요한가?
프로그래머들이 가장 많이 사용하는 프로그래밍 언어 중 하나인 C 언어에는 클래스가 없다.
일 말은 굳이 클래스가 없어도 프로그램을 충분히 만들 수 있다는 뜻이다. 파이썬으로 잘 만든
프로그램을 살펴봐도 클래스를 사용하지 않고 작성한 것이 매우 많다. 즉, 클래스는 지금까지
공부한 함수나 자료형처럼 프로그램 작성을 위해 꼭 필요한 요소는 아니다.


"""

# 계산기 프로그램을 만들며 클래스 알아보기
# calculator.py
result = 0

def add(num):
    global result
    result += num # 결괏값(result)에 입력값(num) 더하기
    return result # 결괏값 리턴

print(add(3))
print(add(4))

"""
그런데 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까?
각 계산기는 각각의 결괏값을 유지해야 하므로 위와 같이 add 함수 하나만으로는 결괏값을 따로 유지할 수 있다.

이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야 한다.
"""

# calculator2.py
result1 = 0
result2 = 0

def add1(num) : # 계산기1
    global result1
    result1 += num
    return result1

def add2(num) : # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3)) # 3
print(add1(4)) # 7
print(add2(3)) # 3
print(add2(7)) # 10

"""
계산기 1의 결괏값이 계산기 2에 아무런 영향을 끼치지 않는다는 것을 확인할 수 있다.
하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까?
그때마다 전역 변수와 함수를 추가할 것인가? 여기에 계산기마다 빼기나 곱하기와 같은
기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.

아직 클래스에 대해 배우지 않았지만, 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.
"""

# calculator3.py
class Calculator :
    def __init__(self) :
        self.result = 0

    def add(self, num) :
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10

"""
Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 '객체'라고 부른다)가
각각의 역할을 수행한다. 그리고 계산기의 결괏값과 상관없이 독립적인 값을 유지한다. 이렇게
클래스를 사용하면 계산기 대수가 늘어나도 객체를 생성하면 되므로 함수만 사용할 때보다 간단하게 프로그램을
작성할 수 있다. 빼기 기능을 더하고 싶다면 Calculator 클래스에 다음과 같이 빼기 기능을 가진 함수를 추가 하면 된다.
"""

class Calculator :
    def __init__(self) :
        self.result = 0

    def add(self, num) :
        self.result += num
        return self.result
    
    # 빼기 기능 추가
    def sub(self, num) :
        self.result -= num
        return self.result
    
# 클래스와 객체
"""
과자 틀 = 클래스
과자 틀로 찍어 낸 과자 = 객체

여기에서 설명할 클래스는 과자 틀과 비슷하다. 클래스(class)란 똑같은 무언가를 계속
만들어 낼 수 있는 설계 도면(과자 틀), 객체(object)란 클래스로 만든 피조물(과자 틀로 찍어 낸 과자)을 뜻한다.

클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다. 과자 틀로 만든 과자에
구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무런 영향이 없는 것과 마찬가지로 동일한 클래스로
만든 객체들은 서로 전혀 영향을 주지 않는다.

다음은 파이썬 클래스의 가장 간단한 예이다.
"""

class Cookie :
    pass

"""
위에서 작성한 Cookie 클래스는 아무런 기능도 가지고 있지 않은 껍질뿐인 클래스이다.
하지만 이렇게 껍질뿐인 클래스도 객체를 생성하는 기능이 있다. '과자 틀'로 '과자'를 만드는 것처럼 말이다.

객체는 클래스로 만들고 1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다. 위에서 만든 Cookie
클래스의 객체를 만드는 방법은 다음과 같다.
"""
a = Cookie()
b = Cookie()

"""
Cookie()의 결괏값을 리턴받은 a와 b가 바로 객체이다. 마치 함수를 사용해서 그 결괏값을 리턴받는 모습과 비슷하다.

객체와 인스턴스의 차이
클래스로 만든 객체를 '인스턴스'라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자
a = Cookie()로 만든 a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다. 즉, 인스턴스라는 말은
특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
'a는 인스턴스'보다 'a는 객체'라는 표현이 어울리며 'a는 Cookie의 객체' 보다
'a는 Cookie의 인스턴스'라는 표현이 훨씬 잘 어울린다.
"""

"""
사칙 연산 클래스 만들기

 - 클래스를 어떻게 만들지 구상하기
    클래스는 무작정 만드는 것보다 클래스로 만든 객체를 중심으로 어떤 식으로 동작하게 할지
    미리 구상한 후 생각한 것을 하나씩 만들면서 완성해 나가는 것이 좋다.

사칙 연산 기능을 가진 FourCal 클래스가 다음처럼 동작한다고 가정해 보자
먼저 a = FourCal()를 입력해서 a라는 객체를 만든다.
"""

class FourCal :
    # 생성자 추가
    def __init__(self, first, second) :
        self.first = first
        self.second = second
              # a.setdata(4,2)
    def setdata(self, first, second) :
        self.first = first
        self.second = second
        
    def add(self) :
        result = self.first + self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def mul(self) :
        result = self.first * self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result
# 파이썬 매서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
# 객체를 호출할 때 호춣ㄴ 객체 자신이 전달되기 때문에 self라는 이름을 사용한 것이다. 다른 이름을 사용해도 상관없다.

a = FourCal()
b = FourCal()
type(a) # <class '__main__.FourCal'>

a.setdata(4,2)
a.first

b.setdata(3,7)
b.first
b.second

a.add()
a.mul()
a.sub()
a.div()


# 생성자
# 이번에는 우리가 만든 FourCal 클래스를 다음과 같이 사용해 보자
a = FourCal()
a.add()
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in add
TypeError: 'FourCal' object is not subscriptable """

"""
FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 먼저 수행하면
'AttributeError: 'FourCal' ~ 오류가 발생한다. setdata 메서드를 수행해야 객체 a의 객체변수
first와 second가 생성되기 때문이다. 이렇게 객체에 first, second와 같은 초깃값을 설정해야
할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다 생성자를 구현하는 것이
안전한 방법이다.

생성자(constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 파이썬 메서드명으로
__init__를 사용하면 이 메서드는 생성자가 된다.

다음과 같이 FourCal 클래스에 생성자를 추가해 보자

 # __init__ 메서드의 init 앞뒤로 붙은 __는 밑줄(_) 2개를 붙여 쓴것이다.

__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단, 메서드 이름을 __init__로 했기
때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이가 있다.
"""

a = FourCal()
""" Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'first' and 'second' """

a = FourCal(4,2)
"""
위와 같이 수행하면 __init__ 메서드의 매개변수에는 각각 다음과 같은 값이 전달된다.
매개변수 | 값
self    | 생성되는 객체
first   | 4
second  | 2
"""

a.first
a.second

a.add()

"""
클래스의 상속
상속(Inheritance)이란 '물려받다'라는 뜻이로, '재산을 상속받다'라고 할 때의 상속과 같은
의미이다. 클래스에도 이 개념을 적용할 수 있다. 어떤 클래스를 만들 때 다른 클래스의 기능을
물려받을 수 있게 만드는 것이다. 이번에는 상속 개념을 사용하여 우리가 만든 FourCal 클래스에
a^b 값을 구할 수 있는 기능을 추가해 보자

앞에서 FourCal 클래스는 이미 만들어 놓았으므로 FourCal 클래스를 상속하는 MoreFourCal 클래스는
다음과 같이 간단하게 만들 수 있다.
"""
class MoreFourCal(FourCal) :
    pass

# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# class 클래스_이름(상속할_클래스_이름)
# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있다.

a = MoreFourCal(4,2)
a.add()
a.sub()
a.mul()
a.div()

"""
상속받은 FourCal 클래스의 기능을 모두 사용할 수 있다는 것을 확인할 수 있다.

상속 기능은 왜 쓸까?
보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
'클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야하지?'
라는 의문이 들 수도 있다. 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는
상황이라면 상속을 사용해야 한다.

이제 원래 목적인 a^b을 계산하는 MoreFourCal 클래스를 만들어 보자
"""

class MoreFourCal(FourCal) :
    def pow(self):
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
a.pow()

# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 그대로 놔둔 채 클래스의 기능을 확장할 때 주로 사용한다.

# =====================================
# 메서드 오버라이딩
# =====================================
a = FourCal(4,0)
a.div()
# FourCal 클래스의 객체 a에 값 4와 0을 지정하고 div 메서드를 호출하면 4를 0으로 나누려고 하므로
# ZeroDivisionError 오류가 발생한다. 0으로 나눌때 오류가 아닌 값 0을 리턴받고 싶다면 어떻게 해야 할까

#다음과 같이 FourCal 클래스를 상속하는 SafeFourCal 클래스를 만들어 보자
class SafeFourCal(FourCal) :
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second
    
""" 
FourCal 클래스에 있는 div 메서드를 동잃ㄴ 이름으로 다시 작성했다. 이렇게 부모 클래스(상속한 클래스)에 있는
메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(method overriding)이라고 한다. 이렇게 메서드를
오버라이딩 하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 리턴하도록 수정했다.
이제 다시 앞에서 수행한 예제를 FourCal 클래스 대신 SafeFourCal 클래스를 사용하여 수행해 보자.
"""
a = SafeFourCal(100,0)
a.div()

"""
FourCal 클래스와 달리 ZeroDivisionError가 발생하지 않고 의도한 대로 0이 리턴되는 것을 확인할수 있다.
"""

# =====================================================
# 클래스 변수
# =====================================================
"""
객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지한다는 점을 이미 알아보았다.
이번에는 객체변수와는 성격이 다른 클래스 변수에 대해 알아본다.
"""
class Family:
    lastname = "김"

Family.lastname

"""
클래스변수는 위 예와 같이 '클래스_이름.클래스변수'로 사용할 수 있다.
또는 다음과 같이 Family 클래스로 만든 객체를 이용해도 클래스 변수를 사용할 수 있다.
"""

a = Family()
b = Family()
a.lastname
b.lastname

""" 김 -> 박 """
Family.lastname = "박"
a.lastname
b.lastname
