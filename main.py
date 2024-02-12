from art import logo, vs
from game_data import data
import random
import os
import time

# Print the logo
print(logo)
print("Welcome to the Higher or Lower Game! 🚀 Choose between two options based on the one with more followers.\n")


def random_data():
    dict_choice = random.choice(data)
    name = dict_choice["name"]
    description = dict_choice["description"]
    country = dict_choice["country"]
    follower_count = dict_choice["follower_count"]
    data.remove(dict_choice)
    format_data = f"{name}, a {description}, from {country}"
    return format_data, follower_count


def print_with_delay(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


playerA = random_data()
description_A = playerA[0]
followers_count_A = playerA[1]

print_with_delay(description_A + "\n")
print_with_delay(str(followers_count_A) + "\n")
print_with_delay(vs + "\n")

playerB = random_data()
description_B = playerB[0]
followers_count_B = playerB[1]

print_with_delay(description_B + "\n")

lose = False
score = 0
while not lose:
    log = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    if log == "a":
        if followers_count_A > followers_count_B:
            score += 1
            os.system("cls")
            print(f"Your score is {score}! 🎉")
            print_with_delay(description_A + "\n")
            print_with_delay(str(followers_count_A) + "\n")
            print_with_delay(vs + "\n")
            time.sleep(0.5)
            playerB = random_data()
            description_B = playerB[0]
            followers_count_B = playerB[1]
            print_with_delay(description_B + "\n")
        elif followers_count_A < followers_count_B:
            print_with_delay("You lose 😞 Better luck next time!\n")
            print_with_delay(f"Your final score is {score}!\n")
            lose = True
    elif log == "b":
        if followers_count_B > followers_count_A:
            score += 1
            os.system("cls")
            print(f"Your score is {score}! 🎉")
            print_with_delay(description_B + "\n")
            print_with_delay(str(followers_count_B) + "\n")
            print_with_delay(vs + "\n")
            time.sleep(0.5)
            playerA = random_data()
            description_A = playerA[0]
            followers_count_A = playerA[1]
            print_with_delay(description_A + "\n")
        elif followers_count_B < followers_count_A:
            print_with_delay("You lose 😞 Better luck next time!\n")
            print_with_delay(f"Your final score is {score}!\n")
            lose = True