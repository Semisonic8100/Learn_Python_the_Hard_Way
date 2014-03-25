print "You enter a dark room with three doors.  Do you go through door #1, door #2, or door #3?"

door = raw_input("> ")

if door in ("1", "one"):
    print "There's a giant bear here eating cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")

    if bear in ("1", "one"):
        print "The bear eats your face off.  Game over!"
    elif bear in ("2", "two"):
        print "The bear eats your legs off.  Game over!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door in ("2", "two"):
    print "You stare into the endless abyss of Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity in ("1", "one") or insanity in ("2", "two"):
        print "Your body survives power by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door in ("3", "three"):
    print "You step through the door into a 70's nightclub."
    print "1. Do a little dance."
    print "2. Make a little love."
    print "3. Get down tonight."

    seventies = raw_input("> ")
    
    if seventies in ("1", "one"):
        print "Get down with your bad self!  Everybody is impressed with your sweet dance moves."
    elif seventies in ("2", "two"):
        print "\'Uh oh.\'  Hope they make a cream for that."
    elif seventies in ("3", "three"):
        print "You shake your booty well into the night, make some new friends, and have a fantastic time.  \'Yay\' happy ending!"
    else:
        print "Your attempt to %s results in utter failure.  Game over." % seventies
else:
    print "You stumble around and fall on a knife and die.  Good job!"
