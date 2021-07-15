# Rock , Paper , Scissors Game
from  random import randint 

player_score =0
computer_score =0

# moves for the player
moves = ("rock","paper","scissors")

while True:
    computer = moves [randint(0,2)]
    player = input("rock,paper or scissors? (or end the game)").lower()
    if player =="end the game":
          print("The game has ended")
          break
    elif player == computer:
        print("Tie")
    elif player == "rock":
        if computer == "paper":
            print("You lose!",computer , "beats",player)
            computer_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score))
        else:
            print("You win!",player ,"beats",computer) 
            player_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score))
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer,"beats",player )
            computer_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score))
        else:
            print("You win!",player,"beats",computer)
            player_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score)) 
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer,"beats",player )
            computer_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score))
        else:
            print("You win!",player,"beats",computer)
            player_score +=1
            print("computer score:" + str(computer_score) + "\n" +"player score:" + str(player_score))
    else:
        print("check your spelling")     
