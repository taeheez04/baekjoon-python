# 1. 키보드한테서 값을 입력받는 표준 입력받기 : input()
H, M = map(int,input().split()) # map 함수를 통해 여러 개의 값을 받음
print(H + M)

import sys # sys 모듈 선언

T = int(input())
nums = [] # 리스트 정의

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().rstrip().split()) # input()보다 속도빠름 / import sys하기 / sys.stdin.readline만 하면 줄바꿈함 / rstrip()로 이를 방지
    nums.append(a + b) # a + b값을 리스트에 계속 추가

for j in range(0, T): # 리스트 순서대로 출력
    print(nums[j])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 표준 출력 print()를 사용할 때 유용한 것

# sep 매개변수 / 구분자 넣기
print("파이썬", "자바", "자바스크립트", sep=" vs ") # 기본값은 공백(" ") / sep=" " 안에 구분 기호를 표시한 (띄어쓰기도 같이)  

# end 매개변수 / 문자 끝에 지정
print("파이썬", "자바", sep=", ", end="? ") # 기본값은 줄바꿈(\n)

# 출력 위치를 지정하는 file
import sys # sys 모듈을 사용

print("파이썬", "자바", file=sys.stdout) # stdout: 표준출력 VScode의 터미널에 결과 출력
print("파이썬", "자바", file=sys.stderr) # stderr: 표준오류 터미널에 오류 메세지를 띄워라

# 공간 확보해 정렬하기 ljust(), rjust()
scores = {"수학": 0, "영어": 50, "코딩": 100}

for subject, score in scores.items(): # items()를 사용해서 딕셔너리를 (key, value)로 분리
    print(subject.ljust(8), str(score).rjust(4), sep=":") # l은 왼쪽, r은 오른쪽, just정렬 / 정렬하는 값은 문자열이여야 함 /()안의 숫자만큼 공간 확보

# 빈칸 0으로 채우기 zfill()
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # ()한 자릿수에 부족한 만큼 0을 채움
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 다양한 형식으로 출력 : format()
print("{0}".format(500))
print("{0: >10}".format(500)) # 빈칸두기(생략가능), 오른쪽 정렬, 10칸 확보 / 이렇게 3분할로 표시됨 
print()

print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) # 음수일 때
print()

print("{0:_<10}".format(500)) # 빈칸 _로 채우기, 왼쪽 정렬, 10칸 확보
print()

print("{0:,}".format(100000000000)) # 3자리마다 쉼표 찍기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
print()

print("{0:^<+30}".format(100000000000)) # 빈칸 ^로 채우기, 왼쪽 정렬, +기호 붙이기, 30칸 확보
print()

print("{0}".format(5 / 3)) # round() 함수로도 반올림할 수 있음
print("{0:f}".format(5 / 3)) # 소수점 여섯 자리까지 나옴
print("{0:.2f}".format(5 / 3)) # 소수점 2째자리까지 출력
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 파일 입출력
# 4.1 파일 열고 닫기 / open(), close()
# "r" = 읽기, "w" = 쓰기, "a" = 이어쓰기
score_file = open("score.txt", "w", encoding="utf8") # seore.txt 파일 (w)쓰기모드로 열기 / utf8 = 한글을 포함한 파일을 사용할 때
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기 / 닫지 않으면 다른 문제가 발생할 수 있음
# 실제로 파일이 생긴 걸 확인 가능

# 4.2 파일쓰기:write()
score_file = open("score.txt", "a", encoding="utf8") # 덮어쓰지 않기 위해 "a" 이어쓰기 활용
score_file.write("과학 : 80\n") # write() 함수
score_file.write("코딩 : 100\n") # print()와 다르게 줄 바꿈을 하지 않음
score_file.close()

# 4.3 파일 읽기:read(), readline(), readlines()
score_file = open("score.txt", "r", encoding="utf8") # "r"읽기모드로 열기
print(score_file.read()) # read() 파일 내용 전체를 읽어옴
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # readline() 파일 내용을 한 줄씩 읽어옴
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
print(score_file.readline(), end="") # end=""를 통해 커서는 다음 줄로 이동 / print() 함수 자체의 줄 바꿈과 중복으로 실행되는 현상을 막기 위해
score_file.close()
print()

# 줄이 얼마나 있을지 모르니 while문을 활용해 터미널에 띄움
score_file = open("score.txt", "r", encoding="utf8")

while True: # True를 설정함으로 탈출 조건을 만나기 전까지 계속 반복
    line = score_file.readline() # 파일을 읽음
    if not line: # 더 이상 읽어올 line이 없을 때
        break # 멈춤
    print(line, end="") # 읽어 온 내용 출력

score_file.close()
print()

# 파일 내용 전체를 불러와 리스트에 저장해 두고 리스트를 반복하면서 내용 출력
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # readlines()를 사용 / 파일 내 모든 줄을 읽어 와서 lines라는 리스트에 저장
for line in lines:
    print(line, end="")

score_file.close()
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. 데이터를 파일로 저장하기: pickle모듈 / 다른 코드에서 파일을 사용하기 위해 파일 저장하고 불러올 수 있게 하는 함수
import pickle # pickle 모듈 가져다 쓰기

profile_file = open("profile.pickle", "wb") # txt파일이 아닌 binary 바이너리 파일을 사용함 / wb rb ab
profile = {"이름": "스누피", "나이": 30, "취미": ["축구", "골프", "코딩"]} 
print(profile)

pickle.dump(profile, profile_file) # dump()를 통해 파일 저장 / profile 저장할 데이터를 profile_file 저장할 파일안에
profile_file.close() # 컴퓨터가 읽은 2진수 바이너리 형태이기에 사람이 확인 불가

profile_file = open("profile.pickle", "rb") # rb 바이너리 형태 읽기
profile = pickle.load(profile_file) # load()를 통해 파일 부른 후 profile에 저장

print(profile)
profile_file.close()
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. 파일 한 번에 열고 닫기: with문 / close()의 번거로움을 해소해줌
import pickle

with open("profile.pickle", "rb") as profile_file: # 파일을 열어 바이너리를 읽고 profile_file 변수에 저장
    print(pickle.load(profile_file)) # pickle 모듈의 load()로 변수 안의 파일 읽기
print()

import pickle

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
print()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. 실습문제
# txt로 사용하기에 pickle모듈 사용 x
for i in range(1, 51): # 1~50까지 반복 
    with open("{}주차.txt".format(i), "w", encoding="utf8") as report_file: # close()문을 사용하기 싫어 with문 사용
        report_file.write("- {}주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :".format(i)) # 각 주차에 들어간 내용 입력
# 위 코드 사용 시 50개의 파일이 생김

# 8. 셀프체크
# 답지
with open("class.txt", "w", encoding="utf8") as class_file:
    class_file.write("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명") # 문제대로 파일 생성

with open("class.txt", "r", encoding="utf8") as class_file:
    a=class_file.read().split() # 파일을 읽은 후 내용을 띄어쓰기로 구분해 리스트로 변환
    
    for i in a: # a에 단어를 하나씩 꺼내 / a = 반복대상, i = 반복대상을 변수로 가져옴
        print(i, end=" ") # 복사 반복
        if i.endswith("명"): # 만약 명으로 끝나면
            print() # 줄바꿈

# 여기서 출력해버리면 파일을 54개 만들어짐