# 사용자 입출력 =====

a = input()
a
# input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.

# 프롬프트를 띄워 사용자 입력받기 =====
input("안내_문구")

number = input("숫자를 입력하세요 : ")
print(number)

# print 자세히 알기 =====
a = 123
print(a)

a = "python"
print(a)

a = [1,2,3]
print(a)

# 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short") # lifeistoo short
print("life" + "is" + "too short") # lifeistoo short
# 위아래의 값이 같음

# 문자열 띄어쓰기는 쉼표로 한다.
print("life", "is", "too short") # life is too short 

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')


