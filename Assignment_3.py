# let the user know what's going on
print ("Welcome to MadLibs!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
yourName = raw_input("What is your name?: ")
day = raw_input("What is your favorite day?: ")
friend1 = raw_input("Name of a classmate you've worked frequently: ")
friend2 = raw_input("Name of anyother classmate: ")
classname = raw_input("What is your favorite class?: ")
assignment = raw_input("What is your least favorite assignment?: ")
adjective = raw_input("Enter one adjective: ")
petName = raw_input("What is your pet name?: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "I am " + yourName + ". " + " I went to " + friend1 + " 's house with " + friend2 + " on " + day + ". " \
"We gethered together to do " + assignment + " of " + classname + ". " \
"My friend" + friend1 + " had a " + adjective + " dog called " + petName + ". " \
petName + " welcomed us with excitement " + ". " \
"It took us 3 hours to finish " + assignment + ". " + " and then " + friend2 + " and I went home together " + ". " \

# finally we print the story
print (story)