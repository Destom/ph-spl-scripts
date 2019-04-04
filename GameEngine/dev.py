#! /usr/bin/python3.7

import actions
import character_lib
import item_lib

item_dict = {}
for item in item_lib.inventory_lots.item_list:
    if (item_dict.contains(item)):
        print(item)
    else:
        print (f'no {item}'')

exit()

choice = ""

while (choice != 'x'):
    print('''What would you like to test?
    1 - arena
    2 - print character stats
    3 - slay ROUS
    4 - enter the store''')

    choice = str(input ('make your selection: '))

    print ('You chose ' +  choice)

    if (choice == '1'):
        actions.arena()
    elif (choice == '2'):
        actions.print_status(character_lib.user)
    elif (choice == '3'):
        actions.combat_victory(character_lib.ROUS)
    elif (choice == '4'):
        actions.home_store.enter()
