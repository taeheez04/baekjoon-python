# 1. 예외 처리하기 // 오류 상황을 대처하는 것
# try - expcept문 / 예외 처리하기
"""try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1])) # 이 문장을 추가하지 않았을 때 - 오류발생 IndexError
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError: # "값이 잘못됨" 오류 출력문
    print("오류 발생! 잘못된 값을 입력했습니다.")

# as / 오류 메세지를 예외 처리로 출력하기
except ZeroDivisionError as err: # "0으로 나눌 수 없음" 오류 출력문
    print(err)

except Exception as err: # 정의하지 않은 오류에 대한 예외 처리
    print("알 수 없는 오류가 발생했습니다.")
    print(err)"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 오류 발생시키기
"""try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError # 오류 발생시키기
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError: # "값이 잘못됨" 오류 출력문
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 사용자 정의 예외 처리하기
"""class BigNumberError(Exception): # 사용자 정의 예외 처리, Exception 클래스 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self): 
        return "[오류 코드 001] " + self.msg # 오류 메세지 가공 / 001 두자리 입력됨, 002 문자열이 입력됨, 003 공백이 입력됨

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError: 
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err: # 사용자 정의 예외 처리
    print("오류가 발생했습니다. 한자리 숫자만 입력하세요.")
    print(err)"""

class SpecialClass(): # 언더바 2개씩 붙은 형태의 메서드 = 스페셜 메서드 or 던더 메서드
    def __init__(self):
        print("특별한 생성자")

    def __str__(self):
        return "특별한 메서드"
    
s = SpecialClass()
print(s)
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 오류와 상관없이 무조건 실행하기: finally
"""class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self): 
        return self.msg 

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError: 
    print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

except BigNumberError as err: 
    print("오류가 발생했습니다. 한자리 숫자만 입력하세요.")
    print(err)

finally: # 오류 발생 여부와 상관없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")"""

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. 실습 문제: 치킨 주문하기
"""class SoldOutError(Exception): # SoldOutError 정의
    pass

try:
    chicken = 10 # 남은 치킨 수
    waiting = 1 # 대기번호, 1부터 시작

    while True:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order < 1: # 1보다 작거나 숫자가 아닌 입력값이 들어오면 오류 발생
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
            waiting += 1 # 대기번호 1증가
            chicken -= order # 주문 수만큼 남은 치킨 감소
        
        if chicken == 0:
            raise SoldOutError
        print()


except ValueError:
    print("값을 잘못 입력했습니다.")
except SoldOutError:
    print("재료가 소진돼 더 이상 주문을 받지 않습니다.")

# 답지
# try와 while문의 위치를 바꿈에 따라 오류가 발생해도 코드를 계속 수행 그 후 break로 반복 종료
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1

while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
            waiting += 1 
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
        print()

    except ValueError:
        print("값을 잘못 입력했습니다.")
    except SoldOutError:
        print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
        break"""

# 셀프체크
# 배터리 잔량에 따라 스마트폰 배터리를 관리하는 프로그램
def save_battery(level):
    print("배터리 잔량 : {0}%". format(level))
    try:
        if level > 30: # 잔량이 30% 초과
            print("일반 모드로 사용합니다.\n")
        elif 5 < level <= 30: # 잔량이 5% 초과 30% 이하
            print("절전 모드로 사용합니다.\n")
        else: # 잔량이 5%이하
            raise Exception ("배터리가 부족해 스마트폰을 종료합니다.\n")
    
    except Exception as e: # 굳이 class안 만들고 Exception 쓰기
            print(e)

# 테스트 코드
save_battery(75)
save_battery(25)
save_battery(3)