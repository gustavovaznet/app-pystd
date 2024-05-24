#IMPORTING LIBRARIES
import random

#IMPORTING FILES
from pk import *

#LISTS
NAMES = [
    "Mark", "Ashley", "Marshall", "Mike", "Joe", "Laura",
    "Patrick", "Martha", "Elizabeth", "Vince", "Alex"
]

PKS = [
    PkFire("Arcanine"),
    PkFire("Charizard"),
    PkFire("Magmar"),
    PkEletric("Pikachu"),
    PkEletric("Raichu"),
    PkWater("Squirtle"),
    PkWater("Gyarados"),
]

#CHARACTER CLASS
class Character:

    #INIT
    def __init__(self, name=None, pks=[], money=100):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.pks = pks

        self.money = money

    #STRING
    def __str__(self):
        return self.name

    #SHOW POKEMONS
    def show_pks(self):
        if self.pks:
            print("pks {}:".format(self))
            for index, pk in enumerate(self.pks):
                print("{} - {}".format(index, pk))
        else:
            print("{} there is no pokemon".format(self))

    #CHOOSE POKEMON
    def choose_pks(self):
        if self.pks:
            pk_selected = random.choice(self.pks)
            print("{} choose {}".format(self, pk_selected))
            return pk_selected
        else:
            print("ERROR: this player has no pokemon")

    #WALLET
    def show_money(self):
        print("You have $ {} in your account".format(self.money))

    def earn_money(self, quantity):
        self.money += quantity
        print("You earned $ {}".format(quantity))
        self.mostrar_money()

    #POKEMON BATTLE
    def battle(self, character):
        print("{} started the battle with {}".format(self, character))

        character.mostrar_pks()
        pk_inimigo = character.escolher_pk()

        pk = self.escolher_pk()

        if pk and pk_inimigo:
            while True:
                victory = pk.atacar(pk_inimigo)
                if victory:
                    print("{} won the battle".format(self))
                    self.ganhar_money(pk_inimigo.level * 100)
                    break

                foe_victory = pk_inimigo.atacar(pk)
                if foe_victory:
                    print("{} won the battle".format(character))
                    break
        else:
            print("This battle cannot happen")


#PLAYER CLASS
class Player(Character):
    tipo = "player"

    #CAPTURE POKEMON
    def capture(self, pk):
        self.pks.append(pk)
        print("{} captured {}!".format(self, pk))

    #CHOOSE POKEMONS
    def choose_pks(self):
        self.mostrar_pks()

        if self.pks:
            while True:
                escolha = input("Choose your pokemon: ")
                try:
                    escolha = int(escolha)
                    pk_selected = self.pks[escolha]
                    print("{} I choose you!!!".format(pk_selected))
                    return pk_selected
                except:
                    print("Invalid option")
        else:
            print("ERROR: This does not have any selected pokemon")

    #START GAME EXPLORATION
    def explore(self):
        if random.random() <= 0.3:
            pk = random.choice(PKS)
            print("A wild pokemon appeard: {}".format(pk))

            escolha = input("Do you wanna capture this pokemon? (s/n): ")
            if escolha == "s":
                if random.random() >= 0.5:
                    self.capturar(pk)
                else:
                    print("{} It ran away!!!".format(pk))
            else:
                print("Okay, good luck")
        else:
            print("This exploration failed")


#FOE CLASS
class Foe(Character):
    tipo = "foe"

    #INIT
    def __init__(self, name=None, pks=None):
        if not pks:
            random_pks = []
            for i in range(random.randint(1, 6)):
                random_pks.append(random.choice(PKS))

            super().__init__(name=name, pks=random_pks)
        else:
            super().__init__(name=name, pks=pks)
