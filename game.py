import random
def game():
    print("Welcome to Rock Paper Scissors Game!")
    print("Rules:Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
    Choices=['rock','paper','scissors']
    while True:
        player_choice=input("Enter your choice(rock/paper/scissors):").lower()
        if player_choice=="exit":
            print("Thanks for playing the Game!")
            break
        if player_choice not in Choices:
            print("enter a valid choice")
            continue
        computer_choice=random.choice(Choices)
        print("The computer choice is:",computer_choice)
        if player_choice==computer_choice:
            print("It's tie!")
        elif (player_choice=="rock" and computer_choice=="scissors")or(player_choice=="scissors" and computer_choice=="paper")or(player_choice=="paper" and computer_choice=="rock"):
            print("You win!")
        else:
            print("You lose")
game()
        
        
