def get_choices():
    player_choice = input("Enter Choice (rock, paper, scissors)")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    
    return choices

def greeting():
    return "hi from the datacamp course"

response = greeting()
print(response)

choices = get_choices()
print(choices)