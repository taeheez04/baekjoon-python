# 9.1 객체 지향 프로그래밍 : 문제를 푸는 하나의 기법(여태까지는 절차적 프로그래밍)
# 객체 = 속성(ex: list[] / 가지고 있는 데이터)과 메소드(ex: append(), sort()등 / 할 수 있는 행동)를 가진 실체
# 현실 세계의 사물을 코드로 모델링하는 것
# 클래스(객체 설계도)들을 통해 객체 생성 > 객체의 기능을 호출 조합 > 문제 해결
# ex) datetime 모듈 안에 date, time이라는 클래스 안에 각각 속성(date = year, month / time = hour, minute)과 메소드(date = today() / time = replace())가 존재
n = 200
print(type(n)) # class int
print(id(n)) # n객체의 고유한 id 반환
print()
#-------------------------------------------------------------------
# 9.3 클래스와 객체, 인스턴스 = 클래스로부터 만들어지는 개별적인 객체 (클래스의 인스턴스 / ex: 속성은 다르지만 메소드는 같은)
#-------------------------------------------------------------------
# 9.4 클래스 정의와 인스턴스
class Cat: # 클래스 정의
    def meow(self): # 메소드 정의
        print("야옹 야옹~~~")

nabi = Cat() # Cat 클래스의 인스턴스이면서 객체인 nabi 정의 
nabi.meow()
print()
#-------------------------------------------------------------------
# 9.5 클래스 정의와 생성자: __init__() 초기화 메소드
class Cat:
    def __init__(self, name, color): # self는 클래스의 인스턴스를 지칭한다 ex: nabi, nero, mimi
        self.name = name # 인스턴스 변수 생성
        self.color = color

    def meow(self):
        print("내 이름은 {0}, 색깔은 {1}, 야옹 야옹~~".format(self.name, self.color))

nabi = Cat("나비", "검정색")
nero = Cat("네로", "흰색")
mimi = Cat("미미", "갈색")

nabi.meow()
nero.meow()
mimi.meow()
print()
#-------------------------------------------------------------------
# 9.6 문자열화 메소드
print(nabi)
print(nero)

class Cat:
    def __init__(self, name, color): 
        self.name = name 
        self.color = color

    def __str__(self):
        return "Cat(name = "+self.name+", color = "+self.color+")" # 객체의 속성을 문자열 형식으로 반환

nabi = Cat("나비", "검정색")
nero = Cat("네로", "흰색")

print(nabi)
print("nero의 정보 : {0}".format(nabi))
print()
#-------------------------------------------------------------------
# 9.7 캡슐화: 클래스의 메소드와 변수를 외부에서 함부로 조작하지 못하도록 감싸고 제한하는 기능
class Cat:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

    def __str__(self):
        return "Cat(name = "+self.name+", age = "+str(self.age)+")"

nabi = Cat("나비", 3)
print(nabi)
nabi.age = 4 # 나이 속성을 고치고 싶은 문제
nabi.age = -5 # 음수가 나오는 문제
print(nabi)
print()

class Cat:
    def __init__(self, name, age): 
        self.__name = name 
        self.__age = age
    
    def __str__(self):
        return "Cat(name = "+self.__name+", age = "+str(self.__age)+")"
    
    # 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않도록 함
    def set_age(self, age): # 세터: 값을 바꿈
        if age > 0: # 양수일 때만 할당
            self.__age = age
    
    def get_age(self): # 게터: 값을 가져옴(읽음)
        return self.__age

nabi = Cat("나비", 3)
print(nabi)
nabi.set_age(4) # age에 접근
nabi.set_age(-5)
print(nabi)
print()

# property 데코레이터를 통해 새터 게터를 사용할 수 있음(실제에서 이걸 더 많이 사용)
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value

nabi = Cat("나비", 3)
print(nabi.age)    # getter 자동 실행 → 3
nabi.age = 5        # setter 자동 실행
print(nabi.age)    # 5
nabi.age = -10     # setter가 막음, 값 변경 안됨
print()
#-------------------------------------------------------------------
# 9.8 객체의 아이덴티티 연산: is, not / 객체인지 아닌지 검사
list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b:
    print("list_a is list_b")
else:
    print("list_a is not list_b")
print("id(list_a) =", id(list_a), ", id(list_b) = ", id(list_b)) # 같은 객체가 아님
# ==, != 와 같은 비교 연산자는 속성 값을 비교
print()

a = "ABC"
b = "ABC"

if a is b: # 같은 문자열을 참조하기 때문에 True 반환
    print("a is b")
else:
    print("a is not b")
print("id(a) =", id(a), ", id(b) = ", id(b))
print()
#-------------------------------------------------------------------
# 9.9 (심화) 클래스와 특수 메소드
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # 특수메소드 사용
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self): # 벡터의 정보를 출력하는 메소드 정의
        return "({0}, {1})".format(self.x, self.y)
    
    """def add(self, other): # 더하는 메소드 정의
        return Vector2D(self.x + other.x, self.y + other.y)"""

v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

# v3 = v1.add(v2) 정의된 메소드 사용
v3 = v1 + v2 # 특수메소드로 인해 일반 연산 가능
v4 = v1 - v2
print("v1 + v2 = ", v3)
print("v1 - v2 = ", v4)
print()
#-------------------------------------------------------------------
# 9.10 클래스 변수와 __dict__
class Circle:
    PI = 3.1415 # 공유해야 할 인스턴스 변수(속성) = 클래스 변수 / 글로벌 변수처럼 선언
    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius # 인스턴스 변수(속성)

    def area(self):
        return Circle.PI * self.__radius ** 2

c1 = Circle("C1", 4) # 인스턴스(객체)
print("c1의 면적: ", c1.area())
c2 = Circle("C2", 6)
print("c2의 면적: ", c2.area())
c3 = Circle("C3", 5)
print("c3의 면적: ", c3.area())
print()

class Circle:
    PI = 3.14
    def __init__(self, name, radius):
        self.name = name
        self.__radius = radius

c1 = Circle("C1", 4)
print("c1의 속성들:", c1.__dict__)
# __dic__[key] 형식으로 value를 얻을 수 있음 (딕셔너리)
print("c1의 name 변수 값:", c1.__dict__["name"])
print("c1의 __radius 변수 값:", c1.__dict__["_Circle__radius"]) # 언더바 사용 시
#-------------------------------------------------------------------
# 9.11 객체와 참조, 할당연산의 의미
n = 100 # 100이라는 숫자 객체를 n이 참조함
m = n # m이 n을 참조하므로 m은 100이라는 숫자 객체를 참조함

n = n + 1 # n이 n+1이라는 객체를 참조하게 됨 / 그래서 100이라는 객체는 참조가 사라져 참조할 방법이 없는 객체 상태가 됨 = 가비지
# 가비지 즉, 메모리 낭비 / 이를 주기적으로 정리하는 절차를 가비지 수집이라고 한다