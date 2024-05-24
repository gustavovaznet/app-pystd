#IMPORTING LIBRARIES
import random

#PK CLASS
class Pk:

    #INIT
    def __init__(self, type, level=None, name=None):
        self.type = type

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = type

        self.attack = self.level * 5
        self.life = self.level * 10

    #STRING
    def __str__(self):
        return "{}({})".format(self.name, self.level)

    #ATTACK
    def attack(self, pk):
        effective_attack = int((self.attack * random.random() * 1.3))
        pk.life -= effective_attack

        print("{} lost {} life points".format(pk, effective_attack))

        if pk.life <= 0:
            print("{} was defeated".format(pk))
            return True
        else:
            return False

#ELETRIC TYPE POKEMON
class PkEletric(Pk):
    type = "eletric"

    def attack(self, pk):
        print("{} perform thundershock attack on {}".format(self, pk))
        return super().attack(pk)

#FIRE TYPE POKEMON
class PkFire(Pk):
    type = "fire"

    def attack(self, pk):
        print("{} perform a fireball attack on {}".format(self, pk))
        return super().attack(pk)

#WATER TYPE POKEMON
class PkWater(Pk):
    type = "water"

    def attack(self, pk):
        print("{} perform a water gun attack on {}".format(self, pk))
        return super().attack(pk)
