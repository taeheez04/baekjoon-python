# 숫자 처리 함수
print(abs(-5)) # 절댓값
print(pow(4, 2)) # 제곱
print(round(3.54)) # 생략시 소수점 1번째 자리에서
print(round(4.678, 2)) # 반올림 소수점 2번째 자리까지

# math 모듈
from math import *
print(floor(4.99)) # 내림 (버림)
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근 (실수로 표현)

# random 모듈
from random import *
print(random()) # 0 <= x < 1 사이의 수를 출력 (난수) (float형)
print(int(random() * 10) + 1) # 0 <= x < 10 사이의 정수 중에 난수 출력 후 +1 / 즉, 1 <= x < 11에서 출력
print(randint(1, 45)) # 1 <= x <= 45 사이 난수 (int형)
print(randrange(1, 46)) # 1 <= x < 46사이 난수 (int형)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 실습문제
from random import *
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정됐습니다.")

# 셀프체크
Celsins = 30
print("섭씨 온도 : " + str(Celsins))
Fahrenheit = (Celsins * 9 / 5) + 32
print("화씨 온도 : " + str(Fahrenheit))
print()

Celsins = 10
print("섭씨 온도 : " + str(Celsins))
Fahrenheit = (Celsins * 9 / 5) + 32
print("화씨 온도 : " + str(Fahrenheit))