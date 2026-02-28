#region 7.1
# (1)
import datetime as dt

start_day = dt.datetime(2019, 2, 24) # 시작날짜

time_gap = dt.datetime.now() - start_day # 시간 차이

print(f"춘향이와 몽룡이의 연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")
print(f"연애 시작일로부터 경과한 날짜 : {time_gap.days}일")
print()

# (2) timedelta 사용
print(f"춘향이와 몽룡이의 연애 시작일 : {start_day.year}년 {start_day.month}월 {start_day.day}일")

day_100 = start_day + dt.timedelta(days = 100) # 시작일로부터 100일 경과 시간
day_200 = start_day + dt.timedelta(days = 200) 
day_500 = start_day + dt.timedelta(days = 500)
day_1000 = start_day + dt.timedelta(days = 1000)

print(f"100일 기념일 : {day_100.year}년 {day_100.month}월 {day_100.day}일")
print(f"200일 기념일 : {day_200.year}년 {day_200.month}월 {day_200.day}일")
print(f"500일 기념일 : {day_500.year}년 {day_500.month}월 {day_500.day}일")
print(f"1000일 기념일 : {day_1000.year}년 {day_1000.month}월 {day_1000.day}일")
print()
#endregion
#-------------------------------------------------------------------
#region 7.2
# (1)
import time

def sum1to1000000(): # 합을 구하는 함수 정의
    sum1to1000000 = 0
    for i in range(1, 1000001):
        sum1to1000000 += i

start_time1 = time.time() # 시작
sum1to1000000() # 함수 호출
end_time1 = time.time() # 끝

print("1에서 1,000,000까지의 합을 구하는 시간 : {0:.4f}초".format(end_time1 - start_time1)) # 소수점 4번째 자리까지 0:.4f
print()

# (2)
import time

start_time2 = time.time() 
for i in range(100):  # 함수 100번 호출
    sum1to1000000()
end_time2 = time.time()

print("1에서 1,000,000까지의 합을 100번 반복해서 구하는 시간 : {0:.4f}초".format(end_time2 - start_time2)) # 소수점 4번째 자리까지 0:.4f
print()
#endregion
#-------------------------------------------------------------------
#region 7.3
# (1)
import time

def HP():
    print("Hello Python!")


start_time1 = time.time()
for i in range(100):
    HP()
end_time1 = time.time()

print("Hello Python! 출력을 100번 반복하는 시간 : {0:.4f}초".format(end_time1 - start_time1)) 
print()

# (2)
import time
import math

def fact():
    math.factorial(1000)


start_time2 = time.time() 
for i in range(100):  
    fact()
end_time2 = time.time()

print("1000!을 100번 반복해서 구하는 시간 : {0:.4f}초".format(end_time2 - start_time2))
print()

# (3)
import time
import math

def square_sum():
    sum1 = 0
    for i in range(1, 1001):
        if i % 2 != 0:
            sum1 += math.pow(i, 3) # pow() 제곱의 합수

start_time3 = time.time() 
for i in range(100):  
    square_sum()
end_time3 = time.time()

print("1에서 1000까지 홀수의 세제곱 더하기를 100번 반복하는 시간 : {0:.4f}초".format(end_time3 - start_time3))
print()

# (4)
import time
import math

def sin_sum():
    sum2 = 0
    for i in range(1, 361):
        sum2 += math.sin(i) # sin() 사인 함수

start_time4 = time.time() 
for i in range(100):  
    sin_sum()
end_time4 = time.time()

print("1에서 360도까지 sin 값의 합을 100번 반복하는 시간 : {0:.4f}초".format(end_time4 - start_time4))
print()
#endregion
#-------------------------------------------------------------------
#region 7.19 타이머 만들기
from tkinter import *

minutes = 0 # 시간 정의
sec = 0
centisec = 0 
b_working = False # 타이머 실행 여부

