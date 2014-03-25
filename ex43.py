from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured.  Subclass it and implement enter()."
        exit(1)

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
        print "\n---------"
        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    quips = [
        "You died.  You kind of suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that is better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class CentralCorridor(Scene):
    
    def enter(self):
        print """The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.  You are the last surviving member, and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pot."""
        print "\n"
        print """You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate filled body.  He's blocking the door to the Armory and about to pull a weapon to blast you."""
        
        action = raw_input("> ")
        if action == "shoot!":
            print """Quick on the draw, you yank out your blaster and fire at the Gothon.  His clown costume is flowing around his body, which throws off your aim.  Your laser hits his costume but misses him entirely.  \n This completely ruins his brand new costume, which his mother bought him.  He flies into a rage and blasts you repeatedly in the face until you are dead.  Then he eats you."""
           return 'death'
        
        elif action == "dodge!":
            print """Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blast crackles past your head.  \n  In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out.\n  You wake up shortly after only to wish you hadn't, as the Gothon stomps on your head repeatedly until you are dead.  Then he eats you."""
            return 'death'
        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the Academy.  You tell the one Gothon joke you know.\n \"Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.\"\n The Gothan stops, trying not to laugh, then busts out laughing.  He can't move!\n While he's laughing you run up and shoot him square in the head, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return "central_corridor'
            
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print """You do a dive roll into the Weapon Armory, crouch and scane the room for more Gothons.  It's quiet.  TOO quiet.\n You stand up and run to the far side of the room and find the neutron bomb in its container.  There's a keypad lock on the box.  You need the code to get the bomb out.  If you get the code wrong 10 times the lock closes forever and you can't get the bomb.  The code is three digits."""
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]>")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZZZEDDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        
        if guess == code
            print """The container clicks open and the seal breaks, letting gas out.  You grab the neutron bomb and run as fast as you can to the bridge, where you must place it in the right spot."""
            return 'the_bridge'
        else:
            print """The lock buzzes one last time and you hear a sickening melting sound as the mechanism is fused together.  You decide to sit there, and finally the Gothons blow up the ship from their ship and you die."""
            return 'death'
            
class TheBridge(Scene):
    
    def enter(self):
        print """You burst onto the Bridge with the neutron destruct bomb under your arm and surprise five Gothons who are trying to take control of the ship.  Each of them has an even uglier clown costume on than the last.  They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off."""
        
        action = raw_input("> ")
        
        if action == "throw the bomb":
            print """In a panic you throw the bomb at the group of Gothons and make a leap for the door.  A Gothon shoots you in the back for your trouble.  As you die you see another Gothon frantically try to disarm the bomb.  You get the satisfaction of knowing they will probably blow up when it goes off."""
            return 'death'
        
        elif action == "slowly place the bomb":
            print """You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat.  You inch backwards to the door, open it, and then carefully place the bomb on the floor.  You keep your blaster pointed at it as you back away.\n When you get to the door, you menace the Gothons one last time with your pistol before you turn and dive through, punching the close button and blasting the lock.  \n Now that the bomb is placed, it's time to get off this tin can.  You run to the escape pod."""
            return 'escape_pod'
            
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"

class EscapePod(Scene):
    
    def enter(self):
        print """You rush through the ship, desperately trying to make it to the escape pod before the whole thing explodes.  The remaining Gothons have evacuated, so your run is clear of interference.  You get to the chamber with the escape pods.  There are five, but some could be damaged.  You don't have time to look.  You have to pick one."""
        good_pod = randint(1,5)
        guess = int(raw_input("[pod #]> "))

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print """The pod escapes out into the void of space.  You have a second to glimpse Earth before the damaged hull ruptures.  The pod implodes violently, crushing your body within."""
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print """The pod easily slides out into space and towards the planet below.  As you fly towards the planet below, you see your ship first implode, then explode like a bright star, taking out the Gothan ship in a torrent of fire and debris.\n You won!"""
            return 'finished'
            




class Map(object):
    
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass

a_map = Map('central corridor')
a_game = Engine(a_map)
a_game.play()

