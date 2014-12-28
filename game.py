from sys import exit
from random import randint

import time 

class Scene(object):
    
    def enter(self):
        print "Bad scene..."
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('done')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
    
        current_scene.enter()

class End(Scene):
    
    end = [
        "You lost",
        "...game over, buddy...",
        "The game has ended...",
        "You are a horse"
    ]
    
    # choose random ending sequence
    def enter(self):
        print End.end[randint(0, len(self.end) - 1)]
        exit(1)
        
class Locked(Scene):
    
    def enter(self):
        print "\nThe turnstile is locked. You are stuck where you are."
        print "Remember: do NOT 'Hit' machines. They are friends."
        print "Should you 'Push' or 'Insert' a coin?"
        
        action = raw_input("> ")
        
        if action == "Hit":
            print "\nYou punch the machine and alarmed security..."
            print "Uh oh! It looks like they are coming over to take you away."
            return 'end'
         
        ##############################    
        elif action == "Push":
            print "\nYou push against the locked machine..."
            return 'scene3'
        ############################## 
            
        elif action == "Insert":
            print "\nYou insert a coin into the machine."
            return 'unlocked'
            
        else:
            print "\nCannot understand input."
            return 'locked'
        
class Unlocked(Scene):
    
    # unlocked should be on a timer? 
    def __init__(self):
        pass
    
    def enter(self):
        print "\nThe machine is unlocked."
        print "Remember: do NOT 'Hit' machines. They are friends."
        print "Should you 'Push' or 'Insert' a coin?"
        
        action = raw_input("> ")
        
        if action == "Hit":
            print "\nYou punch the machine, causing it to lock again!"
            return 'locked'
            
        elif action == "Push":
            print "\nYou push against the unlocked machine."
            print "It turns and you walk through into the lobby."
            return 'lobby'
            
        elif action == "Insert":
            print "\nYou insert a coin into the machine."
            return 'unlocked'
            
        else:
            print "\nCannot understand input."
            return 'unlocked' 

# Include riddle or maze here!         
class Lobby(Scene):
    
    def enter(self):
        print "\nYou pass through the turnstile and into the lobby."
        print "There are four trains about to leave for your city."
        print "No signs. No indication of direction..."
        print "Which train do you pick?"
        
        good_train = randint(1, 4)
        your_train = raw_input("Train #> ")
        
        if int(your_train) != good_train:
            print "\nYou get into the %sth train and it takes off." % your_train
            print "However, it starts going in the wrong direction!"
            return 'end'
            
        else:
            print "\nYou get into the %sth train and it takes off." % your_train
            print "It takes you home. When you get there you make yourself"
            print "some food and then go to sleep."
            return 'done'
        
class Scene3(Scene):
    
    def enter(self):
        print "Scene3"
        
class Done(Scene):
    
    def enter(self):
        print "\nYou won the game!"
        return 'done'
        
        
class Map(object):
    
    scenes = {
        'locked': Locked(),
        'unlocked': Unlocked(),
        'lobby': Lobby(),
        'scene3': Scene3(),
        'end': End(),
        'done': Done(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        return scene
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
 
def main():
    a_map = Map('locked')
    a_game = Engine(a_map)
    a_game.play()
        
if __name__ == '__main__':
    main()