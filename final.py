#
# lab 12
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
def play():
    printWelcomeMessage()
    printNow('You are walking through an overgrown driveway towards a shadowy house.')
    printNow('Trees and bushes are overgrown, and parts of the two-story mansion seems to have been burned.')
    printNow('You walk up to a huge wooden front door, twist the knob, and peer in.\n')

    hasDoll = 0
    hasCrowbar = 0
    hasAmulet = 0

    enterHouse, hasCrowbar = houseEntrance()
    if enterHouse == 1:
        enterRoomOne = roomOne()
        if enterRoomOne == 0 or enterRoomOne == 1:
            enterRoomTwo, hasAmulet = roomTwo()
            if enterRoomTwo == 0 or enterRoomTwo == 1:
                enterRoomThree = roomThree()
                if enterRoomThree == 0 or enterRoomThree == 1:
                    enterRoomFour = roomFour()
                    if enterRoomFour == 0 or enterRoomFour == 1:
                        enterRoomFive = roomFive(hasDoll, hasCrowbar, hasAmulet)
                    else:
                        return
                else:
                    return
            elif enterRoomTwo == 3:
                hasDoll = 1
                enterRoomThree = roomThree()
                if enterRoomThree == 0 or enterRoomThree == 1:
                    enterRoomFour = roomFour()
                    if enterRoomFour == 0 or enterRoomFour == 1:
                        enterRoomFive = roomFive(hasDoll, hasCrowbar, hasAmulet)
                    else:
                        return
                else:
                    return
            else:
                return
        else:
            return
    else:
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
    printNow(message)

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
            printNow('You chose to leave the house. A woman in the attic window wacthed you leave.\n')
            return 0, 0
        elif moveDirection == north:
          #Added for Lab 12, able to pick up a crowbar to use in room 5
          printNow('In the corner of your eye you spot a crowbar.')
          printNow('This might be useful in another room.')
          printNow('Would you like to pick it up?\n')
          hasCrowbar = 0
          crowbarResponse = ''
          while crowbarResponse != 'yes' or crowbarResponse != 'no':
            crowbarResponse = requestString("Type 'yes' to pick up crowbar or 'no' to leave the crowbar").lower()
            if crowbarResponse == 'yes':
              printNow('You pick up the crowbar and continue on your way.\n')
              hasCrowbar = 1
              break
            elif crowbarResponse == 'no':
              printNow('You leave the crowbar and continue on your way\n')
              break
            else:
              printNow("Only 'yes' and 'no' are valid commands.")
          printNow('You enter through the cobwebbed doorway into a vast entrance hall.')
          printNow('You walk up the creaky staircase into an upstairs hall lined with doors.')
          printNow('You open the first door on your left and stare in.\n')

          return 1, hasCrowbar
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You chose to leave the house. A woman in the attic window wacthed you leave.\n')
            return 2, 0
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
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
            printNow('You back out of the room and find another door behind you. You open it and stare in.\n')
            return 0
        elif moveDirection == north:
            printNow('You enter into the tiny dark room.')
            printNow('There is a rocking chair in the corner.')
            printNow('You leave back into the hall, and find another door behind you. You open it and stare in. This room is very bright.\n')
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
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
            printNow('You back out of the room and continue down the hall. You turn left, and open the first door on your right.\n')
            return 0, hasAmulet
        elif moveDirection == north:
            printNow('You enter into the room and notice something sticking out from under the bed.')
            printNow('It seems to be a doll.')
            printNow('Would you like to pick it up?')
            dollResponse = ''
            hasDoll = 0
            hasAmulet = 0
            while dollResponse != 'yes' or dollResponse != 'no':
                dollResponse = requestString("Type 'yes' to pick up doll or 'no' to leave the doll").lower()
                if dollResponse == 'yes':
                  #Added for Lab 12, able to pick up an amulet that you can only get if you pick up the doll. Will be used in room 5
                  printNow('\nAs you pick up the doll, something falls to the ground.')
                  printNow('It looks like an amulet.')
                  printNow('This might be useful in another room.')
                  printNow('Would you like to pick it up?\n')
                  amuletResponse = ''
                  while amuletResponse != 'yes' or amuletResponse != 'no':
                    amuletResponse = requestString("Type 'yes' to pick up the amulet or 'no' to leave the amulet").lower()
                    if amuletResponse == 'yes':
                      printNow('You pick up the amulet and put it around your neck and continue on your way.\n')
                      hasAmulet = 1
                      break
                    elif amuletResponse == 'no':
                      printNow('You leave the amulet and continue on your way\n')
                      break
                    else:
                      printNow("Only 'yes' and 'no' are valid commands.")
                  printNow('You pick up the doll and continue down the hall. You turn left, and open the first door on your right.\n')
                  hasDoll = 3
                  break
                elif dollResponse == 'no':
                    printNow('You leave doll under the bed, leave the room and continue down the hall. You turn left, and open the first door on your right.\n')
                    hasDoll = 1
                    break
                else:
                    printNow("Only 'yes' and 'no' are valid commands.")
            return hasDoll, hasAmulet

        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2, hasAmulet
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
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
            printNow('You back out of the room and continue down the hall. You turn right, and open the first door on your left.\n')
            return 0
        elif moveDirection == north:
            printNow('You enter into another dark room and see your brother.')
            printNow("'What are you doing here brother?', you ask. He doesnt seem very happy.")
            printNow('You leave the room and continue down the hall. You turn right, and open the first door on your left.\n')
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
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
            printNow('You back out of the room and continue down the hall. You go up a spiral staircase and arrive at a red door. You open it.\n')
            return 0
        elif moveDirection == north:
            printNow('You enter into another dark room and see your sister.')
            printNow('Shes standing in the corner of the room with her head down. She must be sleep walking again.')
            printNow('You back out of the room and continue down the hall. You go up a spiral staircase and arrive at a red door. You open it.\n')
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()

