# 8.2 try - except 문
try:
    b = 2 / 0 # 0으로 나눔
    a = 1 + "hundred" # int와 str를 더하려 함
except Exception as e: # 이를 통해 오류의 종류를 알 수 있다
    print("error :", e)
print("#1")
#-------------------------------------------------------------------
# 8.4 try - except - else 오류가 발생하지 않았을 때 출력
"""try:
    a, b = input("두 수를 입력하시오: ").split()
    result = int(a) / int(b)
except ZeroDivisionError:
    print("오류 : 0으로 나눔을 시도했습니다.")
except ValueError:
    print("오류 : 입력 값이 정수나 실수가 아닙니다.")
except:
    print("오류 : 10 2와 같이 두 정수를 입력하세요.")
else: 
    print(f"{a} / {b} = {result}")"""
#-------------------------------------------------------------------
# 8.5 try - except - finally 오류가 나든 말든 무조건 출력
def divide (x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("0으로 나누는 오류발생")
    else:
        print("결과 :", result)
    finally:
        print("수행완료")

print("divide(100, 0) 함수호출 :")
divide(100, 0)
print("#3")
#-------------------------------------------------------------------
# 8.6 raise 예외 강제 발생
"""def get_ans(ans):
    if ans in ["예", "아니오"]:
        print("정상적인 입력입니다.")
    else:
        raise ValueError("입력을 확인하세요.")
    
while True:
    try:
        ans = input("예/아니오 중 하나를 입력하세요 :")
        get_ans(ans)
        break # 정상적인 입력에만 탈출
    except Exception as e: # ValueError라고 하는 Exception 객채를 생성하여 반환
        print("error :", e)"""
#-------------------------------------------------------------------
# 8.7 파일 입출력
"""f = open("hello.txt", "w") # 파일을 열고 (없으면 생성) / open() 파일 객체 반환
f.write("Hello World!") # 문자작성
f.close() # 닫기
# r 읽기 / w 쓰기 / a 추가 / x 쓰기전용, 파일 새로 만듬, 파일 있으면 오류 / + 읽기 쓰기 모드
# t 텍스트 (wt) / b 바이너리 (wb) / r+t 텍스트 읽기 쓰기, 파일 없으면 오류 / w+t 텍스트 쓰기 읽기, 파일 내용 다 지우고 새로 씀 / a+t 뒤에서부터 텍스트 추가, 쓰기모드
f = open("hello.txt", "r")
s = f.read() # 읽는다, readline().rstrip 한 줄씩 읽고 오른쪽에 있는 모든 공백문자 지움
print(s) # 출력
f.close()

f = open("hello.txt", "a", encoding = "UTF8") # 인코딩방식 = "UTF8" 한글 사용 가능
f.write("This will be appended.\n")
f.write("안녕.\n")
f.close()"""
#-------------------------------------------------------------------
# 8.8 (심화) with 문법, 파일 열고 닫고를 한 번에 / 파일 여는 동작을 with()만 사용할 수 있음
f = open("hello.txt", "w")
f.write("Hello World!")
f.close() # 파일 열기가 실패할 경우 급작스럽게 닫힘

f = open("hello.txt", "w")
try: # 열기를 실패할 경우 오류로 인식
    f.write("Hello World!")
finally:
    f.close() # 급작스럽게 닫힘 방지

# with()안에 __enter__(), __exit__()메소드들의 포함됨
with open("hello.txt", "w") as f: # __enter__() = f로 다뤄짐
    f.write("Hello World!") # 위 코드를 간단히 / __exit__()이 파일을 자동으로 닫아줌
