# imports random module form library
from random import randint
import time

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class lobby(Scene):
	name = 'lobby'
	def enter(self):
		print ("You awake...")
		time.sleep (3)
		print ("The room is vast and decreipt, smelling faintly of copper.")
		print ("You pull yourself up and brush yourself off, noticing the red stains on your clothes")
		print ("There is some sort of conceirge desk with a metal grill surrounding it")
		print ("You approach it, feeling your body groan and notice the sign dangling beneath it")
		print ("It reads 'Welcome to Radcliffe Asylum, I am on break' with the word 'permanently' written in a familiar red stain.")
		print ("Beneath the grill is a brass call bell, rusted with age. You wonder if you should push it.")
		return self.action()
			
	def action(self):
		print ("What will you do? (Pick a number 1-3) ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try: 
			choice = int(choice)
		except ValueError:
			print("That's not an int choice!")
			return self.exit_scene(self.name)

		if int(choice) == 2:
			print ("You ring the bell and suddenly the floor opens up beneath you and you fall into a cavernous abyss while laughter rings out.")
			return self.exit_scene('death') 
		elif int(choice) == 1:
			print ("You ring the bell and a heavy lock tumbles to the ground on the door to your right. You exit the lobby of the asylum by the steel door unsure of what's to come.")
			return self.exit_scene('TheCorridor') 
		elif int(choice) == 3:
			print ("You hesitate over the bell. You choose not to push it as you are unsure of what horrors it may summon.")
			print ("You spot a set of stairs leading up from the lobby, hiddn in the gloom by a statue.")
			return self.exit_scene('TheStaircase') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class TheCorridor(Scene):
	name = 'The_Corridor'	
	def enter(self):
		print ("The corridor is lined on both sides by massive red doors, each with a single window composed of bars. The floor is covered in leaves and stains long since faded to brown.")
		print ("You wonder for the first time how you got here as your eyes catch the shape of a light switch next to a notice board.")
		time.sleep (1)
		print ("Suddenly a screech rings out.")
		time.sleep (2)
		print ("You hesitate to step forward but suddenly the steel door slams shut behind you, throwing you into darkness.")
		time.sleep (3)
		print ("You take a moment to catch your breath, your hands feeling along the wall for the light swtich you noticed moments ago. You hear a scurrying down the hall... ")
		
	def action(self):
		print ("Do you flip the switch or better stay in the dark to remain hidden? (y or n):  ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)

		if str(choice) == "y":
				print ("You decide to flip the switch. The lights flicker on and the corridor is as it was. You can see to the very end of the corridor and there is nothing but a moldy wheelchair cast on its side.")
				return self.exit_scene('TheCorridor2') 
		elif str(choice) == "n":
				print ("You do not flip the switch, rather you remain in the dark. The darkness and foreboding and the scurrying becomes louder. Suddenly your legs are seized out from under you and you fall to the floor. You are pulled into one of the rooms behind the red door. Your screams ring out.")
				return self.exit_scene('death') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)
	
	def exit_scene(self, outcome):
		return outcome

	
class TheCorridor2 (Scene): 
	
	name = 'The_Corridor2'
	def enter(self):
		print ("You turn to the notice board by the light switch. Your eyes reead the following:")
		print ("'Radcliffe Asylum shut down! Patients under emergency evacuation due to two serial killers being the on loose. All Radcliffe employees to report to the lobby immediately - 1969'")
		time.sleep (2)
		print ("Are you an employee? You ponder this as you wander futher down the hall when suddenly a syringe flys throw the air aiming for your neck")
		return self.action 
	def action(self):
		print ("Will you survive? (Pick a number 1-3)")
		choice = input(">")
		if choice == ':q':
			return self.exit_scene(choice)
		try: 
			choice = int(choice)
		except ValueError:
			print("That's not an int choice!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You try to dodge right but the syringe plunges into your cheek. As you are overwhelmed with you pain, a man in a labcoat and surgical appears and as your eyes begin to droop, he lowers a rusty scalpel to your face")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("You dodge to the left, hitting the wall and falling to the ground. Althought the first syringe strikes the right wall harmlessly, a second syringe wizzes towards you, hitting you DEAD-center in the eye")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("You throw yourself to the ground and notice a small rotted hole in the wall. You crawl into the hole just as a second syringe strikes the wall.")
			return self.exit_scene('TheVents') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)
	
	def exit_scene(self, outcome):
		return outcome

		
class TheStaircase(Scene):
	
	name ='The_Staircase'
	
	def enter(self):   
		print ("The stairs creek as you make your way up them. A large bay window lets in a brief flash of lightning and you release that there is no noise from the outside. The glass must be 6 inches thick.")
		print ("You reach the middle set of the stairs when you smell something rancid coating the stairs.")
		print ("You peer closer at the stairs and notice they are coated with something vaguely resembling entrails. Your eyes follow their connections to the head of the stairs where you see a creature lumbering out of the gloom, made of entrails, and heading straight for YOU!") 
		return self.action 
	def action(self):
		print ("Do you survive the creature? (Type B to head back, C to charge forward, or I to hide) ")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)

		if str(choice) == "B" or "b":
				print ("You attempt to retreat down the stairs but when you attempt to grab hold of the bannister, your hand grabs an entrail and you lose balance. You fall down the stairs and break your neck")
				return self.exit_scene('death') 
		elif str(choice) == "C" or "c":
				print ("You charge forward, dancing around the creature who release a yelp, seemingly done in rage. You make it to the upper level, the infirmary")
				return self.exit_scene('infirmary') 
		elif str(choice) == "I" or "i":
				print ("You attempt to hide, getting lower on the stairs. But you realize that the action is futile. As you approach the creature you notice something far worse. It is in fact not a creature, its a little girl with her entrails dangling about, all twisted and knotted and stabled to herself. She appears to be nearing death and lets out a yelp of pain. You lean over and close her eyes. Then you make your way to where the stairs lead, the infirmary.")
				return self.exit_scene('infirmary') 
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
		

	def exit_scene(self, outcome):
		return outcome

