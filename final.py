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
    message = 'You are walking through an overgrown driveway towards a shadowy house.\n'
    message += 'Trees and bushes are overgrown, and parts of the two-story mansion seems to have been burned.\n'
    message += 'You walk up to a huge wooden front door, twist the knob, and peer in.\n'
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
    message += 'Welcome to Hill House. The house is very happy you came...\n'
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
          message = 'In the corner of your eye you spot a crowbar.\n'
          message += 'Would you like to pick it up?\n'
          showInformation(message)
          printNow('Hint: The crowbar might be helpful in another room.')
          crowbarResponse = ''
          while crowbarResponse != 'yes' or crowbarResponse != 'no':
            crowbarResponse = requestString("Type 'yes' to pick up crowbar or 'no' to leave the crowbar").lower()
            if crowbarResponse == 'yes':
              showInformation('You pick up the crowbar and continue on your way.\n')
              userData[1] = 1
              break
            elif crowbarResponse == 'no':
              showInformation('You leave the crowbar and continue on your way\n')
              break
            else:
              showInformation("Only 'yes' and 'no' are valid commands.")

          show(makePicture(owl))
          message2 = 'You enter through the cobwebbed doorway into a vast entrance hall.\n'
          message2 += 'You walk up the creaky staircase into an upstairs hall lined with doors.\n'
          message2 += 'You open the first door on your left and stare in.\n'
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
            showInformation('You back out of the room and find another door behind you. You open it and stare in.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(normanBate))
            message = 'You enter into the tiny dark room.\n'
            message += 'There is a rocking chair in the corner.\n'
            message += 'You leave back into the hall, and find another door behind you. You open it and stare in. This room is very bright.\n'
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
            message = 'You enter into the room and notice something sticking out from under the bed.\n'
            message += 'It seems to be a doll.\n\n'
            message += 'Would you like to pick it up?'
            showInformation(message)
            printNow('Hint: The doll might be helpful in another room.')

            dollResponse = ''

            while dollResponse != 'yes' or dollResponse != 'no':
                dollResponse = requestString("Type 'yes' to pick up doll or 'no' to leave the doll").lower()
                if dollResponse == 'yes':
                  #Added for Lab 12, able to pick up an amulet that you can only get if you pick up the doll. Will be used in room 5
                  message = '\nAs you pick up the doll, something falls to the ground.\n'
                  message += 'It looks like an amulet.\n'
                  message += 'This might be useful in another room.\n\n'
                  message += 'Would you like to pick it up?\n'
                  showInformation(message)
                  printNow('Hint: The amulet might be helpful in another room.')
                  amuletResponse = ''
                  while amuletResponse != 'yes' or amuletResponse != 'no':
                    amuletResponse = requestString("Type 'yes' to pick up the amulet or 'no' to leave the amulet").lower()
                    if amuletResponse == 'yes':
                      showInformation('You pick up the amulet and put it around your neck and continue on your way.\n')
                      userData[3] = 1
                      break
                    elif amuletResponse == 'no':
                      showInformation('You leave the amulet and continue on your way\n')
                      break
                    else:
                      showInformation("Only 'yes' and 'no' are valid commands.")
                  showInformation('You pick up the doll and continue down the hall. You turn left, and open the first door on your right.\n')
                  userData[2] = 1
                  break
                elif dollResponse == 'no':
                    showInformation('You leave doll under the bed, leave the room and continue down the hall. You turn left, and open the first door on your right.\n')
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
            showInformation('You back out of the room and continue down the hall. You turn right, and open the first door on your left.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(holdingKnife))
            message = 'You enter into another dark room and see your brother.\n'
            message += "'What are you doing here brother?', you ask. He doesnt seem very happy.\n"
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
            showInformation('You back out of the room and continue down the hall. You go up a spiral staircase and arrive at a red door. You open it.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(girlScreaming))
            message = 'You enter into another dark room and see your sister.\n'
            message += 'Shes standing in the corner of the room with her head down. She must be sleep walking again.\n'
            message += 'You back out of the room and continue down the hall. You go up a spiral staircase and arrive at a red door. You open it.\n'
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
            showInformation('You back out of the room, run down the stairs and out the front door. You have made it out of the house.\n')
            return 0
        elif moveDirection == north:
            show(makePicture(mother))
            message = 'You enter into the red room.\n'
            message += 'You see your siblings there sitting at the table.\n'
            #use the name at the end
            message += '\nThey look to you and say \n"' + userName + ' come play with us."\n\n'
            if hasDoll == 1:
                message += 'You take your seat and notice they all have dolls sitting in their laps.\n'
                message += 'You all play with your dolls as the ghost of your mother watches on with a smile.\n\n'

                #Add alternate endings
                #hidden room, need crowbar to enter
                message +='Your mother steps aside and you notice a door with wooden planks\n\n'

                if hasCrowbar == 1:
                  message += 'Would you like to use the crowbar you picked up earlier?\n'
                  showInformation(message)
                  printNow('Hint: Selecting yes allows you to go to another room. Who knows what you will find.')
                  useCrowbar = ''
                  while useCrowbar != 'yes' or useCrowbar != 'no':
                    useCrowbar = requestString("Type 'yes' to use crowbar, or 'no' to not use a crowbar").lower()
                    if useCrowbar == 'yes':
                      message2 = 'You remove the planks and pry open the door to reveal your father\'s pocket watch, a family heirloom. \n'
                      message2 += 'You enter the room. Your mom appears in front of you.\n'
                      message2 += 'She looks upset!'
                      showInformation(message2)
                      if hasAmulet == 1:
                        #Win: Must have amulet to win
                        message3 = 'She is about to scream, when she sees the amulet around your neck.\n'
                        message3 += 'She stops and returns to her relaxed state.\n'
                        message3 += 'Gives you a hug, gives you your father\'s watch.\n'
                        message3 += 'And walks you out of the house to safety.\n'
                        message3 += 'You leave happy to have seen your family one last time.\n\n\n'
                        message3 += '___END___'
                        showInformation(message3)
                        break
                      else:
                        #Lose: Didn't pick up amulet
                        message3 = 'She opens her mouth and emits a blood curdling scream.\n'
                        message3 += 'You try to run, but it is too late.\n'
                        message3 += 'Your siblings sorround you, with an evil expression in their eyes.\n'
                        message3 += 'The room grows dark, and your hopes of ever getting out alive ...\n\n'
                        message3 += '___END___'
                        break
                    else:
                      showInformation('You stay playing with your siblings, staying stuck for eternety.')
                      break

                else:
                  message += 'You should have picked up the crowbar\n'
                  message += 'You stay playing with your siblings, staying stuck for eternety.'
                  showInformation(message)
            else:
                message += "You sit with your siblings at the table. You notice they all have their dolls. You don't have yours..."
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
