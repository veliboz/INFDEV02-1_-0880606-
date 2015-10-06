print ("Scissors cut paper, paper kills rock and rock destroys scissors\n")
player1 = raw_input("Make your choice player 1: rock, paper or scissors? ")
player2 = raw_input("Make your choice player 2: rock, paper or scissors? ")

if (player1 == "rock" and player2 == "paper"):
    print "player 2 wins"
elif (player1 == "rock" and player2 == "scissors"):
    print "player 1 wins" 
elif (player1 == "rock" and player2 == "rock"):
    print "Draw"

elif (player1 == "paper" and player2 == "rock"):
    print "Player 1 wins"
elif (player1 == "paper" and player2 == "scissors"):
    print "Player 2 wins"
elif (player1 == "paper" and player2 == "paper"):
    print "Draw"

elif (player1 == "scissors" and player2 == "rock"):
    print "Player 2 wins"
elif (player1 == "scissors" and player2 == "paper"):
    print "Player 1 wins"
elif (player1 == "scissors" and player2 == "scissors"):
    print "Draw"
else:
    print "not good"
