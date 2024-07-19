# for 문의 기본 구조
"""
for 변수 in 리스트(또는 튜플, 문자열)
    수행할_문장1
    수행할_문장2
"""

# 1. 전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

# 2. 다양한 for 문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
    print(first + last)

# 3. for 문의 응용
# marks1.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number + 1
    if mark >= 60 :
        print("%d번 학생은 합격" % number)
    else :
        print("%d번 학생은 불합격" % number)

marks.reverse()
num = 1
for mark in marks :
    print("%d등의 점수는 %d 입니다." % (num, mark))
    num += 1

# for 문과 continue 문
# marks2.py
marks = [90,25,67,45,80]

number = 0
for mark in marks :
    number = number + 1
    if mark < 60 :
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for 문과 함께 자주 사용하는 range 함수
a = range(10)
a # range(0,10)

a = range(1,11)
a # range(1,11)

# range 함수의 예시
add = 0
for i in range(1,11) :
    add = add + i
    
print(add) # 55

# marks3. py
marks = [90,25,67,45,80]
for number in range(len(marks)) :
    if marks[number] < 60 :
        continue
    print("%d번 학생 축하, 합격" % (number + 1))


# for와 range를 이용한 구구단
for i in range(2,10) :
    for j in range(1,10) :
        print(i * j, end=" ")
    print("")

# 리스트 컴프리헨션 사용하기
a = [1,2,3,4]
result = []
for num in a :
    result.append(num * 3)

print(result)

# 짝수에만 3을 곱하고 싶을 때
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
# 리스트 컴프리헨션의 문법은 다음과 같다. 'if 조건문' 부분은 앞의
# 예제에서 볼 수 있듯이 생략할 수 있다.

# [표현식 for 항목 in 반복_가능_객체 if 조건문]

# for 문을 2개이상 사용하는 것도 가능. for 문을 여러개 사용할 때의 문법은 다음과 같다.
# [표현식 for 항목1 in 반복_가능_객체1 if 조건문1
#  표현식 for 항목2 in 반복_가능_객체2 if 조건문2
#  ...
# 표현식 for 항목n in 반복_가능_객체n if 조건문n]

result = [x * y for x in range(2,10)
                for y in range(1,10)]

print(result)