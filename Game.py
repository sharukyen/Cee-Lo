"""
Program description: Cee-lo game
"""

import random


def main():
    user_name = "player"  # Add your username here
    player_wins = 0
    computer_wins = 0
    draws = 0
    player_selection = 1
    display_banner(user_name)
    while player_selection != 0:
        print()
        display_menu()
        player_selection = get_user_input()
        if player_selection == 1:
            player_roll = get_valid_roll()
            computer_roll = get_valid_roll()
            player_score = get_score(player_roll)
            computer_score = get_score(computer_roll)
            print()
            print_separator()
            print_roll("Player", player_roll, player_score)
            print_roll("Computer", computer_roll, computer_score)
            if player_score > computer_score:
                print("Player has won!")
                player_wins += 1
            elif player_score < computer_score:
                print("Computer has won!")
                computer_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            print("Player wins:", player_wins, "Computer wins:", computer_wins, "Draws:", draws)
            print_separator()
    print()
    print_separator()
    print_player_stats(player_wins, computer_wins, draws)
    print_separator()



def display_banner(user_name):
    star = "*" * (len(user_name) + len("Cee-lo Game by "))
    user = user_name
    game = "Cee-lo Game by "
    full = print(star), print(game + user), print(star)

    return full


def display_menu():
    print("Please make a selection:")
    print("Enter 1 to play a round of Cee-lo \nEnter 0 to exit")
    return


def get_user_input():
    prompt = "Enter your selection: "
    user_input = input(prompt)
    while int(user_input) > 1 or int(user_input) < 0:
        print("Make a valid selection! ")
        user_input = input(prompt)
    return int(user_input)


def print_separator():
    cross = "*" * 46
    print(cross)


def roll_three_dice():
    first = random.randrange(1, 7)
    second = random.randrange(1, 7)
    third = random.randrange(1, 7)
    total = str(first) + str(second) + str(third)
    return total


def is_456(dice_str):
    if (dice_str == "456" or dice_str == "465" or dice_str == "564"
            or dice_str == "546" or dice_str == "645" or dice_str == "654"):
        return True
    else:
        return False


def is_123(dice_str):
    if (dice_str == "123" or dice_str == "132" or dice_str == "231"
            or dice_str == "213" or dice_str == "312" or dice_str == "321"):
        return True
    else:
        return False


def is_trip(dice_str):
    if (dice_str == "111" or dice_str == "222" or dice_str == "333"
            or dice_str == "444" or dice_str == "555" or dice_str == "666"):
        return True
    else:
        return False


def is_point(dice_str):
    first = dice_str[0]
    second = dice_str[1]
    third = dice_str[2]
    if (first == second == third):
        return False
    elif (first == second or first == third or second == third and first != second and third):
        return True
    else:
        return False


def is_valid_roll(dice_str):
    if (is_123(dice_str) or is_point(dice_str) or is_456(dice_str) or is_trip(dice_str)) == True:
        return True
    else:
        return False


def get_valid_roll():
    a = roll_three_dice()
    while is_valid_roll(a) == False:
        a = roll_three_dice()
    return a


def type_of_roll(dice_str, player):
    if is_trip(dice_str) == True:
        dice_str = "TRIP"
    elif is_point(dice_str) == True:
        dice_str = "POINT"
    elif is_123(dice_str) == True:
        dice_str = "123"
    elif is_456(dice_str) == True:
        dice_str = "456"
    if (dice_str == "TRIP" or dice_str == "POINT"
            or dice_str == "123" or dice_str == "456"):
        return player + " has rolled a " + dice_str
    else:
        return


def get_point_score(dice_str):
    first = dice_str[0]
    second = dice_str[1]
    third = dice_str[2]
    if first == third != second:
        return int(second) + 10
    elif first == second != third:
        return 10 + int(third)
    elif first != second == third:
        return 10 + int(first)


def get_trip_score(dice_str):
    first = dice_str[0]
    second = dice_str[1]
    third = dice_str[2]
    if first == second == third:
        return 20 + int(first)


def get_score(dice_str):
    if is_123(dice_str) == True:
        return 0
    if is_456(dice_str) == True:
        return 30
    if is_point(dice_str) == True:
        return get_point_score(dice_str)
    if is_trip(dice_str) == True:
        return get_trip_score(dice_str)


def print_roll(player_name, player_roll, player_score):
    print(player_name, "has rolled:", player_roll)
    final = str(type_of_roll(player_roll, player_name))
    print("(" + final + " for a score of " + str(player_score) + ")")


def print_player_stats(player_wins, computer_wins, draws):
    print("Player wins:", str(player_wins))
    total = player_wins + computer_wins + draws
    if total == 0:
        print("Win percentage: 0.0%")
    else:
        percentage = round((player_wins / total) * 100, 1)
        print("Win percentage:", str(percentage) + "%")


main()
