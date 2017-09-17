from random import randint
from termcolor import colored

class Player:
	def __init__(self):
		self.score = 0
		self.choice = None

human = Player()
computer = Player()

def game(player1, player2):
	choices = ["rock", "paper", "scissors"]

	computerChoice = randint(0, 2)
	player2.choice = choices[computerChoice]

	while (player1.choice == None):
		print("********************************************")
		humanChoice = raw_input(colored("What is your decision: Rock, Paper or Scissors: ",'green')).lower()
		if (humanChoice not in choices):
			print(colored("Please spell or enter a correct option.\n",'red'))
		else:
			player1.choice = humanChoice

	print "Human chooses: " + player1.choice 
	print "Computer chooses: " + player2.choice + "\n"

	result = whoWon(player1, player2)
	if (result == 0):
		print(colored("Draw",'green',attrs=['bold']))
	elif (result == 1):
		print(colored("Human wins",'green',attrs=['bold']))
		player1.score += 1
	elif (result == 2):
		print(colored("Computer wins",'green',attrs=['bold']))
		player2.score += 1
	else:
		print(colored("Error: No result applicable to the match",'red',attrs=['bold']))

	print (colored("Player: " + str(player1.score) + " / Computer: " + str(player2.score) + "\n",'magenta',attrs=['bold']))

	player1.choice = None

# return 0 if draw.
# return 1 if player1 won, 
# return 2 if player2 won, 
def whoWon(player1, player2):
	if (player1.choice == player2.choice):
		return 0
	elif (player1.choice == "rock") and (player2.choice == "scissors"):
		return 1
	elif (player1.choice == "rock") and (player2.choice == "paper"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "scissors"):
		return 2
	elif (player1.choice == "paper") and (player2.choice == "rock"):
		return 1
	elif (player1.choice == "scissors") and (player2.choice == "rock"):
		return 2
	elif (player1.choice == "scissors") and (player2.choice == "paper"):
		return 1
	else:
		return 3


playAgain = True

while (playAgain == True):
	game(human, computer)

	request = raw_input(colored("Would you like to play again? (Y/N) : ",'red',attrs=['bold'])).lower()
	if (request == 'y'):
		playAgain = True
		print(colored("Playing again\n",'green',attrs=['bold']))
	elif (request == 'n'):
		playAgain = False
		print(colored("Let's stop\n",'white',attrs=['bold']))
	else:
		print(colored("Didn't understand either Y or N, playing again by default.\n",'red',attrs=['bold']))
	

