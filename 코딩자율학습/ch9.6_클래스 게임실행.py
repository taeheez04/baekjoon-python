# 6. 게임 완성
from random import * # random 모듈 사용

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp
        self.speed = speed
        print("{0} 유닛을 생성했습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도{2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴됐습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# 보병 유닛
class Soldier(AttackUnit): # AttackUnit 클래스 상속
    def __init__(self):
        AttackUnit.__init__(self, "보병", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도
    
    def booster(self): # 강화제 기능 메서드로 정의
        if self.hp > 10:
            self.hp -= 10 # 체력 10 소모
            print("{0} : 강화제를 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족해 기술을 사용할 수 없습니다.".format(self.name))

# 탱크 유닛
class Tank(AttackUnit): # AttackUnit 클래스 상속
    # 시지 모드: 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False # 시지 모드 개발 여부, 클래스 변수로 정의

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False # 시지 모드(해체 상태), 인스턴스 변수로 정의
    
    # 시지 모드 설정
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시지 모드가 개발되지 않았다면 바로 반환
            return
        # 현재 일반 모드일 때
        if self.siege_mode == False: # 시지 모드 여부 확인
            print("{0} : 시지 모드로 전환합니다.".format(self.name)) # 시지 모드 전환
            self.damage *= 2 # 공격력 2배 증가
            self.siege_mode = True # 시지 모드 설정
        # 현재 시지 모드일 때
        else:
            print("{0} : 시지 모드를 해체합니다.".format(self.name)) # 일반 모드 전환
            self.damage //= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시지 모드 해제

# 비행 기능
class Flyable: 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

# 전투기 유닛
class Stealth(FlyableAttackUnit): # AttackUnit 클래스 상속
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5) # 부모 클래스 생성자로 기본 정보 설정
        self.cloaked = False # 은폐 모드(해제 상태), 인스턴스 변수 정의

    def cloaking(self): # 은폐 모드를 메서드로 정의
        # 현재 은폐 모드일 때
        if self.cloaked == True:
            print("{0} : 은폐 모드를 해제합니다.".format(self.name))
            self.cloaked = False # 은폐 모드 해제
        # 현재 은폐 모드가 아닐 때
        else:
            print("{0} : 은폐 모드를 설정합니다.".format(self.name))
            self.cloaked = True # 은폐 모드 설정

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

#------------------------------------------------#
# 6.2 게임 실행하기
# 게임 시작과 유닛 생성
# 게임 시작
game_start()

# 보병 3기 생성
so1 = Soldier()
so2 = Soldier()
so3 = Soldier()

# 탱크 2기 생성
ta1 = Tank()
ta2 = Tank()

# 전투기 1기 생성
st1 = Stealth()
print()

# 유닛 일괄 관리(생성된 모든 유닛 추가)
attack_units = []
attack_units.append(so1)
attack_units.append(so2)
attack_units.append(so3)
attack_units.append(ta1)
attack_units.append(ta2)
attack_units.append(st1)

# 전군 이동과 탱크 시지 모드 개발
# 전군 이동
for unit in attack_units:
    unit.move("1시")
print()

# 탱크 시지 모드 개발
Tank.siege_developed = True
print("[알림] 탱크의 시지 모드 개발이 완료됐습니다.")
print()

# 공격 준비와 전군 공격
# 공격 모드 준비(보병: 강화제, 탱크: 시지 모드, 전투기: 은폐 모드)
for unit in attack_units:
    if isinstance(unit, Soldier): # Soldier 클래스의 인스턴스이면 강화재
        unit.booster()
    elif isinstance(unit, Tank): # Tank 클래스의 인스턴스이면 시지 모드
        unit.set_siege_mode()
    elif isinstance(unit, Stealth): # Stealth 클래스의 인스턴스이면 은폐 모드
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")
print()

# 전군 피해와 게임 종료
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 피해를 무작위로 받음 (5~20)
print()

# 게임 종료
game_over()
print()

# 7. 게임 최종 리뷰 / 책 참고