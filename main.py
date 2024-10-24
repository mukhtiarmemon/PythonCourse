import random

#the function
def get_choices():
    player_choice = input("Enter Choice (rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)    
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

#another function
def check_win(player, computer):
    print("your choice: " + player + "computer choice: " + computer)
    if player == computer:
        return "It is a tie"



def greeting():
    return "hi from the datacamp course"

response = greeting()
#print(response)

choices = get_choices()
#print(choices)

#lists
food = ["piza", "carrots", "eggs"]
dinner = random.choice(food)
