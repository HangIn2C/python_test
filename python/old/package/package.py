"""
파이썬에서 패키지(packages)란 관련있는 모듈의 집합을 말한다. 패키지는 파이썬 모듈을
계층적(디렉터리 구조)으로 관리할 수 있게 해 준다.
# 파이썬에서 모듈은 하나의 .py 파일이다.
파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어진다.
다음은 임의로 그려 본 game 이라는 파이썬 패키지의 구조이다.

game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py

game, sound, graphic, play는 디렉터리, 확장자가 .py인 파일은 파이썬 모듈이다.
game 디렉터리가 이 패키지의 루트 디렉터리, sound, graphic, play는 서브 디렉터리이다.
"""

# 패키지 만들기
