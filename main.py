from art import logo, vs
from game_data import data
import random

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
    return f"{name}, a {description}, from {country}", follower_count


def plyerA():
    plyer_des, followers = random_data()
    return plyer_des, followers


def plyerB():
    plyer_des, followers = random_data()
    return plyer_des, followers


player_desA, followersA = plyerA()
print(player_desA)

print(vs)

player_desB, followersB = plyerB()
print(player_desB)


score = 0
log = input("\nWho has more followers? Type 'A' or 'B': ").lower()
if log == "a":
    if followersA > followersB:
        score += 1
        print(f"Your score is {score}")
    elif followersA < followersB:
        print("You lose")
        print(f"Your score is {score}")
elif log == "b":
    if followersB > followersA:
        score += 1
        print(f"Your score is {score}")
    elif followersB < followersA:
        print("You lose")
        print(f"Your score is {score}")



# Todo: Try some test to get the data from the dictionary


# Todo: Try to get the data from a function that take it randomly

# Todo: get the data form the data module
# Todo: import the random module to choose different data
# Todo: Try to compare the first one A with the second one with followers dat

# Todo: Ask the user to choose between A and B
# Todo: If the user has chosen the right choice the score rise
# Todo: after get a right choice compare the right with other one
# Todo: make sure the one you choose to remove it form the list

# Todo: Show the details about every one you choose
