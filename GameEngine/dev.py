#! /usr/bin/python3.6

import actions
import character_lib

choice = ""

while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print character stats
    3 - slay ROUS''')

    choice = str(input ('make your selection: '))

    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.arena()
    elif (choice == '2'):
        actions.print_status(character_lib.user)
    elif (choice == '3'):
        actions.combat_victory(character_lib.ROUS)