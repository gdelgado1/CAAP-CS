# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter, 
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'lobby' : S.lobby(),
				'The_Corridor' : S.TheCorridor(),
				'The_Corridor2' : S.TheCorridor2(),
				'The_Vent' : S.TheVent(),
				'The_Staircase' : S.TheStaircase(),
				'The_Infirmary' : S.TheInfirmary(),
				'Exit_Den' : S.ExitDen(),
				'death' : Death()
				}
	
	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)