def increase_time():
    global minutes, sec, centisec, b_working # 전역변수로 불러오기

    if b_working == True: # 타이머가 실행이라면
        centisec += 1 
        sec += (centisec // 100)
        centisec %= 100
        minutes += (sec // 60)
        sec %= 60 # 시간에 대한 식들

        label.after(10, increase_time) # 10 밀리초로 카운트
        label.config(text = "{0:02d}:{1:02d}:{2:02d}".format(minutes, sec, centisec)) # config 라벨 / 버튼 등의 속성

def start_time(): # 시작함수
    global b_working
    if b_working:   # 이미 실행 중이면 재시작을 막음
        return
    b_working = True # 타이머 실행
    increase_time() # 함수 호출

def stop_time(): # 종료함수
    global b_working
    b_working = False # 타이머 종료

def reset_time(): # 리셋함수
    global minutes, sec, centisec
    minutes = sec = centisec = 0 # 시간을 모두 0으로
    display = "{0:02d}:{1:02d}:{2:02d}".format(minutes, sec, centisec) 
    label.config(text = display) # 라벨


window = Tk()
window.title("Timer")

label = Label(window, text = "00:00:00", fg = "black", font = "Arial 120 bold") # 텍스트, 배경, 폰트
label.pack() # pack() 자동으로 위에서 아래로 배치

button = Button(window, text = "Start", command = start_time) # 버튼 각각의 기능
button.pack() # 각각 사용

button = Button(window, text = "Stop", command = stop_time)
button.pack()

button = Button(window, text = "Reset", command = reset_time)
button.pack()

window.mainloop() # 윈도우 무한루프
#endregion
#-------------------------------------------------------------------
#region 8.10 파일 안 랜덤 숫자 넣기
import random # 모듈 전체를 불러옴 ex) random.randint
# form random import * # 현재 이름공간으로 직접 가져옴 ex) randint 바로 써도 가능 (이름 충돌함 / 잘 안 씀)
from collections import Counter # Counter이 숫자를 세어줌

rand30 = []

for i in range(30):
    rand30.append(random.randint(1, 10)) # 리스트에는 append()로 추가할 것 적기 편할 듯

with open("randint30.txt", "w") as f:
    for j in rand30:
        f.write(str(j) + " ") # 리스트에 문자를 꺼내 str()형태로 1칸 띄어 적어둠

with open("randint30.txt", "r") as t:
    s = t.read()
    nums = list(map(int, s.split())) # 읽은 걸 int형태로 구분하여 nums[]에 넣어둠

counter = Counter(nums) # counter이 숫자를 세어둔 것 / 딕셔너리 형태

for i in range(1, 11): # 이를 1~10까지 몇개씩인지 출력
    print(f"{i} : {counter[i]}개")
#endregion
#-------------------------------------------------------------------
#region 9.14 주어진 원의 면적들을 구할 수 있고, 이들이 좌표에서 겹치는 지 포함되는 지를 알 수 있음
class Circle:
    PI = 3.14 # 클래스 변수
    def __init__(self, x, y, radius): # 생성자 메소드
        self.__x = x # 인스턴스 변수
        self.__y = y
        self.__radius = radius

    def __str__(self): # 클래스 안에서의 메서드 순서 상관 X / 밖에서 사용 순서가 중요
        return "Circle : (x = {0}, y = {1}, r = {2}), 면적: {3}".format(self.__x, self.__y, self.__radius, self.area()) # self.area는 메서드의 주소가 출력됨 / 클래스 안에 정의된 함수이므로 메서드처럼 사용

    def set_x(self, x): # 값을 바꿈(지정)
        self.__x = x
    def get_x(self): # 반환
        return self.__x
    
    def set_y(self, y):
        self.__y = y
    def get_y(self):
        return self.__y
    
    def set_raduis(self, raduis):
        self.__radius = raduis
    def get_radius(self):
        return self.__radius

    def area(self): # 넓이 구하는 메서드
        return Circle.PI * self.__radius ** 2

    def overlaps(self, c): # 겹친다 / 완전히 떨어진 경우만 빼면 됨
        distance = ((self.__x - c.__x) ** 2 + (self.__y - c.__y) ** 2) ** 0.5 # 중심거리

        r1 = self.__radius # 반지름의 값 선언
        r2 = c.__radius

        if distance > (r1 + r2): # 겹칩의 조건 (중심거리 > 두 원의 반지름 합)
            return False
        else:
            return True

    def contains(self, c): # 포함된다
        distance = ((self.__x - c.__x) ** 2 + (self.__y - c.__y) ** 2) ** 0.5 

        r1 = self.__radius 
        r2 = c.__radius

        if r1 < distance + r2: # 포함의 조건 (큰 원의 반지름 > 두 원의 중심 거리 + 작은 원의 반지름 (큰 원의 중심으로부터 가장 끝 점))
            return False
        else:
            return True

c1 = Circle(0, 0, 100)
c2 = Circle(0, -10, 10)
c3 = Circle(-100, 0, 120)

print("c1 =", c1)
print("c2 =", c2)
print("c3 =", c3)

print("c1 containa c2 :", c1.contains(c2))
print("c1 containa c3 :", c1.contains(c3))
print("c1 overlaps c2 :", c1.overlaps(c2))
print("c1 overlaps c3 :", c1.overlaps(c3))
#endregion
#region 10.25 m ~ n사이의 소수를 리스트 형식으로 반환하는 함수가 for문 > 리스트 축약 표현, all()함수를 사용하여 다시 구현
# 원래 코드
def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

def primes(m, n):
    prime_list = []
    for val in range(m, n + 1):
        if is_prime(val) == True:
            prime_list.append(val)
    return prime_list

print(primes(10, 50))

# 다시 구현한 코드
def is_prime(n):
    if n == 2 or n == 3: # 즉시 True인 경우는 넣지 않음
        return True
    return all(n % i != 0 for i in range(2, n))
# all(조건식 for 요소 in 반복대상)

def primes(m, n):
    return [val for val in range(m, n + 1) if is_prime(val) == True]

print(primes(10, 50))
#endregion
#region 11.20 
# (1) 다음과 같은 관계식을 만족시키는 해 x, y, z를 linalg.solve()함수를 이용하여 구하시오
# 2x + y + z = 16
# x + 2y + z = 9
# x + y + 2z = 3
import numpy as np

a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([16, 9, 3])
x = np.linalg.solve(a, b)
print("x = {0:.1f}, y = {1:.1f}, z = {2:.1f}".format(x[0], x[1], x[2])) # 부동 소수점때문에 2:.1f로 표시
print()

# (2) 선형방정식에서 왼쪽 변의 방정식의 계수는 다음과 같은 행렬로 표기할 수 있다
# A = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]]) 이 행렬의 행렬식을 linalg.det()함수를 사용하여 구하시오
A = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
print("def(A) =", np.linalg.det(A))
#endregion