# DEEP DEEP FOREST
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
# 
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "fireflies" : ["apple"],
    "location" : "start"
}

rooms = {
    "room1" : "a forest clearing",
    "room2" : "a forest path",
    "room3" : "an alternate path"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result

def printGraphic(name):
    if (name == "fireflies"):
        print ('     !__!        ')
        print ('    (@)(-)       ')
        print ('   \.^||^./      ')
        print ('  -:  ::  :-     ')
        print ('  /<..^^..>\     ')
        print ('  the fireflies  ')

    if (name == "crown"):
        print ('    _.+._   ')
        print ('  (^\/^\/^) ')
        print ('   \@*@*@/  ')
        print ('   <-|-|->  ')
        print ('  the crown ')

    if (name == "butterfly"):
        print ('   //\         /\\  ')
        print ('  || * \ . . / * || ')
        print ('   \\____\X/____//  ')
        print ('    / *  /O\  * \   ')
        print ('    \__/  "  \__/   ') 
        print ('it is a butterfly') # this one is escaped!

    if (name == "frog"):
        print ('       (.)_(.)       ')
        print ('    _ (   _   ) _    ')
        print ('   / \/,-----,\/ \   ')
        print (' __\ ( (     ) ) /__ ')
        print (' )   /\ \._./ /\   ( ')
        print (' )_/ /|\   /|\  \_(  ')
        print (' he is the owner of the castle  ')

    if (name == "title"):
        print ('-------------------------')
        print ('      _                  ')
        print ('     | |                 ')
        print ('  ___| |_   _____   ___  ')
        print (' / _ \ \ \ / /  _ \/ __| ')
        print ('|  __/ |\ V /|  __/\__ \ ')
        print (' \___|_| \_/  \___|__/ / ')
        print ('                         ')
        print ('-------------------------')



def gameOver():

    printGraphic("fox")

    print("-------------------------------")
    print("to be continued!")
    print("name: " + player["name"] ) # customized with a name
    print( "score: " + str(player["score"]) ) # customized with a score
    return

def strangePath():
    print("The path looks dark but you move forward anyway...")
    print("You stop when you hear someone is singing a song.")
    printGraphic("butterfly")
    raw_input("press enter >")

    print("You consider your options.")
    print("options: [follow butterfly , keep going , back to find other paths]")

    pcmd = raw_input(">")

    if (pcmd == "follow butterfly"): 
        print ("follow the butterfly...")
        print ("You walk around the castle...")
        print ("Let's roll a dice to see what happens next!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 10
        roll = rollDice(0, 20, difficulty)
        
        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print ("You find a crown!")
            print ("It looks like someone lost it.")
            print ("Do you take the crown?")
            
            printGraphic("crown")

            # we dive further into the logic
            pcmd = raw_input("yes or no >")

            if (pcmd == "no"):
                print ("You leave it there.")
                strangePath()

            elif (pcmd == "yes"):
                print ("You pick it up and return to find other paths.")
                player["items"].append("crown") # add an item to the array with append
                player["score"] += 100 # add to the score
                forestClearing()

            else:
                print ("You leave it there.")
                forestClearing()

        else:
            print ("Turns out there is nothing happening... oh well.")
            strangePath()

    elif (pcmd == "keep going"):
        print ("You keep going forward... you have a strange feeling")
        print ("that you feel like you just walk through the same path...") # the lost woods reference
        strangePath()

    elif (pcmd == "back to find other paths"):
        print ("You decide to go back.")
        pcmd = raw_input(">")
        forestClearing()

    else:
        print ("You can't do that!")
        strangePath()


def forestPath():
    print ("The forest path leads you down a narrow path.")
    print ("You see a glowing area.")
    raw_input("press enter >")

    printGraphic("fireflies")
    print ("You walk closer to glowing area and see a fireflies flew out of it.")
    print ("'Who travels in my community?', says the fireflies.")
    print ("...She can talk!")
    raw_input("press enter >")
    
    print ("You consider your options.")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("crown" in player["items"]):
        print ("options: [ look around , talk to fireflies , give crown, run ]")
    else:
        print ("options: [ go back, talk to fireflies, run ]")

    pcmd = raw_input(">")

    # option 1: look at the fireflies
    if (pcmd == "go back"):
        print ("You go back...")
        forestClearing() # try again
    
    # option 2: talk to the fireflies
    elif (pcmd == "talk to fireflies"):
        print ("You try and talk to the fireflies!")
        print ("Let's roll a dice to see what happens next!")
        raw_input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("It's your lucky day! He wants to give you his light to light your way home.")
            player["score"] += 50
        else:
            print ("You try to talk to the fireflies, but... he does not respond you.")
            forestPath() # try again
        
        # nested actions and ifs
        pcmd = raw_input("Do you want to take his light? yes or no >")

        # yes
        if (pcmd == "yes"):

            print ("You take the fireflies light!")

            player["items"].append("fireflies")

            # string and int converstion!
            # we need to convert the score to a number to add to it
            # then convert it back to a string to display it to the player
            player["score"] = int(player["score"]) + 100 # conversion

            # we generate a custom string and add the score
            print ( "Your score increased to: " + str(player["score"]) ) 
            
            gameOver()

        # no
        elif (pcmd == "no"):
            print ("The fireflies flies away!")
            forestPath()
        
        # try again
        else:
            forestPath()

    elif (pcmd == "give crown"):
        print ("You give the crown to the fireflies!")
        raw_input("press enter>")
        printGraphic("crown")
        gameOver()


    # option 3: run
    elif (pcmd == "run"):
        print ("You run!")
        forestClearing() # back to start

    # try again
    else:
        print ("I don't understand.")
        forestPath() # forest path

def forestClearing():
    print ("You stand in a The elves kingdom.")
    print ("here is a path ahead of you and another path to the right.")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

    if (("crown" in player["items"]) and not ("fireflies" in player["items"])):
        print ("Your options: [ look around, path, give the crown back]")

    elif ("crown" in player["items"]):
        print ("Your options: [ look around, path, exit ]")

    else:
        print ("Your options: [ look around, path , other path , exit ]")

    pcmd = raw_input(">") # user raw_input

    # player options
    if (pcmd == "look around"):
        # its a trick!
        print ("You look around... the path behind you is .... gone?")

        raw_input("press enter >")
        forestClearing()

    # path option
    elif (pcmd == "path"):
        print ("You take the path.")
        raw_input("press enter >")
        forestPath() # path 1

    # path2 option
    elif (pcmd == "other path"):
        print ("You take the other path.")
        raw_input("press enter >")
        strangePath() # path 2

    # exiting / catching errors and crazy raw_inputs
    elif (pcmd == "exit"):
        print ("you exit.")
        return # exit the application
        
    elif (pcmd == "give the crown back"):
        print ("you find the owner of the crown in the castle...")
        printGraphic("frog")

        print ("'Thank you, my firend, I will lead you back to your world.'he says.") # escaped
        return # exit the application, secret ending

    else:
        print ("I don't understand that")
        forestClearing() # the beginning

def introStory():
    # let's introduce them to our world
    print ("Good to see you gain! What should I call you?")
    player["name"] = raw_input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print ("Welcome to the elves kingdom" + player["name"] + "!")
    print ("The story so far...")
    print ("Your were driving car on the way home at the night.")
    print ("You saw it was getting more and more foggy ahead.")
    print ("You often drive on this road, so such heavy foggy seem strange.")
    print ("Do you decide to drive ahead?")

    pcmd = raw_input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You drive through the foggy, you arrived in a elves kingdom...")
        raw_input("press enter >")
        forestClearing()
    else:
        print ("No? ... That doesn't work here.")
        pcmd = raw_input("press enter >")
        introStory() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens