# C:/doit/game/__init__.py
# 패키지 내 모듈을 미리 import
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 패키지 초기화
# __init__.py 파일에 패키지를 처음 불러올 때 실행되어야 하는 코드를 작성 할 수 있다. 예를 들어
# 데이터베이스 연결이나 설정 파일 로드와 같은 작업은 수행할 수 있다.

# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game ...")