class TheVent(Scene):
	
	name = 'The_Vent'

	def enter(self):
		print ("You have fled into the vent. The tight crawl space inspire claustorphobia but when you look briefly behind, you notice a masked figure brnadishing a syringe at the entrance to the hole!")
		time.sleep (3)
		print ("You continue to crawl farther into the vent in attempt to avoid the masked man and his manic syringes. You are nearing a nexus in the vents. The nexus leads off into 4 seperate vents.")
		return self.action 
	
	def action(self):
		print ("There's 4 vents, which one do you take?")
		good_vent = randint(1,5)
		guess = input("[vent #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
			guess = int(guess)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)
		   
		if int(guess) != good_pod:
			print ("You crawl into vent", guess,  "when it begins to shudder and shake. The masked man watches you with wide eyes as the vent crashes.")
			return self.exit_scene('death')
		else:
			print ("You crawl into vent",guess,"and find yourself in brightly lit room.")
			return self.exit_scene('infirmary')

	def exit_scene(self, outcome):
				   return outcome 
				   
class TheInfirmary(Scene):
	
	name = 'The_Infirmary'

	def enter(self):
		print ("You enter the brightly lit infirmary. The room compared to the rest of the asylum is clean and new. There is an overpowering stench of rubbing alcohol and air freshner.")
		print ("There are sheets laid out on the cots that line the infirmary, surrounded by a variety of medical equipment. You can discern the shapes of what appear to be bodies.")
		time.sleep (3)
		print ("Pulling a sheet back, you uncover an emaciated corpse, the body almost distorted beyond recognition. Yet the shape of it appears familiar...")
		time.sleep (5)
		print ("You're overcome with revulsion and suddenly your head begins to pound. Then you're eyes catch on a door with a padlock. The padlock itself appears very familiar.")
		return self.action 
	def action(self):
		print ("There's a padlock on the door. Do you really know the code?")
		code = [randint(0,9), randint(0,9), randint(0,9)]
		guesses = 0
		# loop to check three random integers, one at a time
		for i in range(3):
			print ("Enter digit %d." % (i+1))
			guess = input("[padlock]> ")
			if guess == ':q':
				return self.exit_scene(guess)
			try:
			   guess = int(guess)
			except ValueError:
			   print("That's not an int!")
			   return self.exit_scene(self.name)
			while int(guess) != code[i] and guesses <10:
				print ("Nope")
				guesses += 1
				guess =input("[padlock]> ")
				if guess == ':q':
					return self.exit_scene(guess)
				try:
				   guess = int(guess)
				except ValueError:
				   print("That's not an int!")
				   guess = -1
		
		if guesses < 10:
			print ("The padlock drops to the floor and you yank open the door, it screams on its hinges.")
			return self.exit_scene('Exit_Den')
		else:
			print ("You cannot open the lock and as you attempt the code, the dial breaks off. You turn around in frustration and spy the man in a mask exiting the vent")
			print ("A scalpel and some syringe shooter in hand, he nears you. You feel warm below your waist and the world goes black.")
			return self.exit_scene('death')

	def exit_scene(self, outcome):
	   return outcome 
				   
class ExitDen(Scene):
	
	name = 'Exit_Den'

	def enter(self):
		print ("The room is in complete contrast to the infirmary. It is dingy and decreipt, exposed to the outer elements by a hole in the roof.")
		print ("There is a matress laid on the ground surrounding by a variety of medical implements. The difference here is that these can cut. You grab one off the floor")
		time.sleep (3)
		print ("Behind the mattress, leans a full-length mirror. The mirror althought covered in hairline cracks revelas that you're dressed in a set of blue scrubs coated with blood...")
		time.sleep (5)
		print ("As you near the mirror, you note the masked man is approaching but you are no longer overcome with fear.")
		print ("He removes his mask and suddenly you understand why. Your stalker in fact looks exactly like you.")
		time.sleep (5)
		print ("Brother? The man approaches you a hug. You finally remember all the fun you two had in the Asylum.")
		return self.action 
	
	def action(self):
		print ("You're a killer. But so is he? Do you accept him? (y or n)")
		choice = input(">")
		if choice == ':q':
			return self.exit_scene(choice)

		if str(choice) == "y":
				print ("You accept his embrace, and savor the fresh blood coating his arms. His is your brother and this is your playground. Nevermind that he pushed you down the stairs to the lobby. There are so many fun games to play now that you remember. If you hadn't, he would've had to kill you out of pity.")
				return game_over(won)
		elif str(choice) == "n":
				print ("You stab him with the scalpel. He tries to fight it but you do it again and again...")
				time.sleep (4)
				print ("You pray his blood will wash you of the sins you begin to recollect. You climb out the gaping hole in the roof and look at the stars. The air is chilly but kind.")
				return game_over(won)
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)
			   
	def exit_scene(self, outcome):
	   return outcome 

