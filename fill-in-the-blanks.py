# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!



lvl1Q = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
                adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
                don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
                tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

lvl1QProgress = lvl1Q

lvl1A = ["function","parameters", "None", "list"]

lvl2Q = '''A ___1___ consist of a bunch of html documents. ___2___ stands for Hyper Text Markup Language. ___3___ is used to add style to the webpage. The components of the web include the ___4___ (your computer and browser), over the ___5___, and interacting with ___6___ '''

lvl2QProgress = lvl2Q

lvl2A = ["webpage", "HTML", "CSS","client","internet", "servers"]


lvl3Q = '''Between binary sort and bubble sort, which one is faster?:___1___.A ___2___ is used for connecting users to the internet
                LAN stands for ___3___ and a ___4___ allows for full duplex transmission and also serves as a gateway in the network'''

lvl3QProgress = lvl3Q

levelDifficulty = ["easy", "meadium","hard"]
lvl3A= ["binary", "modem", "local area network", "router"]

attempts = 5



#list of blank spaced input to associate with possibly correct answers
blankSpaceList1 = ["___1___","___2___","___3___", "___4___"]
blankSpaceList2 = ["___1___","___2___","___3___", "___4___", "___5___", "___6___"]
blankSpaceList3 = ["___1___","___2___","___3___", "___4___"]

levelDifficulty = ['easy', 'medium', 'hard' ]


def run_Game ():
    choice = raw_input("Please enter your level difficulty: ")
    
    #give feedback to user based on the difficulty chosen
    if choice in levelDifficulty:
        print "The level you chose is: "+choice
        print "You have 5 attempts per question"

    else:
        print "You need to choose between: easy, medium, or hard"
        run_Game()
    
    #start game based on difficulty 
    if choice == 'easy':
        easy()
    
    elif choice == 'medium':
        medium()
    
    else:
        hard()



def easy():
    global attempts
    global lvl1Q_Progress
    for  i,blank in enumerate(blankSpaceList1):
        while attempts > 0:
            #print updated paragraph 
            print "The current paragraph reads as such:\n"
            print lvl1QProgress

            #takes in guesses and checks if they're correct
            guess = raw_input ("\nWhat should be substituted in for " + blank + "? ")

            #correct
            if guess == lvl1A[i]:

                lvl1Q_Progress = lvl1QProgress.replace(blank,guess)

                print "Your guess was correct!"
                attempts = 5
                break

            else :
                attempts = attempts - 1
                
                if attempts == 0:
                    print "You've failed too many straight guesses. Game Over..."
                    break

                elif attempts == 1:
                    print 'You have ' +str(attempts)+ ' attempt left. this is your last attempt! Make it count!'
                
                else:

                    print "Sorry try again..."
                    print "This isn't the correct answer! You have "  +str(attempts)+ " attempts left."
    
    if attempts > 0:
        print "\nYou won!!!, WO0H0OOooOO"
            
            

def medium():
    global attempts
    global lvl2QProgress
    for  i,blank in enumerate(blankSpaceList2):
        while attempts > 0:
            #print updated paragraph 
            print "The current paragraph reads as such:"
            print lvl2QProgress

            #takes in guesses and checks if they're correct
            guess = raw_input ("What should be substituted in for " + blank + "? ")

            #correct
            if guess == lvl2A[i]:

                lvl2QProgress = lvl2QProgress.replace(blank,guess)

                print "Your guess was correct!"
                attempts = 5
                break

            else :
                attempts = attempts - 1
                
                if attempts == 0:
                    print "You've failed too many straight guesses. Game Over..."
                    break

                elif attempts == 1:
                    print 'You have ' +str(attempts)+ ' attempt left. this is your last attempt! Make it count!'
                
                else:

                    print "Sorry try again..."
                    print "This isn't the correct answer! You have "  +str(attempts)+ " attempts left."
    
    if attempts > 0:
        print "\nYou won!!!, WO0H0OOooOO"

def hard():
    global attempts
    global lvl3QProgress
    for  i,blank in enumerate(blankSpaceList3):
        while attempts > 0:
            #print updated paragraph 
            print "The current paragraph reads as such:"
            print lvl3QProgress

            #takes in guesses and checks if they're correct
            guess = raw_input ("\nWhat should be substituted in for " + blank + "? ")

            #correct
            if guess == lvl3A[i]:

                lvl3QProgress = lvl3QProgress.replace(blank,guess)

                print "Your guess was correct!"
                attempts = 5
                break

            else :
                attempts = attempts - 1
                
                if attempts == 0:
                    print "You've failed too many straight guesses. Game Over..."
                    break

                elif attempts == 1:
                    print 'You have ' +str(attempts)+ ' attempt left. this is your last attempt! Make it count!'
                
                else:

                    print "Sorry try again..."
                    print "This isn't the correct answer! You have "  +str(attempts)+ " attempts left."
    
    if attempts > 0:
        print "\nYou won!!!, WO0H0OOooOO"


run_Game()





