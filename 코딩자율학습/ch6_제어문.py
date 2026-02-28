# 1. 조건문
# if / elif / else
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 반복문
# for문 (범위 안 반복)
orders = ["아이언맨", "토르", "스파이더맨"] # 리스트, 딕셔너리, 튜플, 문자열, 데이터를 담은 변수명 all pass
for customer in orders:
    print("{0} 님, 커피가 준비됐습니다. 픽업대로 와주세요.".format(customer))

# for 문 한 줄로 작성하기
students = [1, 2, 3, 4, 5]
print(students)
students = [i + 100 for i in students] # i가 들어간 두 자리의 변수명이 같아야 함
print(students)

students = ["Iron man", "Thor", "Spider Man"]
print(students)
students = [i.upper() for i in students] # 모두 대문자로 바꿈
print(students)
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# while문 (조건을 만족할 동안 계속 반복하는) / True로 인한 반복 crtl + c로 강제 종료
customer = "토르" 
index = 5

while index >= 1:
    print("{} 님, 커피가 준비됐습니다.".format(customer))
    index -= 1 # 1번 부를때마다 1씩 차감
    print("{}번 남았어요.".format(index))
    if index == 0: # 0이 되면 밑의 print()문 출력
        print("커피를 폐기 처분합니다.")

"""customer = "토르" 
person = None # 값이 없다는 의미
while person != customer: # person과 coustomer 값이 다를 때 밑과 같이 출력
    print("{0} 님, 커피가 준비됐습니다.".format(customer))
    person = input("이름이 어떻게 되세요? :")"""

# continue, break (반복문 흐름 제어)
absent = [2, 5]
no_book = [7]
for student in range(1, 11): # 1~10번
    if student in absent: # 없는 번호일 경우
        continue # 다음 번호로 넘어가기
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}번 학생은 교무실로 따라와요.".format(student))
        break # 반복문 탈출
    print("{0}번 학생, 책을 읽어 보세요.".format(student))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#실습 문제
from random import * # sample을 사용하기 위해 random 모듈 추가

all_customer = 0 # 총 탑승객 수 정의
for texi_customer in range(1, 51): # 임의의 사람 50명 정의
    texi_time = sample(range(5, 51), 1) # 사람들에게 5~50분 사이의 소요시간 랜덤으로 부여
    if texi_time > [15]: # 15분을 초과하는 승객일때
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(texi_customer, texi_time))
    else: # 5분 이상 15분 이하인 손님일 때 (그외 상황)
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(texi_customer, texi_time))
        all_customer += 1 # 총 탑승객을 1씩 추가함
print("총 탑승객 : {}명".format(all_customer)) # 총 탑승객 출력
print()

### 내 답의 문제점: sample을 사용함으로써 랜덤으로 숫자를 부여하긴 하지만 이를 리스트형태로 표현되므로 int형태를 원했던 답과 벗어남
### list형태 이기에 if문에 [15]를 쓰게 됨 /// 이 외에는 모두 같음

#답지
from random import *

cnt = 0
for i in range(1, 51): 
    time = randrange(5, 51) # randrange가 랜덤으로 ()안 숫자들 중 랜덤으로 부여한다는 의미 / 이를 통해 int형태로 출력가능
    if 5 <= time < 15: # 이런 식의 표현이 문제와 더 가까움
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승객 : {0}명".format(cnt))
print()

#셀프체크
product = 3
for i in range(0, product):
    print("2+1 상품입니다.")
sum = int(1 * product - (product / 3))
print("총 가격은 {0}000원입니다.".format(sum))
print()

#답지
price = 1000
goods = 6
total = 0
for i in range(1, goods + 1): # 1~3 반복
    print("2+1 상품입니다.")
    if i % 3 == 0: # 3의 배수일 경우 가격을 더하지 않고 넘김
        continue
    total += price # price를 계속 더함
print("총 가격은 " + str(total) + "원입니다.")