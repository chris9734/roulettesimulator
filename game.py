import random
import sys

#These are the only paremeters you can adjust, don't touch the rest#
####################################################################
initialmoney = 10000#Startcapital
incrementfactor = 3 #The multiplication factor of how much one bets after he loses
initialbet = 1      #How much do you want to bet in your first round

probability = 48.00 #How likely is it to win (two decimals max!)
games = 100         #How many rounds do you want to play max
lostmax = 7         #How often are you allowed to loose in a row
####################################################################

random.seed() #Internal seed for random generator

#################################################
#This function just returns if one loses or wins#
def game():
    myrandom = random.randint(1, 10000)
    if myrandom <= probability * 100:
#        print("You won :)")
        return 1
    else:
#        print("You lost :(")
        return 0
#################################################
#Don't touch!#
bet = initialbet
money = initialmoney
lostcount = 0
#################################################

for i in range(0, games):   #Repeats the loop as many rounds one wants to play
    money -= bet            #Subtracts a "bet-unit" from your capital
    if(lostcount == lostmax):#Checks if you lost lostmax in a row
        print("Game over, you lost " + str(lostmax) + " in a row")
        print("You started with " + str(initialmoney) + " and now you have " + str(money))
        sys.exit()
    if money < 0:           #If you run out of money you lose
        print("Game over, you run out of money")  #Print game over
        sys.exit()          #Exit game


    if game() == 1:         #You won!
        money += bet * 2    #You get double of what you bet before
        bet = initialbet    #Next bet you will be set as what you set as "initialbet"
        lostcount = 0       #Resets the lost in a row counter
    else:                   #You lost!
        bet *= incrementfactor#Next bet will be incrementfactor times higer as what it was just now
        lostcount += 1      #Increments lost counter

print("You didn't loose after " + str(games) + " rounds!\nYou started with " + str(initialmoney) + " and got additional " + str(money - initialmoney)) #You played the max number of rounds you wanted to and didn't run out of money