#
# Room 5
# This room has 2 outcomes, based on the return
# value from room 2
#
def roomFive(hasDoll, hasCrowbar, hasAmulet):
    south = 'south'
    north = 'north'
    help = 'help'
    exit = 'exit'

    moveDirection = getDirection()
    while moveDirection != south or moveDirection != north:
        if moveDirection == south:
            printNow('You back out of the room, run down the stairs and out the front door. You have made it out of the house.\n')
            return 0
        elif moveDirection == north:
            printNow('You enter into the red room.')
            printNow('You see your siblings there sitting at the table.')
            if hasDoll == 1:
                printNow('You take your seat and notice they all have dolls sitting in their laps.')
                printNow('You all play with your dolls as the ghost of your mother watches on with a smile.\n')

                #Add alternate endings
                #hidden room, need crowbar to enter
                printNow('Your mother steps aside and you notice a door with wooden planks')

                if hasCrowbar == 1:
                  printNow('Would you like to use the crowbar you picked up earlier?\n')
                  useCrowbar = ''
                  while useCrowbar != 'yes' or useCrowbar != 'no':
                    useCrowbar = requestString("Type 'yes' to use crowbar, or 'no' to not use a crowbar").lower()
                    if useCrowbar == 'yes':
                      printNow('You remove the planks and pry open the door to reveal your father\'s pocket watch, a family heirloom. ')
                      printNow('You enter the room. Your mom appears in front of you.')
                      printNow('She looks upset!')
                      if hasAmulet == 1:
                        #Win: Must have amulet to win
                        printNow('She is about to scream, when she sees the amulet around your neck.')
                        printNow('She stops and returns to her relaxed state.')
                        printNow('Gives you a hug, gives you your father\'s watch.')
                        printNow('And walks you out of the house to safety.')
                        printNow('You leave happy to have seen your family one last time.\n\n\n')
                        printNow('___END___')
                        break
                      else:
                        #Lose: Didn't pick up amulet
                        printNow('She opens her mouth and emits a blood curdling scream.')
                        printNow('You try to run, but it is too late.')
                        printNow('Your siblings sorround you, with an evil expression in their eyes.')
                        printNow('The room grows dark, and your hopes of ever getting out alive ...\n')
                        printNow('___END___')
                        break
                    else:
                      printNow('You stay playing with your siblings, staying stuck for eternety.')

                else:
                  printNow('You should have picked up the crowbar')
                  printNow('You stay playing with your siblings, staying stuck for eternety.')
            else:
                printNow("You sit with your siblings at the table. You notice they all have their dolls. You don't have yours...")
                printNow('Suddenly the door slams and the lights go out. There is nothing but silence.\n\n\n')
                printNow('___END___')
            return 1
        elif moveDirection == help:
            printWelcomeMessage()
        elif moveDirection == exit:
            printNow('You turn back and sprint out of the house. A woman in the attic window wacthed you leave.\n')
            return 2
        else:
            printNow("Only 'north', 'south', 'help', and 'exit' are valid commands.")
        moveDirection = getDirection()
