# 1. 큰따옴표로 양쪽 둘러싸기
"Hello World"

# 2. 작은따옴표로 양쪽 둘러싸기
'python is fun'

# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need python"""

# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need python'''

# food = "Python's favorite food is perl"
# food

# food = 'python's favorite food is perl'
# food

say = '"python is very easy." he says.'

# 3. 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
food = 'python\' favorite food is perl'
say = "\"Python is very easy.\" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
## 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

## 2. 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline = '''
    Life is too shor
    You need python
    '''
print(multiline)
# 연속된 작은따옴표, 큰따옴표는 결과는 동일

# 문자열 연산하기
# 문자열 더해서 연결하기
head = "python"
tail = " is fun!"
head + tail

# 문자열 곱하기
a = "python"
a * 2 #pythonpython





