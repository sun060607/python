name = "마린"
hp = 40
damage = 5
print("\n{} 유닛이 생성되었습니다.".format(name))
print("채력 {0},공격력 {1} ".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("\n{} 유닛이 생성되었습니다.".format(tank_name))
print("채력 {0},공격력 {1} ".format(tank_hp, tank_damage))
def attack(name, location, damage):
    print("\n{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}".format(name, location,damage))
attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)
print()
