from art import logo, vs
from game_data import data
import random
import os
# ! Start

# Todo: Print the logo

print(logo)
print(
    "Welcome to the Higher or Lower Game!\nChoose between two options based on the one with more followers.\n"
)


def random_data():
    dict_choice = random.choice(data)
    name = dict_choice["name"]
    description = dict_choice["description"]
    country = dict_choice["country"]
    follower_count = dict_choice["follower_count"]
    data.remove(dict_choice)
    format_data = f"{name}, a {description}, from {country}"
    return format_data, follower_count


plyerA = random_data()
description_A = plyerA[0]
followers_count_A = plyerA[1]

print(description_A)
print(followers_count_A)
print(vs)

plyerB = random_data()
description_B = plyerB[0]
followers_count_B = plyerB[1]

print(description_B)

lose = False
score = 0
while not lose:
    log = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    if log == "a":
        if followers_count_A > followers_count_B:
            score += 1
            os.system("cls")
            print(f"Your score is {score}")
            print(description_A)
            print(followers_count_A)

            print(vs)

            plyerB = random_data()
            description_B = plyerB[0]
            followers_count_B = plyerB[1]
            print(description_B)

            log = input("\nWho has more followers? Type 'A' or 'B': ").lower()
            


        elif followers_count_A < followers_count_B:
            print("You lose")
            print(f"Your score is {score}")
            lose = True

    elif log == "b":
        if followers_count_B > followers_count_A:
            score += 1
            os.system("cls")
            print(f"Your score is {score}")

            print(description_B)  
            print(followers_count_B)
            print(vs)

            plyerA = random_data()
            description_A = plyerA[0]
            followers_count_A = plyerA[1]

            print(description_A)
        elif followers_count_B < followers_count_A:
            print("You lose")
            print(f"Your score is {score}")
            lose = True


# def plyerA():
#     plyer_des, followers = random_data()
#     return plyer_des, followers


# def plyerB():
#     plyer_des, followers = random_data()
#     return plyer_des, followers


# playerA = random_data()
# print(plyerA[0])

# print(vs)

# player_desB, followersB = plyerB()
# print(player_desB)


# # Todo: Try some test to get the data from the dictionary


# # Todo: Try to get the data from a function that take it randomly

# # Todo: get the data form the data module
# # Todo: import the random module to choose different data
# # Todo: Try to compare the first one A with the second one with followers dat

# # Todo: Ask the user to choose between A and B
# # Todo: If the user has chosen the right choice the score rise
# # Todo: after get a right choice compare the right with other one
# # Todo: make sure the one you choose to remove it form the list

# # Todo: Show the details about every one you choose
