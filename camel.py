import random

def startScreen():
    print("Welcome to Camel!")
    print('''You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.\n''')

# List of stats for the game loop

distanceTraveled = 0
playerThirst = 0 #Thirst goes up during travel?
camelStatus = 100
nativeDistance = 100
canteenAmount = 100
destination = 100

# status = ["Distance Traveled: %d" % distanceTraveled, "Thirst: %d " % playerThirst, camelStatus, nativeDistance, canteenAmount, destination]



playerChoice = ''

options = ["A. Drink from your canteen.",
    "B. Ahead moderate speed.",
    "C. Ahead full speed.",
    "D. Stop and rest.",
    "E. Status check.",
    "Q. Quit."]

# Prints above player options
def printOptions():
    for i in options:
        print(i)




# Print out a list of current statuses
def status():
    print()
    print("You have entered: " + playerChoice)
    print("Distance Traveled: %d" % distanceTraveled)
    print("Thirst: %d" % playerThirst)
    print("Camel Status: %d" % camelStatus)
    print("Native distance: %d" % nativeDistance)
    print("Canteen Amount: %d" % canteenAmount)
    print("You have %d miles to go before you reach safety" %destination)

def loseCondition(): # Conditions to lose the game with
    if playerThirst >= 100:
        print("You died of thirst")
        return True

    elif nativeDistance <= 0:
        print("You were killed by natives")
        return True

    elif camelStatus <= 0:
        print("Your camel died!")
        return True


    elif destination <= 0:
        print("You have survived!")
        return True



done = False

startScreen()

while done is False:
    print()
    printOptions()
    print("Choose a letter:")
    playerChoice = input()
    playerChoice = playerChoice.lower()

    if loseCondition() is True: # Lose condition fuction
        done = True
        print("You have lost!!!")
        break

    if len(playerChoice) != 1: # For if the player doesn't enter anything, or more than one letter
        print("Please enter a letter")

    elif playerChoice == str("a"): # Drinking from canteen
        print("You have entered: " + playerChoice.upper())
        if canteenAmount >= 0: # Checks canteen amount
            thirstAmount = random.randint(5,11)
            playerThirst -= thirstAmount
            canteenAmount -= thirstAmount
            print("You have drank from your canteen.")

        if playerThirst < 0: # Prevents negative player thirst amounts
            playerThirst = 0
        elif canteenAmount == 0:
            print("You ran out of water.")

        nativeDistance -= 50
        print("Your thirst is %d" % playerThirst)

    elif playerChoice == str("b"): # Ahead moderate speed
        print("You have entered: " + playerChoice)
        travelDistance = random.randint(5,11) # Required to subtract current travel distance
        distanceTraveled += travelDistance    # instead of total to destination amount
        playerThirst += random.randint(15,31) # Thirst Level
        nativeDistance += travelDistance * .5 # Gain on them half speed
        camelStatus -= random.randint(0,6)
        destination -= travelDistance
        print("You traveled %s miles" % travelDistance)

    elif playerChoice == str("c"): # Ahead Max Speed
        print("You have entered: " + playerChoice)
        travelDistance = random.randint(10,21)
        distanceTraveled += travelDistance
        playerThirst += random.randint(9,21)
        camelStatus -= random.randint(9,21)
        nativeDistance += travelDistance * 1.5
        destination -= travelDistance
        print("You traveled %s miles" % travelDistance)


    elif playerChoice == str("d"): #Stop and rest
        print("You have entered: " + playerChoice)
        print("You are resting.")
        camelStatus += random.randint(9,21)


    elif playerChoice == str("e"): #Check Status
        status()


    elif playerChoice == str("q"): #Quit
        print("You have quit")
        done = True




