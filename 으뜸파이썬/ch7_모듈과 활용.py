#7.6 그림 그리기 모듈 turtle
# 기본
"""import turtle as t
# print(dir(turtle)) 내장 함수 종류 표시

t.shape("turtle") # 커서 모양을 거북이로 / 6whd dlTdma
t.shapesize(2, 2) # 사이즈 키우기

t.setup(width = 400, height = 400)
for i in range(20):
    t.forward(i*10) # i만큼 직선
    t.left(93) # 93도 왼쪽으로 꺽기

t.done() # 이벤트 루프로 진입시킴 / 마우스 컨트롤이 가능한 영역
# t.bye() # 화면을 종료시킴"""
#-------------------------------------------------------------------
# 사각형 4개 각각 다른 색 채우기
"""import turtle as t

color = ["blue", "red", "yellow", "green"]

def draw_rect(): # 사각형 만드는 함수 정의
    for _ in range(4): # 4번하는데
        t.forward(100) # 100직선이동
        t.left(90) # 90도 왼쪽으로 꺽어

for j in range(4): # 4번하는데
    t.color(color[j]) # 컬러를 하나씩 꺼내고
    t.setheading(90 * j) # 각각 90도씩 돌리며
    t.begin_fill() # 시작 그린 도형에 색을 채울꺼야
    draw_rect() 
    t.end_fill() # 끝 색 채우기

t.done()"""
#-------------------------------------------------------------------
# pencolor() 메소드를 이용한 패턴 만들기
"""import turtle as t

color = ["red", "green", "blue", "orange"]

t.bgcolor("black") # 배경
t.speed(0) # 속도향상
for i in range(200):
    t.pencolor(color[i % 4])
    t.forward(i)
    t.left(93)

t.done()"""
#-------------------------------------------------------------------
"""import turtle as t

t.goto(80, 100) # 직선
t.penup() # 펜 이동
t.goto(0, 100) # 이만큼
t.pendown() # 펜을 닿게 함 (내림)
t.goto(80, 0) # 펜 이동

t.done()"""
#-------------------------------------------------------------------
# 랜덤 플로팅
"""import turtle as t
import random as rd

t.shape("circle") # 커서 모양 동그라미
d = 300
t.speed(0)
t.penup() # 펜 기능 즉, 선 이용하지 않기
for _ in range(40): # 랜덤으로 좌표를 잡아 이어보기
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x, y)
    t.stamp() # 좌표 점 찍기

t.done()"""
#-------------------------------------------------------------------
# 랜덤 터틀점 색 표시
"""import turtle as t
import random as rd

color = ["red", "green", "blue", "orange"]

t.shape("turtle")
t.shapesize(4, 4)

d = 300
t.speed(0)
t.penup() 

for i in range(40):
    x = rd.randint(-d, d)
    y = rd.randint(-d, d)
    t.goto(x, y)
    t.color(color[i % 4])
    t.stamp() # 컬러를 넣고 스탬프를 찍어야 첫번째 터틀도 색이 생김

t.done()"""
#-------------------------------------------------------------------
# 하나 이상의 객체 만들기
"""import turtle as t
t1 = t.Turtle()
t1.shape("circle")
t1.goto(100, 100)
t2 = t.Turtle()
t2.shape("square")
t2.goto(-100, 100)
t.done()"""
# 생성자를 사용하면 된다
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 새로운 창을 만드는 tkinter 모듈
"""from tkinter import *

window = Tk() # 윈도우 창 객체
label = Label(window, text = "헬로 파이썬") # 버튼, 텍스트 상자등과 같은 미리 만들어진 제어 가능한 요소들 위젯이 필요하다
# window = 부모 컨테이너 / text = 레이블 위젯에 뿌려질 문자열
label.pack() # 컨테이너에 레이블을 위치시킨다

window.mainloop() # 메소드 호출 / 이벤트 루프를 생성하는 역할 / 마우스 컨트롤이 가능한 영역"""
#-------------------------------------------------------------------
# 클릭하면 바뀌는 창
"""from tkinter import *

def change_label():
    if label.cget("text") == "헬로 파이썬":
        label.config(text = "안녕 파이썬") # 라벨 / 버튼 등의 속성
        label.config(bg = "cyan")
    else:
        label.config(text = "헬로 파이썬")
        label.config(bg = "yellow")

window = Tk()
label = Label(window, text = "헬로 파이썬", bg = "yellow")
label.pack()
btn = Button(window, text = "클릭하면 문자가 변경됨", fg = "blue", command = change_label)
btn.pack()

window.mainloop()"""
#-------------------------------------------------------------------
# Entry에 대해 - 키보드 입력을 받는
"""from tkinter import *

def entry_to_label():
    str = input_entry.get()
    label.config(text = str)

window = Tk()

input_entry = Entry(window, width = 50)
input_entry.pack()

button = Button(window, text = "처리", command = entry_to_label)
button.pack()

label = Label(window, text = " ")
label.pack()

window.mainloop()"""
#-------------------------------------------------------------------
# 사칙 연산 계산기 만들기
"""from tkinter import *

window = Tk()
window.title("계산기") # 제목
window.geometry("350x200") # 크기

Label(window, text = "숫자 1").grid(column = 0, row = 0) # grid 위치
Label(window, text = "숫자 2").grid(column = 0, row = 1)
res_label = Label(window, text = "결과 :") # 결과 레이블
res_label.grid(column = 0, row = 2) # grid의 반환값이 None이기에 따로 빼두어야 configure()가 실행됨

num1 = Entry(window, width = 10) # 키보드 입력 받기 Entry
num2 = Entry(window, width = 10)
num1.grid(column = 1, row = 0) # grid의 반환값이 None이기에 따로 빼두어야 get()이 실행됨
num2.grid(column = 1, row = 1)

def add():
    res_text = "결과 = " + str(float(num1.get()) + float(num2.get()))
    res_label.configure(text = res_text)

def subtract():
    res_text = "결과 = " + str(float(num1.get()) - float(num2.get()))
    res_label.configure(text = res_text)

def multiplication():
    res_text = "결과 = " + str(float(num1.get()) * float(num2.get()))
    res_label.configure(text = res_text)

def division():
    res_text = "결과 = " + str(float(num1.get()) / float(num2.get()))
    res_label.configure(text = res_text)

btn_plus = Button(window, text = "+", command = add).grid(column = 2, row = 1) # command = None으로 하면 연결된 함수 없음을 뜻함
btn_minus = Button(window, text = "-", command = subtract).grid(column = 3, row = 1)
btn_mult = Button(window, text = "*", command = multiplication).grid(column = 4, row = 1)
btn_div = Button(window, text = "/", command = division).grid(column = 5, row = 1)

window.mainloop() # 무한루프 진입"""
