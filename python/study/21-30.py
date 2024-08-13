# 021 문자열 인덱싱
""" letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요 """
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
""" 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요 """
license_plate = "24가 2210"
# before4word = license_plate[4:]
before4word = license_plate[-4:]
print(before4word)

# 023 문자열 인덱싱
"""
아래의 문자열에서 '홀'만 출력하세요
"""
string  = "홀짝홀짝홀짝"
temp = ""
for i in string:
    if i == "홀":
        temp += "홀"
print(temp)
# or
print(string[::2]) # 슬라이싱할 때 '시작인덱스:끝인덱스:오프셋'을 지정할 수 있다.

# 024 문자열 슬라이싱
""" 문자열을 거꾸로 뒤집어 출력하세요 """
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환(replace 메서드를 사용하면 문자열을 일부 치환할 수 있다.)
""" 아래의 전화번호에서 하이푼('-')을 제거하고 출력하세요 """
phone_number = "010-1111-2222"
modi_number = phone_number.replace("-", " ")
print(modi_number)

# 026 문자열 다루기
""" 25문자의 전화번호를 모두 붙여 출력하세요 """
modi_number2 = phone_number.replace("-", "")
print(modi_number2)

# 027 문자열 다루기
""" url에 저장된 웹 페이지 주소에서 도메인을 출력하세요(kr) """
url = "http://sharebook.kr"
print(url[-2:])
# or
url_split = url.split('.')
print(url_split);print(url_split[1])

# 028 문자열은 immutable(불변) 문자열은 수정할 수 없다.
lang = 'python'
lang[0] = 'P' # 에러 발생
print(lang)

# 029 replace 메서드
""" 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요 """
string = "abcdfe2a354a32a"
string = string.replace("a", "A")
print(string)
# 바꾸고 string에 다시 입력해서 변하지 않는다.

# 030 replace 메서드
#아래 코드의 실행 결과를 예상해 보세요
string = 'abcd'
string.replace('b', 'B')
print(string)
# string 원래의 값으로 돌아온다.






