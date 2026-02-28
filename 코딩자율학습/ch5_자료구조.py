# 1. 리스트 / # []대괄호를 사용함
subway = ["푸", "피글렛", "티거"]

print(subway.index("피글렛")) # 위치
subway.append("이요르") # 값 추가 
print(subway) # print(subway.append(""))라 사용시 반환값이 None이기에 이를 출력
subway.insert(1, "루") # 1번째 자리에 삽입
print(subway)
print(subway.pop()) # 끝 값 반환 후 삭제
print(subway)
subway.clear() # 리스트 안의 값을 모두 삭제
print(subway)
subway.append("푸")
print(subway.count("푸")) # 문자열과 마찬가지로 같은 값의 갯수를 알려줌

num_list = [5, 2, 4, 3, 1]
num_list.sort() # 오름차순
num_list.sort(reverse=True) # 내림차순
num_list.reverse() # 순서 뒤집기

you_list = [1, 3, 2]
# my_list = sort(you_list) // sort는 기존 리스트 데이터를 변경함 / 리스트 명을 그대로 사용 / 오류
new_list = sorted(you_list) # sorted는 기존 리스트 데이터를 변경하지 않고 정렬된 새로운 리스트를 만듬
print(you_list)
print(new_list)

mix_list = ["푸", 20, True]
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list) # 리스트 합치기 / 뒤로 들어감
print(num_list)
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. 딕셔너리 / # {}중괄호와 :세미콜론 사용으로 한 쌍을 만듬
cabinet = {3: "푸", 100: "피글렛"}
print(cabinet[3]) # index역할을 key가 함 > 이를 통해 value에 접근 / key가 할당되지 않으면 오류 출력
# valus로 key를 찾을 수는 없다

print(cabinet.get(100)) # get()사용 가능 / 할당되지 않는 key에는 None을 출력
print(cabinet.get(5, "사용가능")) # key에 해당하는 값이 없으면 기본값을 사용

print(3 in cabinet)
print(5 in cabinet) # in 연산자를 사용하여 자료구조에 해당 key의 유무 확인
print("곰" in "곰돌이") # in 연산자는 문자열에 해당 글자가 포함됐는지 확인할 때도 사용가능

cabinet = {"A-3": "푸", "B-100": "피글렛"}
print(cabinet)
cabinet["A-3"] = "티거" # key에 해당 값 있음 > 값 변경
cabinet["C-20"] = "이요르" # key에 해당하는 값이 없을 때 > 값 추가
print(cabinet)
del cabinet["A-3"] # key 'A-3'에 해당하는 값 삭제
print(cabinet)

print(cabinet.keys()) # key만 출력
print(cabinet.values()) # value만 출력
print(cabinet.items()) # key와 value 한 쌍으로 출력
cabinet.clear() # 값 전체 삭제
print(cabinet)
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. 튜플 / # ()소괄호 사용
menu = ("돈가스", "치즈돈가스") # 튜플은 리스트와 비슷하지만 / 값을 변경, 추가, 삭제가 불가능하다
print(menu[0])

name = "피글렛" # 변수로 정의했을 때 / 튜플을 사용하는 이유 간편함
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김태희", 22, "남자") 
print(name, age, hobby)

(departure, arrival) = ("김포", "제주")
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival)
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 세트 = 집합 / # 세트는 {} 중괄호 사용 / 딕셔너리와 헷갈리지 않기 / 중복을 허용하지 않음
jave = {"푸", "피글렛", "티거"}
python = set(["푸", "이요르"]) # 2가지 표현법

print(jave & python)
print(jave.intersection(python)) # 교집합
print(jave | python) 
print(jave.union(python)) # 합집합 / 순서가 매번 바뀜
print(jave - python)
print(jave.difference(python)) # 차집합

python.add("피글렛") # 추가
print(python)

jave.remove("피글렛") # 제거
print(jave)
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. 자료구조 변환 // 리스트 = list []대괄호 , 튜플 = tuple ()소괄호 , 세트 = set {}중괄호
menu = {"커피", "우유", "치즈"} # 현재 세트형태
menu = list(menu) # 리스트로 변환
print(menu, type(menu))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#실습문제
from random import *

lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst) # 리스트를 섞음
print(lst)
print(sample(lst, 3)) # 랜덤으로 하나의 숫자를 뽑는다 / 중복이 없기 때문에 리스트의 숫자보다 많을 수 없다
print()

#답지
from random import * # shuffle과 sample을 사용하기에 random 모듈을 사용한다

id = list(range(1, 21)) # range를 사용해서 1부터 20까지의 숫자를 나열 / 그 후 리스트로 자료 변환
shuffle(id) # id를 섞음
winners = sample(id, 4) # 랜덤으로 4명을 선별
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # 뽑는 사람들 중 0번째 인덱스 출력
print("커피 당첨자 : {0}".format(winners[1:])) # 나머지 인덱스들 출력
print("-- 축하합니다! --")
print()

#나의 생각 but 풀지 못함...
from random import *

id = list(range(1, 21))
shuffle(id)
chicken_winners = sample(id, 1)
remain_id = set(id) - set(chicken_winners) # 세트의 차집합을 통해 치킨 우승자를 제외시킴
coffee_winners = sample(list(remain_id), 3)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken_winners)) 
print("커피 당첨자 : {0}".format(coffee_winners))  
print("-- 축하합니다! --")
print()

#셀프체크
a_list = ["자료구조", "알고리즘", "자료구조", "운영체제"]
a_set = set(a_list) # 세트로 바꿔 중복을 없앤다 / 세트의 특징으로 인해 순서가 바뀜
a_list = list(a_set) 
print("신청한 과목은 다음과 같습니다.")
print(a_list) # 다시 리스트로 변환 후 출력