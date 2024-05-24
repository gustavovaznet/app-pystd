#IMPORTING LIBRARIES
import pickle

#FILES
from pk import *
from character import *


def choose_initial_pk(player):
    print("Hiii {}, you can now choose a Pokemon to follow you on this new journey of yours!!!".format(player))

    pikachu = PkEletric("Pikachu", level=1)
    charizard = PkFire("Charizard", level=1)
    gyarados = PkWater("Gyarados", level=1)

    print("You have 3 options: ")
    print("1 -", pikachu)
    print("2 -", charizard)
    print("3 -", gyarados)

    while True:
        choice = input("Choose your Pokemon: ")

        if choice == "1":
            player.capture(pikachu)
            break
        elif choice == "2":
            player.capture(charizard)
            break
        elif choice == "3":
            player.capture(gyarados)
            break
        else:
            print("Invalid option")


def save_game(player):
    try:
        with open("database.db", "wb") as file:
            pickle.dump(player, file)
            print("Game saved with success!!!")
    except Exception as error:
        print("Error, please try again :(")
        print(error)


def load_game():
    try:
        with open("database.db", "rb") as file:
            player = pickle.load(file)
            print("Game has been loaded successfully")
            return player
    except Exception as error:
        print("File not found")


if __name__ == "__main__":
    print('-----------------------------------------')
    print("Welcome to the Pokemon Forest Adventure 2.0 - The Best Pokemon Game")
    print('-----------------------------------------')

    player = load_game()

    if not player:
        name = input("Enter your name: ")
        player = Player(name)
        print("Hiii {}, this is the pokemon world,"
              "from now on your mission is to become a Pokemon Master!!!!".format(player))
        print("Capture as much Pokemon you can, you are gonna need them to battle against your challengers!!")
        player.show_money()

        if player.pks:
            print("I can see you've got some nice Pokemon")
            player.show_pks()
        else:
            print("Choose a Pokemon, because you still don't have one...")
            choose_initial_pk(player)

        print("Now you have a Pokemon, let's battle your challenger!")
        gary = Foe(name="Mark", pks=[PokemonAgua("gyarados", level=1)])
        player.battle(gary)
        save_game(player)

    while True:
        print("--------------------------------------")
        print("What do you wanna do?")
        print("1 - Explorer the pokemon world!!!")
        print("2 - Battle!!!")
        print("3 - Check pokephone")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "0":
            print("Farewell...")
            break
        elif choice == "1":
            player.explore()
            save_game(player)
        elif choice == "2":
            random_foe = Foe()
            player.battle(random_foe)
            save_game(player)
        elif choice == "3":
            player.show_pks()
        else:
            print("Invalid option")
