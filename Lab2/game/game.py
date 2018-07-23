# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine
import time 

# global variables to keep track of score, player, and leaderboard
moves = int(0)
name = ""
leaderboard = int(0)
difficultyl= ""

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	global difficultyl
	score = Score(name, moves)
	print ("\nGame Over...?")

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves
		print ("Beware \n"
		"\n"
		" ██▓ ███▄    █   ██████  ▄▄▄       ███▄    █  ██▓▄▄▄█████▓▓██   ██▓\n"
		"▓██▒ ██ ▀█   █ ▒██    ▒ ▒████▄     ██ ▀█   █ ▓██▒▓  ██▒ ▓▒ ▒██  ██▒\n"
		"▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░  ▒██ ██░\n"
		"░██░▓██▒  ▐▌██▒  ▒   ██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░ ▓██▓ ░   ░ ▐██▓░\n"
		"░██░▒██░   ▓██░▒██████▒▒ ▓█   ▓██▒▒██░   ▓██░░██░  ▒██▒ ░   ░ ██▒▓░\n"
		"░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓    ▒ ░░      ██▒▒▒ \n"
		" ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░    ░     ▓██ ░▒░ \n"
		" ▒ ░   ░   ░ ░ ░  ░  ░    ░   ▒      ░   ░ ░  ▒ ░  ░       ▒ ▒ ░░  \n" 
		" ░           ░       ░        ░  ░         ░  ░            ░ ░     \n"    
		"											   ░ ░                  \n" 
		"														    The Game\n")
		time.sleep (4)
		print ("Welcome to The Game! To quit enter :q at any time. Be careful to not lose your mind...")
		time.sleep (3)
		name = input("\n Who is so unlucky to end up traped in Radcliffe Asylym. Enter your name. > ")
		if (name == ':q'):
			exit(1)
		difficultyl = str(input ("How much do you wish to suffer? (Difficulty Level) (easy, hard): "))
		if difficultyl == "easy" or difficultyl == "hard":
			break
		else: 
			print ("Incorrect Input, Please Choose a Provided Level.")
	a_map = Map('lobby') 
	a_game = Engine(a_map, difficultyl)
	moves = a_game.play()
	game_over(a_game.won())

play_game()

def test_game():
	test_playgame = game_over()
	test_playgame2 = play_game()
test_game()