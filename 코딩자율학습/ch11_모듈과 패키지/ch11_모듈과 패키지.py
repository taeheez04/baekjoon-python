# 1. 모듈 다루기
import theater_module as mv # 모듈 가져오기 / as를 통해 별명을 만들어 사용하기 쉬움
mv.price_soldier(5)

from theater_module import price, price_morning # from ~ import 문 / * 사용시 모두 사용
price_morning(4) # soldier은 import하지 않아 사용 불가

from theater_module import price_soldier as price # 벌명을 만들어 사용
price(10)
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 패키지 다루기
import travel.thailand # travel 패키지의 thailand 모듈 가져오기
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # import를 통해 클래스 가져옴
trip = ThailandPackage() # travel.thailand 제외가능
trip_to.detail()

from travel import vietnam # import 대상에 따라 코드도 달라짐 / 여기서는 모듈이 대상
trip_to = vietnam.VietnamPackage()
trip_to.detail()
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 모듈 공개 설정하기: __all__
from travel import * # __init__.py에 공개로 설정해둠
trip_to = vietnam.VietnamPackage() # 공개 설정 없이 출력 시 오류 발생
trip_to.detail()
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 모듈 직접 실행하기 // 단독으로 사용해야 else문 출력됨, 위에서 import(정의는 1번만)했기에 else문 출력 x // 터미널 찾아보면 위 코드들에서 else문이 출력됨
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. 패키지와 모듈 위치 확인하기
import inspect # getfile 함수를 사용하기 위해 inspect 모듈 사용
import random
print(inspect.getfile(random)) # random 모듈 위치(경로)

from travel import *
print(inspect.getfile(thailand))
print()


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. 패키지 설치하기
# 책을 참고 / 전세계 다른 사람들이 만들어 둔 패키지를 가져와 사용하는 방법을 알려줌

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. 내장 함수 사용하기
# import로 모듈을 선언하면 사용할 수 있는 내장함수에 추가됨을 알 수 있음 / 웹 페이지에서도 확인가능 (책 참고)
print(dir())

import random # 랜덤 모듈 선언
print(dir()) # 다른 창에서 실행할 것
print(dir(random))
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8. 외장 함수 사용하기 / import해야 사용할 수 있는 것 / 목록을 볼 수 있는 웹 사이트가 있음
# 8.1 폴더 또는 파일 목록 조회 모듈
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 출력
print()

# 8.2 운영체제의 기본 기능 모듈
import os
print(os.getcwd()) # 현재 작업 폴더 위치(경로)

"""folder = "sample_dir"
if os.path.exists(folder): # 같은 이름의 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제했습니다.") # 삭제 문구 출력
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성했습니다.")"""

print(os.listdir()) # 현재 작업 폴더 안의 폴더와 파일 목록 출력
print()

# 8.3 시간 관련 모듈
import time 
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print("우리가 만난 지 100일은", today + td)
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 9. 실습 문제: 나만의 모듈 만들기
import byme
byme.sign()
print()

# 셀프 체크
# greeting.py 확인