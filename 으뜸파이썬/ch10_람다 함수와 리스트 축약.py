# 10.1 람다 함수 = return문도 없고 이름도 없는 간략화된 함수 / 주로 재사용하지 않음 (1회성)
add = lambda x, y: x + y
print("100과 200의 합 :", add(100, 200))

print("100과 200의 합 :", (lambda x, y: x + y)(100, 200)) # 더 간략히 / 그냥 100+200하면 되서 잘 사용하지는 않음
print()
#-------------------------------------------------------------------
# 10.2 필터 함수: 반복 가능한 요소들을 함수에 넣어 그 리턴 값이 참인 것만 묶어서 반환
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False
    
ages = [34, 39, 20, 18, 13, 54]
print("성년 리스트 :")
for a in filter(adult_func, ages):
    print(a, end = " ")

# 람다 함수를 이용한
ages = [34, 39, 20, 18, 13, 54]
adult_ages = list(filter(lambda x: x >= 19, ages))
print("성년 리스트 :", adult_ages)
print()
#-------------------------------------------------------------------
# 10.3 맵 함수: 반복 가능한 자료형 + 각 요소들에 지정된 매핑 함수를 적용 > 반복 가능한 자료형을 반환
def square(x):
    return x ** 2

a = [1, 2, 3, 4, 5, 6, 7]
square_a = list(map(square, a))
print(square_a)

# 람다, 맵 함수를 사용
a = [1, 2, 3, 4, 5, 6, 7]
square_b = list(map(lambda x: x**2, a))
print(square_b)
print()
#-------------------------------------------------------------------
# 10.4 리듀스 함수: 반복가능 객체의 항목 + 주어진 함수로 연산을 수행 > 하나의 값을 얻는데 사용
from functools import reduce # 리듀스가 포함된 모듈

a = [1, 2, 3, 4]
n = reduce(lambda x, y: x + y, a) # ((1 + 2) + 3) + 4 = 10
print(n)
print()
#-------------------------------------------------------------------
# 10.5 리스트와 축약 표현 / [{표현식} for {변수} in {반복자/연속열} if {조건 표현식}] 문법
a = [x ** 2 for x in range(1, 8)] # 리스트 축약 표현식 (if {조건 표현식} 생략됨)
print(a)

st = "Hello World"
s_list = [x.upper() for x in st]
print(s_list)

# if {조건 표현식}
ages = [34, 39, 20, 18, 13, 54]
print("성년 리스트 :", [x for x in ages if x >= 19])

# 이중 for 루프
product_xy = [x * y for x in [1, 2, 3] for y in [2, 4, 6]]
print(product_xy)
print()
#-------------------------------------------------------------------
# (심화) 10.6 반복자
# 반복자 객체는 __next__()메소드를 가지고 있어 객체의 다음 항목을 반환하는 기능을 가짐
# 리스트, 딕셔너리, 집합, 파일, range등 반복가능 자료형(객체)은 iter()함수를 통해 > 반복자 객체로
l = [10, 20, 30]
l_iter = iter(l)
print(type(l_iter))

try:
    l = [10, 20, 30]
    iterator = iter(l)
except TypeError:
    print("list는 iterable 객체가 아닙니다.")
else:
    print("list는 iterable 객체입니다.")

try:
    t = ("홍길동", 22, 79.7)
    iterator = iter(t)
except TypeError:
    print("tuple은 iterable 객체가 아닙니다.")
else:
    print("tuple은 iterable 객체입니다.")

try:
    n = 100
    iterator = iter(n)
except TypeError:
    print("n은 iterable 객체가 아닙니다.")
else:
    print("n은 iterable 객체입니다.")
# next()함수와 __next__()메소드 사용 가능 / 반복자 객체가 되었기에
print(next(l_iter))
print(l_iter.__next__())
print(next(l_iter)) # 출력할 다음이 없으면 오류 발생
print()
#-------------------------------------------------------------------
# (심화) 10.7 반복자 클래스의 정의
class OddCounter:
    def __init__(self, n = 1):
        self.n = n
    
    def __iter__(self): # 객체 자신을 반환하는 __iter()__메소드
        return self
    
    def __next__(self): # 루프가 돌 때마다 지정된 값을 반환하는 __next()__메소드
        if self.n < 20:
            t = self.n
            self.n += 2
            return t
        raise StopIteration # 조건을 만족하지 않으면 raise함
    
my_counter = OddCounter()
print(next(my_counter)) # next()함수나
print(my_counter.__next__()) # __next()__메소드 사용으로 반복자임을 확인
for x in my_counter: # 매번 루프를 돌 때마다 조건 검사를 하는 번거로움 %발생%
    #if x < 20: 
        #break
    print(x, end = " ") # __next__()안에 if, raise를 넣어줌으로 번거로움 해소
print() # end = " "때문에 커서가 값 뒤에 있어 2개를 써야 한칸이 띄어진 걸로 보임
print()
#-------------------------------------------------------------------
# 10.8 반복가능 객채를 위한 내장함수
# all() 모두 참이면 참
# any() 하나라도 참이면 참
# bool() 값을 부울 값으로 변환 / 항목 유무를 True와 False로 알려줌
# spilt(".") .을 기준으로 구분 / join(".") .을 기준으로 연결
#-------------------------------------------------------------------
# (심화) 10.9 제너레이터와 yield문(반환문): 값을 필요할 때마다 생성해서 반환 / 메모리 효율적으로 사용 but 일회성
my_generator = (x for x in range(1, 4)) # 반복자를 미리 만드는 것이 아니라 필요로 할 때마다 반환 해준다는 점
for n in my_generator:
    print(n)
print(type(my_generator))

def create_gen():
    alist = range(1, 4)
    for x in alist:
        yield x # 제너레이터 반환문
    
my_generator1 = create_gen()
print(my_generator1)
for n in my_generator1:
    print(n)

for n in my_generator1: # 제너레이터는 한번 실행하면 다음번에는 아무 객체도 반환하지 않음
    print(n)