from sys import exit
from random import randint 

import costs 

class Wallet(object):
    
    # money is property of object
    _money = 30
    
    #def __init__(self):
    #    self.money = Wallet.money
     
    # object (money) as property
    @property
    def money(self):
        return self.__class__._money
        
    @money.setter
    def money(self, value):
        self.__class__._money = value    
        
    def check_money(self):
        if self.money <= 0:
            print "You are out of money!"
            return False
        else:
            print "\nYou have $%i left in your wallet." % self.money
            return True
        
    def get_money(self):
        print "Money in wallet: ", self.money
        self.money = self.money
        
    def turn_cost(self):
        self.money = costs.turn_cost(self.money)
        print "After turn...", self.money
        
    def train_cost(self):
        self.money = costs.train_cost(self.money)
        
    def casino_cost(self):
        self.money = costs.casino_cost(self.money)
        
    def double(self):
        self.money = costs.double(self.money)
        
    def triple(self):
        self.money = costs.triple(self.money)


# shared attributes for all Scenes
# money goes through all scenes
# money in Wallet class
# + and - money through costs module  
class Scene(object):
    
    def __init__(self):
        # composition -> get methods from class Wallet()
        self.wallet = Wallet()
        #self.money = wallet.get_money() 
    
    def enter(self):
        print "Bad scene..."
        exit(1)
        
    def check_wallet(self):
        have_money = self.wallet.check_money()
        
        # end on no money
        if not (have_money):
            return 'end'   
        
    def prompt_turnstile(self):
        print "Remember: do NOT 'Hit' machines. They are friends."
        print "Also: you can visit the 'Casino' at any time for more money."
        print "Should you 'Push' or 'Insert' a coin?"
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        #self.money = wallet.start_money()

    def play(self):
        #money = wallet.start_money()
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('done')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
    
        current_scene.enter()

class End(Scene):
    
    end = [
        "\nYou lost\n",
        "\n...game over, buddy...\n",
        "\nThe game has ended...\n",
        "\nYou are a horse...\nbetter luck next time...\n"
    ]
    
    # choose random ending sequence
    def enter(self):
        print End.end[randint(0, len(self.end) - 1)]
        exit(1)
        
class Locked(Scene):
        
    def enter(self):
        print "\nThe turnstile is locked. You are stuck where you are."
        self.check_wallet()
        self.prompt_turnstile()
        
        action = raw_input("> ")
        
        if action == "Casino":
            return 'casino'
        
        elif action == "Hit":
            print "\nYou punch the machine and alarmed security..."
            print "Uh oh! It looks like they are coming over to take you away."
            return 'end'
         
        ##############################    
        elif action == "Push":
            print "\nYou push against the locked machine..."
            return 'locked'
        ############################## 
            
        elif action == "Insert":
            print "\nYou insert a coin into the machine."
            self.wallet.turn_cost()
            self.wallet.get_money()
            return 'unlocked'
            
        else:
            print "\nCannot understand input."
            return 'locked'
        
class Unlocked(Scene):
    
    def enter(self):
        print "\nThe machine is unlocked."
        self.check_wallet()
        self.prompt_turnstile()
        
        action = raw_input("> ")
        
        if action == "Casino":
            return 'casino'

        elif action == "Hit":
            print "\nYou punch the machine, causing it to lock again!"
            return 'locked'
            
        elif action == "Push":
            print "\nYou push against the unlocked machine."
            return 'lobby'
            
        elif action == "Insert":
            print "\nYou insert a coin into the machine."
            self.wallet.turn_cost()
            self.wallet.get_money()
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
        self.check_wallet()
        print "Which train do you pick?"
        print "Also: you can visit the 'Casino' at any time for more money."
        
        good_train = randint(1, 4)
        your_train = raw_input("Train #> ")
        
        if your_train == "Casino":
            return 'casino'
            
        else:
            self.wallet.train_cost()
            int_train = int(your_train)
        
        if int_train == 1:
            suffix = "st"
            
        elif int_train == 2:
            suffix = "nd"
            
        elif int_train == 3:
            suffix = "rd"
            
        elif int_train == 4:
            suffix = "rd"
            
        else: 
            print "\nCannot understand input."
            return 'unlocked'
        
        if int_train != good_train:
            print "\nYou get into the %s%s train and it takes off." % (your_train, suffix)
            print "However, it starts going in the wrong direction!"
            return 'end'
            
        else:
            print "\nYou get into the %s%s train and it takes off." % (your_train, suffix)
            print "It takes you home. When you get there you make yourself"
            print "some food and then go to sleep."
            return 'done'
        
class Casino(Scene):
    
    def enter(self):
        self.check_wallet()
        self.wallet.casino_cost()
        print "Casino - let's make some money!"
        print "\nGet two of the same for a little money"
        print "and three of the same for a TON!\n"
        
        slots = [
            "donkey", "horse", 
            "seven", "cowboy", 
        ]
        
        # subtract money for each play
        first_slot = slots[int(randint(0, 3))]
        second_slot = slots[int(randint(0, 3))]
        third_slot = slots[int(randint(0, 3))]
        
        print "The first slot is... %s!" % first_slot
        print "The second slot is ... %s!!" % second_slot
        print "And the third is ... %s!!!" % third_slot
        
        if (first_slot == second_slot == third_slot):
            
            print "\nAll three!\n"
            self.wallet.triple()
            
        elif ((first_slot == second_slot) or 
            (second_slot == third_slot) or (first_slot == third_slot)):
            
            print "\nYou got two!\n"
            self.wallet.double()
            
        else:
            
            print "\nNo money this time...\n"
        
        print "You leave the casino..."
        return 'locked' 
       
        
class Done(Scene):
    
    def enter(self):
        print "\nYou won the game!\n"
        exit(1)
        
class Map(object):
    # start wallet - only once
    #money = wallet.start_money()
    """
    scenes = {
       'locked': Locked(money),
       'casino': Casino(money),
       'unlocked': Unlocked(money),
       'lobby': Lobby(money),
       'end': End(money),
       'done': Done(money),
    }
    """
    money = 30
    
    scenes = {
       'locked': Locked(),
       'casino': Casino(),
       'unlocked': Unlocked(),
       'lobby': Lobby(),
       'end': End(),
       'done': Done(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        self.money = Map.money
            
    def next_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        #scene = Map.dict_scenes(scene_name)
        return scene
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
if __name__ == '__main__':
    #money = wallet.start_money()
    a_map = Map('locked')
    a_game = Engine(a_map)
    a_game.play()
    main()