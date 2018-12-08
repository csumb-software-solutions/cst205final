#
# Final Project
# Team 7 - Software Solutions
# Andrew Meraz
# Doug Asker
# Jared Cheney
#
# Game inspired by the Netflix series the Haunting of Hill House
#

#
# main function
#

#We are storing data under userData for 4 items that can be used throughout the game, including the user name
#userData[0] = userName
#userData[1] = crowBar
#userData[2] = Doll
#userData[3] = Amulet
userData = ['', 0, 0, 0]

# Note: make sure to get project structure from github and replace filepath with your file path
filePath = "C:\\Users\\jared\\Desktop\\CSUMB\\CST_205\\final\\cst205final\\images\\"
owl = filePath + "owl.jpeg"
girlScreaming = filePath + "girl_screaming.jpg"
holdingKnife = filePath + "holding_knife.jpg"
hotel = filePath + "hotel.jpg"
mother = filePath + "mother.jpg"
normanBate = filePath + "norman_bates.jpg"
skeleton = filePath + "skeleton.jpg"

def play():
    blackWhiteHotel = betterBnW(makePicture(hotel))
    #request the name of the user. Used in room 5.
    userData[0] = requestString("Please type in your name.")
    printWelcomeMessage()
    show(blackWhiteHotel)
    message = 'You are driving in areally bad storm, you see a Motel and next to it a shadowy house.\n'
    message += 'Trees and bushes are overgrown, and parts of the two-story mansion seems to have been burned.\n'
    message += 'You park your car at the Motel and run in to the office.\n'
    showInformation (message)

    enterHouse = houseEntrance()
    if enterHouse == 1:
        enterRoomOne = roomOne()
        if enterRoomOne == 0 or enterRoomOne == 1:
            enterRoomTwo = roomTwo()
            if enterRoomTwo == 0 or enterRoomTwo == 1:
                enterRoomThree = roomThree()
                if enterRoomThree == 0 or enterRoomThree == 1:
                    enterRoomFour = roomFour()
                    if enterRoomFour == 0 or enterRoomFour == 1:
                        enterRoomFive = roomFive()
                    else:
                        return
    return

#
# get the direction from the user
#
def getDirection():
    return requestString('Would you like to go north into the room or south to exit?').lower()

#
# show the greeting/help text
#
def printWelcomeMessage():
    message = '\n===========================================================\n'
    message += 'Welcome to Bates Motel. Norman and his Mother are very happy you came...\n'
    message += "To move forward enter 'north'\n"
    message += "To go backwards enter 'south'\n"
    message += "For help on how to play enter 'help'\n"
    message += "To quit the game enter 'exit'\n"
    message += '===========================================================\n\n'
    showInformation(message)

