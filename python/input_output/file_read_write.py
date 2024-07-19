# 파일 읽고 쓰기

# 파일 생성하기
# newfile.py
f = open("새파일.txt", 'w')
f.close
# 프로그램을 실행한 디렉터리에 새로운 파일이 하나 생성된 것을 확인 할 수 있다.
# 파일을 생성하기 위해 파이썬 내장 함수 open을 사용했다. open 함수는 다음과 같이
# '파일 이름'과 '파일 열기 모드'를 입력값으로 받고 결곽값으로 파일 객체를 리턴한다.

# 파일_객체 = open(파일_이름, 파일_열기_모드)
""" 
파일 열기 | 설명
모드
r           읽기 모드 : 파일을 읽기만 할 때 사용한다.
w           쓰기 모드 : 파일에 내용을 쓸 때 사용한다.
a           추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 살지고 해당
파일이 존재하지 않으면 새로운 파일이 생성된다. 위 예에서는 디렉터리에 파일이 없는 상태에서
'새파일.txt'파일을 쓰기 모드인 'w'로 열었기 때문에 '새파일.txt'라는 이름의
새로운 파일이 현재 티렉터리에 생성되었다.

만약 '새파일.txt' 파일을 c:doit 디렉터리에 생성하고 싶다면 다음과 같이 작성해야 한다.
"""
# newfile2.py
f = open("D:새파일.txt", 'w')
f.close

""" 
위 예에서 f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다. 사실 이 문장은
생략해도 된다. 프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일의 객체를 자동으로
닫아 주기 때문이다. 하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다.
쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생하기 때문이다.
"""

""" 
파일 경로와 슬래시(/)
파이썬 코드에서 팡ㄹ 경로를 표시할 때 "C:/doit/새파일.txt" 처럼 슬래시(/)를 사용할 수
있다. 만약 역슬래시를 2개 사용하거나 r"C:\doit\새파일.txt"와 같이 문자열 앞에
r문자(raw string)를 덧붙여 사용해야 한다. 왜냐하면 "C:\noto\test.txt" 처럼 파일 
경로에 \n과 같은 이스케이프 문자가 있을 경우, 줄바꿈 문자로 해석되어 의도했던 파일
경로와 달라지기 때문이다.
"""

# 파일을 쓰기 모드로 열어 내용 쓰기
# write_data.py
f = open("C:/Users/SAN-CAD5/Documents/vs/새파일.txt", 'w')
for i in range(1,30):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()
# 위 프로그램을 다음과 비교해 보면 아래는 터미널에 위는 파일에 쓰는 차이
for i in range(1,15) :
    data = "%d번째 줄입니다.\n" % i
    print(data)

# 파일을 읽는 여러 가지 방법
# readline 함수 이용하기
# readline_test.py
f = open("C:/Users/SAN-CAD5/Documents/vs/새파일.txt", 'r')
line = f.readline() #1번째 줄입니다.
print(line)
f.close()

# 모든 줄을 읽고 싶을 때
#readline_all.py
f = open("C:/Users/SAN-CAD5/Documents/vs/새파일.txt", 'r')
while True :
    line = f.readline()
    if not line : break
    print(line)
f.close()

"""
whlie True : 무한 루프 안에서 f.readline()을 사용해 파일을 계속 한 줄씩 읽어 들인다.
만약 더 이상 읽을 줄이 없으면 break를 수행한다. readline()은 더 이상 읽을 줄이 없을 경우
빈 문자열 ('')을 리턴한다.
    한 줄씩 읽어 출력할 때 줄 끝에 \n 문자가 있으므로 빈 줄도 같이 출력된다.

# 위의 예는 사용자의 입력을 받아 그 내용을 축력하는 경우이다. 파일을 읽어서 출력하는
# 예제와 비교하면 입력을 받는 방식만 다르다는 것을 알 수 있다.
# 두 번째 예는 키보드를 사용한 입력 방법, 첫 번째 예는 파일을 사용한 입력 방법이다.
"""

while True :
    data = input()
    if not data : break
    print(data)


# ===============================================================
# readlines 함수 사용하기
# readlines.py
f = open("C:/Users/SAN-CAD5/Documents/vs/새파일.txt", 'r')
lines = f.readlines()
for line in lines :
    print(line)
f.close

# 줄 바꿈(\n) 문자 제거하기
# 파일을 읽을 때 줄 끝의 줄 바꿈(\n)문자를 제거하고 사용해야 할 경우가 많다.
# 다음처럼 strip 함수를 사용하면 줄 바꿈 문자를 제거할 수 있다.

f = open("C:/Users/SAN-CAD5/Documents/vs/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄 끝의 줄 바꿈 문자(\n)를 제거한다.
    print(line)
f.close()

# read 함수 사용하기
# read.py

