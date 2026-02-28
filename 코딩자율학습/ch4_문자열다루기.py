# 2.슬라이싱
jumin = "990229-1234567"
print(jumin[7]) # 7번째
print(jumin[2:4]) # 2 ~ 4직전까지
print(jumin[:6]) # 0 ~ 6직전까지 (ex [7:], [:])
print(jumin[-7:]) # 음수 (-)는 뒤에서부터(-1부터) 시작
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.함수로 문자열 처리
python = "Python is Amazing"
print(python[0].isupper()) # 대문자인지 확인
print(python[1:3].islower()) # 소문자인지 확인
print(python.replace("Python", "Java")) # 위치 바꾸기

# find() 위치 알기
print(python.find("n")) # n위치 찾기
print(python.find("Java")) # Java가 없어 -1 반환 / index는 오류 발생
# index() 
print(python.index("n"))
print(python.index("n", 2, 6)) # 2 ~ 6직전에서 n 찾기
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.문자열 포매팅
# 4-1 서식 지정자 사용
print("원주율은 %.2f입니다." % 3.14) # 소수점 2번째자리까지 / 생략시 6번째자리까지
print("Apple은 %c로 시작해요." % "A") # 문자
print("나는 %s색 %s개를 주세요." % ("파란", 20)) # 문자열, 정수값 가능 / 값을 여러개 넣은 상황

# 4-2 ()함수 사용
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {0}살이며, {1}색을 좋아해요.".format("빨간", 20))

# 4-3 f-문자열 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5.탈출문자
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace") # \\사용
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace") # r 사용: 어떤 값이든 무시하고 출력

print("Red Apple\rPine") # Pine가 \r을 만나 맨 앞으로 (Red 를 덮는 효과 / 인덱스 갯수만큼)
print("Redd\bApple") # backspace 역할
print("Red\tApple") # Tab 역할 (8칸 - 조정가능)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#실습문제
site = "http://naver.com" # 사이트 이름 표시
passward = site[7:-4] # site에서 앞에 http://와 뒤에 .com을 슬라이싱을 통해 떼어냄
pw = passward[:3] + str(len(passward)) + str(passward.count("e")) + "!" # 최종 pw는 passward 첫 3문자 + 총 길이 + e문자열의 개수 + !로 구성
print("%s의 비밀번호는 %s입니다." % (site, pw)) # 서식 지정자를 사용해 표현
print()

site = "http://daum.net" 
passward = site[7:-4]
pw = passward[:3] + str(len(passward)) + str(passward.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(site, pw)) # format()함수를 사용
print()

site = "http://google.com"
passward = site[7:-4]
pw = passward[:3] + str(len(passward)) + str(passward.count("e")) + "!"
print(f"{site}의 비밀번호는 {pw}입니다.") # f-문자열 사용
print()

# 답지
site = "http://youtube.com"
passward = site.replace("http://","") # replace를 통해 http://을 삭제
passward = passward[:passward.index(".")] # passward.index(".")이 .의 인덱스 위치를 찾아 그 뒤를 날림 
pw = passward[:3] + str(len(passward)) + str(passward.count("e")) + "!"
print("%s의 비밀번호는 %s입니다." % (site, pw))
print("{0}의 비밀번호는 {1}입니다.".format(site, pw)) # 순서 부여
print(f"{site}의 비밀번호는 {pw}입니다.")
print()

#셀프체크
# 주어진 문장: the early bird catches the worm.
# 주어진 문장: Action Speak Louder Than Words.
# 주어진 문장: PRACTICE MAKES PERFECT.
proved = "the early bird catches the worm."
print(proved[0].upper() + proved[1:].lower())
print(proved.capitalize()) # 파이썬에서 제공하는 함수 / 1글자 대문자, 나머지 소문자