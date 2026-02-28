# 1. 함수 정의하기
def open_account(): # 함수 정의
    print("새로운 계좌를 개설합니다.")
open_account() # 함수 호출
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 전달값과 반환값
#입금
def deposit(balance, money): # 2개의 전달값 (현재 잔액, 입금하려는 금액)
    print("{0}원을 입금했습니다. 잔액은 {1}원입니다.".format(money, balance + money))
    return balance + money # 잔액 정보 반환
balance = 0 # 초기 잔액
balance = deposit(balance, 1000)

#출금
def withdraw(balance, money): 
    if balance >= money: # 빼려는 돈이 잔액보다 적은 경우
        print("{0}원을 출금했습니다. 잔액은 {1}원입니다.".format(money, balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))
        return balance
balance = withdraw(balance, 2000) # 빼려는 돈이 잔액보다 많아 else문 출력
balance = withdraw(balance, 300)

#수수료 부과
def withdraw_night(balance, money):
    commission = 100 # 수수료 값
    print("업무 시간 외에 {}원을 출금했습니다.".format(money))
    return commission, balance - money - commission # 쉼표 (,)를 통해 반환 (튜플을 사용함)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 함수 호출하기
def profile(name, age = 20, main_lang = "파이썬"): # 매개변수를 미리 저장해 둔 값은 기본값이다 / 전달값을 기본값보다 먼저 쓴다
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
profile("찰리")
profile("루시", 22, "자바") # 기본값을 사용 안할 수도 있음
profile(name = "찰리", main_lang = "파이썬", age = 20)
profile("루시", main_lang="자바", age=25) # 전달값 먼저 작성 후 키워드 인자 작성 / 전달값 위치 맞아야 함 = 위치 인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end="!") # end 매개변수 없으면 2줄로 출력됨 // \n은 줄바꿈, " "띄워쓰기, !나 (,)은 문장의 마지막에 사용
    print(lang1, lang2, lang3, lang4, lang5)
profile("루시", 25, "코틀린", "스위프트", "", "", "")

def profile(name, age, *language): # *을 넣어 가변인자를 만듬 = 개수가 변할 수 있는 인자
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    
    #print(language, type(language)) # 튜플로 표현함
    for lang in language:
        print(lang, end=" ") # 언어를 모두 한 줄에 표시
    print() # 줄 바꾸기 용도
profile("찰리",20,"파이썬","자바","C", "C++", "C#", "자바스크립트")
profile("루시", 25, "코틀린", "스위프트") # 빈칸을 만들지 않아도 됨
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 지역변수와 전역변수
glasses = 10 # 모두 사용되는 전역변수

def rent(people):
    glasses = 20 # 함수 안에서만 사용되는 지역변수
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2)
print("남은 3D 안경 개수: {0}".format(glasses))

#위를 해결하기 위해
glasses = 10 

def rent(people):
    global glasses # 전역 공간에 있는 변수를 함수 안에도 사용하겠다 / but 자주 사용하면 코드가 복잡해짐
    glasses = glasses - people # global 없이 사용하면 오류 발생
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))

print("전체 3D 안경 개수: {0}".format(glasses))
rent(2)
print("남은 3D 안경 개수: {0}".format(glasses))

#global의 문제점을 해결해줄 코드
glasses = 10 

def rent_return(glasses, people): # return을 통해 전달값을 구함
    glasses = glasses - people
    print("[함수 내부] 남은 3D 안경 개수: {0}".format(glasses))
    return glasses

print("전체 3D 안경 개수: {0}".format(glasses))
glasses = rent_return(glasses, 2)
print("남은 3D 안경 개수: {0}".format(glasses))
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#실습문제
def std_weight (height, gender): # 함수 정의 / 키와 성별을 입력받음
    if gender == "남자": # 남자일 경우
        weight = (height * 0.01) ** 2 * 22
        print("키 {0}cm 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, weight)) # 소수점 2째자리이기에 {1:.2f}로 표현함
    else:
        weight = (height * 0.01) ** 2 * 21
        print("키 {0}cm 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height, weight))

std_weight (175, "남자")
print()

#답지
def std_weight (height, gender): 
    if gender == "남자": 
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 키는 m로 변환 / 소수점 2째 자리까지 표시 round 함수
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
print()

#셀프체크
def get_air_quality (air):
    if 0 <= air <= 30:
        return "좋음"
    elif 31 <= air <= 80:
        return "보통"
    elif 81 <= air <= 150:
        return "나쁨"
    else:
        return "매우 나쁨"

print(get_air_quality(15))
print()