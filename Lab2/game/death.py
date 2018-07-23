# importing random int maker module
from random import randint
# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["Your mind just couldn't handle it.",
			"Lights out loser for all eternity.",
			"Better hope they have psychiatrists where your going.",
			"The Asylum gets us all in the end.",
			"Better luck next time.",
			"Well at least it was quick!"
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'