#!python

class monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Attackmonster(monster):
    def __init__(self, name, hp , damage):
        monster.__init__(self,name,hp)
        self.damage = damage

# 공격하는 함수
    def Mattack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [ 공 격 력 : {2} ].".format(self.name ,location,self.damage))

#공격 받는 함수
    def Mdamage(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name , damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name ,self.hp))
        if self.hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))


#영진
youngjin = Attackmonster("영진", 50 , 15)
youngjin.Mattack("5시")

youngjin.Mdamage(25)
