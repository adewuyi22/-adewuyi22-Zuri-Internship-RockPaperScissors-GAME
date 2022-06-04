#ZURI-INTERNSHIP TASK
#CREATING A 'ROCK, PAPER, or SCISSORS' GAME

import random

while True:
	rock = "ROCK"
	paper = "PAPER"
	scissors = "SCISSORS"

	choices = ["r", "p", "s"]
	cpu = random.choice(choices)

	player = None
	print("RULE OF THE GAME: \n-----------------\n R for: Rock \n P for: Paper \n S for: Scissors")
	print("\n-------------------------\nPICK AN OPTION: ('R' 'P' 'S')")
	
	while player not in choices:
	
		#Getting input from player
		player = input("\nRock, Paper, or Scissors: ").lower()
		
		#if player != "rock" and player != "paper" and player != "scissors":
		if player not in choices: 
			print("Invalid Input! Pls try again...")
		else:
			print("-------------------------------")

		if player == cpu:
			print("CPU: ", cpu)
			print("Player: ", player)
			print("Tie!")
				
		elif player == "r":
			if cpu == "p":
				print("CPU: ", paper)
				print("Player: ", rock)
				print("You loose!")
			if cpu == "s":
				print("CPU: ", scissors)
				print("Player: ", rock)
				print("You Win!")

		elif player == "s":
			if cpu == "r":
				print("CPU: ", rock)
				print("Player: ", scissors)
				print("You loose!")
			if cpu == "p":
				print("CPU: ", paper)
				print("Player: ", scissors)
				print("You Win!")

		elif player == "p": 
			if cpu == "s":
				print("CPU: ", scissors)
				print("Player: ", paper)
				print("You loose!")
			if cpu == "p":
				print("CPU: ", paper)
				print("Player: ", paper)
				print("You Win!")

	play_again = input("\nDo you want to play again? (YES / NO)): ").lower()
	if play_again != "yes" and play_again != "y":
		print ("------\nBye! \n------")
		break