#
# main enterance to the house
# pick up crowbar
#
def houseEntrance():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('You chose to leave the house. A woman in the attic window wacthed you leave.\n')
            return 0
        elif moveDirection == north:
          #Added for Lab 12, able to pick up a crowbar to use in room 5
          message = 'Hi my name is Norman, Norman Bates.\n'
          message = 'I am glad that you will be staying.\n'
          message += 'Do you really want to stay?\n'
          showInformation(message)
          printNow('Hint: Staying at the Bates motel might be dangerous.')
          crowbarResponse = ''
          while crowbarResponse != 'yes' or crowbarResponse != 'no':
            crowbarResponse = requestString("Type 'yes' to stay or 'no' to leave the Motel").lower()
            if crowbarResponse == 'yes':
              showInformation('You grab your room key and proceed to your room.\n')
              userData[1] = 1
              break
            elif crowbarResponse == 'no':
              showInformation('You decide that you are not going to stay at the Bates Motel\n')
              return 2
            else:
              showInformation("Only 'yes' and 'no' are valid commands.")

          show(makePicture(owl))
          message2 = 'You enter your room and it is very still except for the portrait, the eyes keep following you .\n'
          message2 += 'Norman knocks on the door.\n'
          message2 += 'You open the door and he stares .\n'
          showInformation(message2)

          return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInformation('You chose to leave the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 1
#
def roomOne():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('You will now go up too the house on the hill. You enter the house\n')
            return 0
        elif moveDirection == north:
            show(makePicture(normanBate))
            message = 'You decide to visit the old house. The door is open and as you enter you hear a faint sound of an old women singing. \n'
            message += 'The room is very dark.\n'
            message += 'You look back into the hall, and find another door behind you. You open it and stare in.\n'
            showInformation(message)
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInfomration('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 2
# This room has an action in it
# returns 1 if no action was taken
# returns 3 if action was taken
#
def roomTwo():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('You back out of the room and continue down the hall. You turn left, and open the first door on your right.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(skeleton))
            message = 'You enter into the room and on the bed is a skeleton. There is also something shining under the bed.\n'
            message += 'It is difficult to see what it is.\n\n'
            message += 'Would you like to lift the covers to see more?'
            showInformation(message)
           # printNow('Hint: There may be more under the bed.')

            dollResponse = ''

            while dollResponse != 'yes' or dollResponse != 'no':
                dollResponse = requestString("Type 'yes' to lift the covers or 'no' to not lift the covers").lower()
                if dollResponse == 'yes':
                  #Added for Lab 12, able to pick up an amulet that you can only get if you pick up the doll. Will be used in room 5
                  message = '\nAs you lift the covers, you see a knife.\n'
                  message += 'The knife has dried blood stains on it.\n'
                  message += 'This might be useful in another room.\n\n'
                  message += 'Would you like to pick it up?\n'
                  showInformation(message)
                  printNow('Hint: The knife might be helpful in another room.')
                  amuletResponse = ''
                  while amuletResponse != 'yes' or amuletResponse != 'no':
                    amuletResponse = requestString("Type 'yes' to pick up the knife or 'no' to leave the knife").lower()
                    if amuletResponse == 'yes':
                      showInformation('You pick up the knife and continue on your way.\n')
                      userData[3] = 1
                      break
                    elif amuletResponse == 'no':
                      showInformation('You leave the knife and continue on your way\n')
                      break
                    else:
                      showInformation("Only 'yes' and 'no' are valid commands.")
                  showInformation('You continue down the hall. You turn left, and open the first door on your right.\n')
                  userData[2] = 1
                  break
                elif dollResponse == 'no':
                    showInformation('You leave the room and continue down the hall. You turn left, and open the first door on your right.\n')
                    break
                else:
                    showInformation("Only 'yes' and 'no' are valid commands.")
            return 1

        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInformation('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 3
#
def roomThree():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('You back out of the room and continue down the hall.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(holdingKnife))
            message = 'You enter into another dark room and see an old lady in a rocking chair.\n'
            message += "'What are you doing here?', she asks, She doesnt seem very happy.\n"
            message += 'You leave the room and continue down the hall. You turn right, and open the first door on your left.\n'
            showInformation(message)
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInformation('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 4
#
def roomFour():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('Your being being chased by Normans mother with a knife. You run down towards Motel.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(girlScreaming))
            message = ' Normans mother is chasing you with a knife. You run down the hill back to your room.\n'
            message += 'Norman is standing outside of the room with a smile. He says you should not go up to the house.\n'
            message += 'You run and Norman is following you.\n'
            showInformation(message)
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInformation('You turn back and run. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 5
# This room has 2 outcomes, based on the return
# value from room 2
#
def roomFive():
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'
    hasDoll = userData[2]
    hasCrowbar = userData[1]
    hasAmulet = userData[3]
    userName = userData[0]

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            showInformation('You run, screaming for help.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(mother))
            message = 'You go back into your motel room and lock the door.\n'
            message += 'You see the eyes in portrait follow you around the room..\n'
            #use the name at the end
            message += '\nyou hear Normans voice say \n"'  + userName +  ' mother is very angry."\n\n'
            if hasDoll == 1:
                message += 'You pick up the phone to call the police but the phone is dead.\n'
                message += 'You can hear the thunder from the storm .\n\n'

                #Add alternate endings
                #hidden room, need crowbar to enter
                message +='You look out the window and see nothing but darkness. \n\n'

                if hasCrowbar == 1:
                  message += 'Would you like to hide?\n'
                  showInformation(message)
                  printNow('Hint: Selecting yes means you may never be found.')
                  useCrowbar = ''
                  while useCrowbar != 'yes' or useCrowbar != 'no':
                    useCrowbar = requestString("Type 'yes' to hide, or 'no' to open the door").lower()
                    if useCrowbar == 'yes':
                      message2 = 'You close your eyes and hope it is just a dream. \n'
                      message2 += 'You sit on the bed trying to understand what is happening.\n'
                      message2 += 'you are very tired and upset!'
                      showInformation(message2)
                      if hasAmulet == 1:
                        #Win: Must have amulet to win
                        message3 = 'you scream, when you see a shadow in the window .\n'
                        message3 += 'You try to decide if you should look out the window or hide.\n'
                        message3 += 'In a soft voice you hear Norman ask you if you are alright.\n'
                        message3 += 'Have you just imagined all of this..\n'
                        message3 += 'You respond to Norman and tell him you are fine.\n\n\n'
                        message3 += '___END___'
                        showInformation(message3)
                        break
                      else:
                        #Lose: Didn't pick up amulet
                        message3 = 'She opens her mouth and emits a blood curdling scream.\n'
                        message3 += 'You try to run, but it is too late.\n'
                        message3 += 'You see an old lady, with an evil expression in her eyes.\n'
                        message3 += 'The room grows dark, and your hopes of ever getting out alive ...\n\n'
                        message3 += '___END___'
                        break
                    else:
                      showInformation('You are stuck at the Bates Motel for eternety.')
                      break

                else:
                  message += 'You should not have picked up the knife. \n'
                  message += 'You wake up and relize it is just a dream.'
                  showInformation(message)
            else:
                message += "You see Norman at the table. You notice he has a smile on his face..."
                message += 'Suddenly the door slams and the lights go out. There is nothing but silence.\n\n\n'
                message += '___END___'
                showInformation(message)
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            showInformation('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            showInformation("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

# make an image black and white v2
def betterBnW(pic):
   pixels = getPixels(pic)

   for p in pixels:
     r1 = getRed(p)
     g1 = getGreen(p)
     b1 = getBlue(p)

     bw = r1*0.299 + g1*0.587 + b1*0.114

     bwColor = makeColor(bw, bw, bw)
     setColor(p, bwColor)

   return pic
