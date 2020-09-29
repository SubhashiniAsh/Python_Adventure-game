import time
import random
weapon_list = ['Asgard sword', 'Soul stone', 'Aether']
creature_list = ['Loki', 'Thanos', 'Red Skull']
items = []


def print_pause(string, time_wait):
    print(string)
    time.sleep(time_wait)


def intro():
    print_pause("Welcome to the Adventure Game!", 2)
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.", 2)
    print_pause("Rumor has it that a creature is somewhere around here,"
                " and has been terrifying the nearby village.\n"
                "...", 2)


def main():
    weapon = random.choice(weapon_list)
    creature = random.choice(creature_list)
    items = []

    def lost():
        print_pause("You lost the game because you don't possess the magical"
                    " weapon!", 2)
        print_pause("GAME OVER", 2)
        play_again()

    def win():
        print_pause("You are fighting now", 2)
        print_pause("You won!", 2)
        print_pause("GAME OVER", 2)
        play_again()

    def select_way():
        print_pause("Enter 1 to knock on the door of the house.", 2)
        print_pause("Enter 2 to peek into the cave.", 2)
        print_pause("What would you like to do?", 1)
        way = input("(Please enter 1 or 2).\n")
        if way == '1':
            print_pause(creature + " opens the door!", 2)
            print_pause(creature + " scowls at you", 2)
            while True:
                response = input("Do you want to fight with " + creature +
                                 " Please enter 'yes' or 'no'\n")
                if response.lower() == "no":
                    print_pause("You walk back to the field", 2)
                    select_way()
                elif response.lower() == "yes":
                    if items:
                        win()
                    if not items:
                        lost()
                else:
                    print_pause("That's a wrong input, you are back to the"
                                " field", 2)
        elif way == '2':
            print_pause("You peek into the cave", 4)
            if weapon in items:
                print_pause("You have already collected the " + weapon, 2)
                print_pause("You walk back to the field", 2)
                select_way()
            else:
                print_pause("It is very dark and you follow your instinct into"
                            " the cave", 2)
                print_pause("You hear eerie sounds", 3)
                print_pause("You find a shiny object behind a huge rock", 2)
                print_pause("You go closer and pick it up.", 2)
                print_pause("It is " + weapon, 2)
                print_pause("Then you carefully exit the cave", 2)
                print_pause("You walk back to the field", 2)
                items.append(weapon)
                select_way()
        else:
            select_way()
    select_way()


def play_game():
    intro()
    main()
    play_again()


def play_again():
    game_again = input("Would you like to play again? 'yes' or 'no'\n").lower()
    if game_again == 'yes':
        play_game()
    elif game_again == 'no':
        print_pause("Thank you, Goodbye", 2)
        exit()
    else:
        print_pause("Incorrect input\n", 2)
        play_again()

if __name__ == "__main__":
    play_game()
