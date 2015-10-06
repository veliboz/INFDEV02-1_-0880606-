print ("scissors cut paper, paper kills rock, rock destroys scissors,\nrock crushes lizard, lizard poisens spock, spock smashes scissors, \nscissors decapitate lizard, lizard eats paper, paper disproves spock, \nspock vaporises rock \n")
player1 = raw_input("Make your choice player 1: rock, paper, scissors, spock or lizard? ")
player2 = raw_input("Make your choice player 2: rock, paper, scissors, spock or lizard? ")

if (player1 == "rock" and player2 == "paper"):
    print "player 2 wins"
elif (player1 == "rock" and player2 == "scissors"):
    print "player 1 wins" 
elif (player1 == "rock" and player2 == "spock"):
    print "Player 2 wins"
elif (player1 == "rock" and player2 == "lizard"):
    print "Player 1 wins"
elif (player1 == "rock" and player2 == "rock"):
    print "Draw"

elif (player1 == "paper" and player2 == "rock"):
    print "Player 1 wins"
elif (player1 == "paper" and player2 == "scissors"):
    print "Player 2 wins"
elif (player1 == "paper" and player2 == "spock"):
    print "Player 1 wins"
elif (player1 == "paper" and player2 == "lizard"):
    print "Player 2 wins"
elif (player1 == "paper" and player2 == "paper"):
    print "Draw"

elif (player1 == "scissors" and player2 == "rock"):
    print "Player 2 wins"
elif (player1 == "scissors" and player2 == "paper"):
    print "Player 2 wins"
elif (player1 == "scissors" and player2 == "spock"):
    print "Player 2 wins"
elif (player1 == "scissors" and player2 == "lizard"):
    print "Player 1 wins"
elif (player1 == "scissors" and player2 == "scissors"):
    print "Draw"

elif (player1 == "spock" and player2 == "rock"):
    print "Player 1 wins"
elif (player1 == "spock" and player2 == "paper"):
    print "Player 2 wins"
elif (player1 == "spock" and player2 == "scissors"):
    print "Player 1 wins"
elif (player1 == "spock" and player2 == "lizard"):
    print "Player 2 wins"
elif (player1 == "spock" and player2 == "spock"):
    print "Draw"

elif (player1 == "lizard" and player2 == "rock"):
    print "Player 2 wins"
elif (player1 == "lizard" and player2 == "paper"):
    print "Player 1 wins"
elif (player1 == "lizard" and player2 == "scissors"):
    print "Player 2 wins"
elif (player1 == "lizard" and player2 == "spock"):
    print "Player 1 wins"
elif (player1 == "lizard" and player2 == "lizard"):
    print "Draw"

else:
    print "not good"