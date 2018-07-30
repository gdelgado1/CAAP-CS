# Gustavo Delgado
# Lab3 - CAAP-CS - gdelgado1

from random import randint

# global variable of chutes and ladders
# remenber to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
					8 : 15,
					12 : 2,
					14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
	a = randint(1,6)
	return a 

# makes a game (just a list) of the given dimensions
def makeGame(w,l):
	game_board = w*l
	squares = []
	for i in range(game_board):
		squares.append(i+1)
	return squares 

# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
	global chutes_ladders
	for i in chutes_ladders: 
		if i == d: 
			return True  
	return False 

# function to make and play a game
def play_game():
# This should be a list of dictionaries of each player's state 
	global chutes_ladders 
	playdict = []
	num_players = int(input("How many people are playing (up to 5)? "))
	for i in range (num_players): 
		name = input("What is a player's name? ")  
		playdict.append({'name':name,'state':1,'moves':0}) 
	makeGame(4,4)
	print ("This is the current standing; Player numbers assigned in this order: ",playdict) 
	while True:
		try: 
			style = int(input("Would you like the game to be played continously (1) or be prompted to roll (2)?  "))
			if style == 1: 
				print ("Game will be played continously until a player wins")
			if style == 2: 
				print ("Prompt to Roll! Let the Games Begin!")
		except: 
			print ("To choose a style you must input either 1 or 2!")
		else:
			break
	if style == 2:
		playing = False 
		while playing == False: 
			for p in range(num_players): 
				print("Player",p+1,"it is your turn")
				roll = input("Press ENTER to roll the die: ")
				dice = roll_die()
				print("Player",p+1,"you rolled a",dice) 
				playdict[p]['state'] += dice
				playdict[p]['moves'] += 1
				print (playdict)
				if playdict[p]['state'] in chutes_ladders:
					playdict[p]['state'] == chutes_ladders[playdict[p]['state']]
					print ("You encountered a chute/ladder")
				if playdict[p]['state'] > 16:
					playing == True
					playdict[p]['state'] == 16
					print("Player " + str(p+1) + " you are a winner!")
					print(playdict)
					return
	if style == 1: 
		playing = False 
		while playing == False:
			for p in range(num_players): 
				dice = roll_die()
				playdict[p]['state'] += dice
				playdict[p]['moves'] += 1
				if playdict[p]['state'] in chutes_ladders:
					playdict[p]['state'] == chutes_ladders[playdict[p]['state']]
				if playdict[p]['state'] > 16:
					playing == True
					playdict[p]['state'] == 16
					print("Player " + str(p+1) + " you are a winner!")
					print(playdict)
					return
play_game()

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average	
def game_simulation(sim_num):
	global chutes_ladders
	div = 0
	playdict = []
	playdict.append({'name':"CompSim",'state':1,'moves':0}) 
	for i in range(sim_num):
		playing = False
		while playing == False:
			for p in range(1): 
				dice = roll_die()
				playdict[p]['state'] += dice
				playdict[p]['moves'] += 1
				if playdict[p]['state'] in chutes_ladders:
					playdict[p]['state'] == chutes_ladders[playdict[p]['state']]
				if playdict[p]['state'] > 16:
					playing == True
					playdict[p]['state'] == 16
					return
	temp = playdict[p]['moves']
	div += temp
	return float(val)/sim_num