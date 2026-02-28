# 1. 게임의 코드로 배우는 클래스
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. 클래스와 객체 생성하기
class Unit: # 클래스명 대문자로 시작
    def __init__(self, name, hp, damage): # 메서드명(생성자) 언더바를 앞뒤로 각각 2개씩 // self는 객체의 인스턴스 변수 or 메서드에 접근하겠다는 의미 // 그 뒤로는 전달값
        self.name = name 
        self.hp = hp # 메서드 안에 저장한 함수(전달값을 받는 변수) = 인스턴스 변수
        self.damage = damage # 인스턴스 변수를 각각 전달값에 저장
        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

soldier1 = Unit("보병", 40, 5) # 함수를 통해 만들어진 것 = 객체 or 클래스의 인스턴스
soldier2 = Unit("보병", 40, 5) 
tank = Unit("탱크", 150, 35)
print()

# 2.2 인스턴스 변수: 메서드에 정의한 변수 / self와 함께 사용
stealth1 = Unit("전투기", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(stealth1.name, stealth1.damage)) # 안에서는 self를 사용해 인스턴스 변수 정보를 출력 // 클래스 밖에서 객체로 접근해야 함
print()

# 업그레이드하면 전투기가 은폐 가능
stealth2 = Unit("업그레이드한 전투기", 80, 5)
stealth2.cloaking = True # 외부에서 인스턴스 변수 정의, 은폐 가능

if stealth2.cloaking == True:
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.name)) # stealth1에는 cloaking이라는 인스턴스 변수를 정의하지 않아 오류 발생
print()

# 2.3 메서드
class AttackUnit: # 공격 유닛이라는 클래스 정의
    def __init__(self, name, hp, damage): # 유닛 정의 함수
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 전달받은 방향으로 공격하는 함수
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage): # damage만큼 유닛 피해를 주는 함수
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

# 화염방사병: 공격 유닛, 화염방사기를 사용함
flamethrower1 = AttackUnit("화염방사기", 50, 16)
flamethrower1.attack("5시")
flamethrower1.damaged(25)
flamethrower1.damaged(25)
print()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. 클래스 상속하기
class Unit: # 일반 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
class AttackUnit(Unit): # Unit한테 상속
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) # 부모 클래스의 생성자 호출
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

flamethrower1 = AttackUnit("화염방사기", 50, 16)
flamethrower1.attack("5시")
flamethrower1.damaged(25)
flamethrower1.damaged(25)
print()

# 3.2 다중 상속 (여러 클래스로부터 상속을 받은 것)
class Flyable: # 비행 기능
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공격과 비행을 상속받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 요격기: 공중 공격 유닛, 미사일 여러 발을 한 번에 발사
interceptor = FlyableAttackUnit("요격기", 200, 6, 5)
interceptor.fly(interceptor.name, "3시")
print()

# 3.3 메서드 오버라이딩
class Unit:
    def __init__(self, name, hp, speed): # 속도가 추가됨
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move (self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed): # 속도를 추가하므로 유닛을 상속받던 클래스도 재정의
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): # 공격을 상속받던 클래스도 재정의
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # but 공중유닛이기에 지상 이동 속도 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # Unit 클래스의 move() 메서드를 오버라이딩 (번거로움을 해소하고자 자식 클래스에 메서드를 재정의하는 행위)----------------------
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 코딩 확인을 위해
hoverbike = AttackUnit("호버 바이크", 80, 20, 10) # 호버 바이크: 지상 유닛, 기동성 좋음
spacecruiser = FlyableAttackUnit("우주 순양함", 500, 25, 3) # 우주 순양함: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음

# 만든 유닛 이동
hoverbike.move("11시") # 지상은 이동
spacecruiser.fly(spacecruiser.name, "9시") # 공중은 날아간다
spacecruiser.move("9시") # 오버라이딩을 통해 출력되는 공중 공격 유닛
print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. 동작 없이 일단 넘기기: pass
# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass
# 보급고: 건물 유닛, 1개 건물 유닛 = 8유닛
supply_depot = BuildingUnit("보급고", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    pass

game_start()
game_over()
print()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. 부모 클래스 호출하기: super()
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # 지상 이동 속도 0, 건물은 지상 이동 불가
        super().__init__(name, hp, 0) # 부모 클래스 접근, self 없이 사용
        self.location = location

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. 게임 완성
# 7. 게임 최종 리뷰 / 책 참고
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8. 실습 문제: 부동산 프로그램 만들기
class House:
    # 매물 초기화: 위치, 건물 종류, 매물 종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} 원 {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

# 1번째 매물: 강남 아파트 매매 10억 원 2010년
Building1 = House("강남", "아파트", "매매", "10억", 2010)

# 2번째 매물: 마포 오피스텔 전세 5억 원 2007년
Building2 = House("마포", "오피스텔", "전세", "5억", 2007)

# 3번째 매물: 송파 빌라 웰세 500/50만 원 2000년
Building3 = House("송파", "빌라", "월세", "500/50만", 2000)


print("총 3가지 매물이 있습니다.")
Building1.show_detail()
Building2.show_detail()
Building3.show_detail()
print()

# 정답
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# 매물들을 넣어둘 리스트 생성
houses = []
house1 = House("강남", "아파트", "매매", "10억 원", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
house3 = House("송파", "빌라", "월세", "500/50만 원 ", "2000")

# 리스트에 각각의 매물들 추가
houses.append(house1)
houses.append(house2)
houses.append(house3)

# len(houses)를 통해 갯수 출력
print("총 {0}가지 매물이 있습니다.".format(len(houses)))
for house in houses: # for 변수 in 반복대상:
    house.show_detail()
print()

# 9. 셀프 체크
class ParkingManager:
    # 주차 정보 초기화: 총 주차 가능 대수
    def __init__(self, capacity):
        self.capacity = capacity
        print("총 {0}대를 등록할 수 있습니다.".format(capacity))

    # 신규 차량 등록
    def register(self):
        if i >= 5:
            print("더 이상 등록할 수 없습니다.")
        else:
            print("차량 신규 등록 ({0}/{1})".format(i+1, self.capacity))

# 테스트 코드
manager = ParkingManager(5)
for i in range(6):
    manager.register()
print()

# 정답
class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0 # count 객체를 생성할 때 0으로 정의를 해야함
        print("총 {0}대를 등록할 수 있습니다.".format(capacity))

    def register(self):
        if self.count >= self.capacity: # 나는 5를 기준으로 했는데 capacity를 가져와 사용해야 했음
            print("더 이상 등록할 수 없습니다.")
            return
        self.count += 1 # 주차된 차량 count를 하나씩 늘린다
        print("차량 신규 등록 ({0}/{1})".format(i+1, self.capacity))

manager = ParkingManager(5)
for i in range(6):
    manager.register()