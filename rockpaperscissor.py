import random
def generate_random():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def check_winner(user_input, computer_input):
    if user_input == computer_input:
        return "It's a tie"
    elif (
        (user_input == "scissors" and computer_input == "paper") or
        (user_input == "paper" and computer_input == "rock") or
        (user_input == "rock" and computer_input == "scissors")
    ):
        return "You won!"
    else:
        return "Computer won"

print("Welcome to Rock, Paper, Scissors Game")

user_input = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
computer_input = generate_random()

print("You chose:", user_input)
print("Computer chose:", computer_input)

winner = check_winner(user_input, computer_input)

print("The winner is:", winner)


