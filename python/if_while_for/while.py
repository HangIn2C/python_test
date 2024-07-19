# while 문의 기본 구조
""" 
while 조건문 :
    수행할_문장1
    수행할_문장2
    수행할_문장3
"""
# while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행된다.

treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10 :
        print("나무 넘어갑니다.")

# =========================================

prompt = """ 
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0
while number != 4 :
    print(prompt)
    number = int(input())

# =============================================
# coffee.py
coffee = 10
money = 300
while money :
    print("커피")
    coffee = coffee - 1
    print("남은 커피의 양 %d개" % coffee)
    if coffee == 0 :
        print("커피 없음")
        break

# =================================================

# coffee.py
coffee = 10
while True :
    money = int(input("돈 넣기"))
    if money == 300 :
        print("커피")
        coffee -= 1
        print("커피 남은 양 : %d" % coffee)
    elif money > 300 :
        print("거스름돈 %d를 주고 커피 준다" % (money - 300))
        coffee -= 1
        print("커피 남은 양 : %d" % coffee)
    else :
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# =====================================================
# while 문의 맨 처음으로 돌아가기
a = 0
while a < 10 :
    a = a + 1
    if a % 2 ==0 : continue
    print(a)

# 무한 루프 / 빠져나가는 법 ctrl + c
a = 0
while True :
    a += 1
    print(a)

