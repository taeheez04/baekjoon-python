class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

#class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 상속 순서 변경
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 수송선
troopship = FlyableUnit()