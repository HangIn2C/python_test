# 자료형의 값을 저장하는 공간, 변수

a = 1
b = "python"
c = [1,2,3]

# 변수_이름 = 변수에_저장할_값

# 변수란
a = [1,2,3]

# 변수가 가리키는 메모리의 주소 확인 법
a = [1,2,3]
id(a) # 2692068138944

# 리스트를 복사하고자 할 때
a = [1,2,3]
b = a
c = [1,2,3]
id(a) # 2692068141696
id(b) # 2692068141696
# 둘의 주솟값이 동일
id(c) # 2692068138944 # 주솟값이 다름

a is b # True 동일한 값
a is c # False 주솟값이 다르므로 False

a[1] = 4
a # [1,4,3]
b # [1,4,3]

# 1. [:]이용하기
a = [1,2,3]
b = a[:]
a[1] = 4
a # [1,4,3]
b # [1,2,3]

# 2. copy 모듈 이용하기
from copy import copy
a = [1,2,3]
b = copy(a)

b is a # False
# b is a가 False를 리턴하므로 b와 a가 가리키는 객체는 서로 다르다는 것을 알 수 있다.

# 변수를 만드는 여러 가지 방법 =====
a, b = ('python', 'life')
# 위, 아래는 서로 비슷
(a, b) = 'python', 'life'

[a,b] = ['python', 'life']

a = b = 'python'

a = 3
b = 5
a,b = b,a
a # 5
b # 3
