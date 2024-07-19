# money = True
money = False

if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
    
# =====================
# indent_error.py
# money = True
# if money :
#     print("택시를")
# print("타고") # indent error 위치를 맞추어야 한다.
#     print("가라")

money = 2000
card = True
if money > 3000 or card :
    print("택시")
else :
    print("걷기")


# in, not in
1 in [1,2,3] # 1이 안에 있으므로 True
1 not in [1,2,3] # 1이 안에 있으므로 not 때문에 False

'a' in ('a','b','c') # True
'j' not in 'python' # True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print('택시')
else :
    print('걷기')

# 조건문에서 아무 일도 하지 않게 설정하고 싶으면
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket :
    pass # 
else :
    print('카드 사용')

# 다양한 조건을 판단하는 elif

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print('택시')
else :
    if card :
        print("택시")
    else :
        print("걷다")

# elif 사용
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print('택시')
elif card :
    print('택시')
else :
    print('걷다')

""" 
if 조건문 :
    수행할 문장 1
    수행할 문장 2
elif 조건문 :
    수행할 문장 1
    수행할 문장 2
elif 조건문 :
    수행할 문장 1
    수행할 문장 2
else :
    수행할 문장 1
    수행할 문장 2
"""

# if 문을 간략히
if 'money' in pocket :
    pass
else :
    print("카드")

# 간략히
if 'money' in pocket : pass
else : print("카드")

# 조건부 표현식
score = 50
if score >= 60 :
    message = "success"
else :
    message = "failure"
message

# 파이썬의 조건부 표현식
message = "success" if score >= 60 else "failure"
# 변수 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
