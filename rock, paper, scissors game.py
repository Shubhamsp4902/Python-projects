import random

# while loop is used to make the value true 
while True:
    choices = ["rock", "paper", "scissors"]
    
    computer = random.choice(choices)
    player = None
    
    # while loop is here used to repeat the process until user input matches the choices list
    while player not in choices:
        player = input("rock, paper or scissors ").lower()       
     # From here coding for rules begins
    if player == computer:
         print("computer: ", computer) # this will print the choices of the computer
         print("player: ", player) # this will print the choices the user given
         print("Tie")
         
    elif player == "rock":
         if computer == "paper":
             print("computer: ", computer)
             print("player: ", player)
             print("You lost!")
         if computer == "scissors":
             print("computer: ", computer)
             print("player: ", player)
             print("You won!")
             
    elif player == "paper":
          if computer == "rock":
              print("computer: ", computer)
              print("player: ", player)
              print("You won!")
          if computer == "scissors":
              print("computer: ", computer)
              print("player", player)
              print("You lost!")
              
    elif player == "scissors":
           if computor == "paper":
               print("computer: ", computer)
               print("player:", player)
               print("You won!")
           if computer == "rock":
               print("computer: ", computer)
               print("player: ", player)
               print("You lost!")
               
      #  this code is regarding asking user if they want to play this game again         
    play_again = input("Play Again (yes/no)").lower()
    if play_again != "yes":
             break
             
print("Bye")
             