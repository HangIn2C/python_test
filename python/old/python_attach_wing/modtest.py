# modtest.py

import mod2
result = mod2.add(3,4)
print(result)

"""
다른 파이썬 파일에서도 import mod2로 mod2 모듈을 불러 와서 사용할 수 있다.
대화형 인터프리터에서 한 것과 동일한 방법이다. 위 예제가 정상적으로 실행되기
위해서는 modtest.py 파일과 mod2.py 파일이 동일한 디렉터리 (c:\doit)에 있어야 한다.

>>> import sys
>>> sys.path
['', 'C:\\Users\\SAN-CAD5\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\SAN-CAD5\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\SAN-CAD5\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\SAN-CAD5\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\SAN-CAD5\\AppData\\Roaming\\Python\\Python312\\site-packages', 'C:\\Users\\SAN-CAD5\\AppData\\Roaming\\Python\\Python312\\site-packages\\win32', 'C:\\Users\\SAN-CAD5\\AppData\\Roaming\\Python\\Python312\\site-packages\\win32\\lib', 'C:\\Users\\SAN-CAD5\\AppData\\Roaming\\Python\\Python312\\site-packages\\Pythonwin', 'C:\\Users\\SAN-CAD5\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']

sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리 목록을 보여 준다. 이 디렉터리 안에
저장된 파이썬 모듈은 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러 사용할 수 있다.

그렇다면 sys.path에 C:\doit\mymod 디렉터리를 추가하면 mymod 디렉터리에 저장된 파이썬
모듈은 아무 곳에서나 불러 사용할 수 있다.
sys.path는 리스트이므로 다음과 같이 할 수 있다.

>>> sys.path.append("C:/doit/mymod")
>>> sys.path
['', ~~ ,
'C:/doit/mymod']

sys.path.append를 사용해서 C:/doit/mymod 라는 디렉터리를 sys.path에 추가했다. 그리고 다시
sys.path를 축력해 보니 가장 마지막에 C:/doit/mymod 디렉터리가 추가되었다.

>>> import mod2
>>> print(mod2.add(3,4))

path에 mymod 위치를 추가하여 디렉터리 이동없이 모듈을 불러와서 사용할 수 있다.
"""

"""
PYTHONPATH 환경 변수 사용하기
모듈을 부러와서 사용하는 또 다른 방법으로는 PYTHONPATH 환경 변수를 사용하는 것이 있다.

C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>> import mod2
>>> print(mod2.add(3,4))
7

set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를
설정한다. 그러면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 mymod 디렉터리에 저장된
mod2 모듈을 불러와서 사용할 수 있다.
"""