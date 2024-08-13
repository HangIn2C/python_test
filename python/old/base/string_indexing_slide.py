# 인덱싱(indexing)이란 무엇인가를 '가리킨다', 슬라이싱(slicing)은
# 무엇인가를 '잘라 낸다'라는 의미이다. 이런 의미를 생각하면서 다음 내용을 살펴보자

# 문자열 인덱싱
a = "Life is too shor, You need Python"
a[3] # a라는 문자열의 네번째 문자 e를 말한다.

# 문자열 인덱싱 활용하기
a = "Life is too short, You need python"
# space도 갯수에 포함된다.
a[0] # L
a[12] # s
a[-1] # n 뒤에서 첫번째

a[-2] # o
a[-5] # y

# 문자열 슬라이싱
a = "Life is too short, You need python"
b = a[0] + a[1] + a[2] + a[3]
b # Life

a[0:4] # Life

a[0:2] # Li
a[5:7] # is
a[12:17] # short

# a[시작_번호:끝_번호]에서 끝 번호 부분을 생략하면 시작 번호부터
# 그 문자열의 끝까지 뽑아 낸다.
a[19:] # You need python

# a[시작_번호:끝_번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 뽑아낸다.
a[:17] # Life is too short

# a[시작_번호:끝_번호]에서 시작 번호와 끝 번호를 생략하면 문자열의 처음부터 끝까지 뽑아 낸다.
a[:] # Life is too short, You need python

# 슬라이싱으로 문자열 나누기
a = "20230331Rainy"
date = a[:8]
weather = a[8:]
print("date : " + date, "\nweather : " + weather)



