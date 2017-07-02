import character
import importlib

class opponent:
        def __init__(self,name,health,max_health,attack,defence,evasion):
            self.name = name
            self.health = health
            self.max_health = max_health
            self.attack = attack
            self.defence = defence
            self.evasion = evasion

rat = opponent("Rat",10,10,4,2,2)
rous = opponent("ROUS(rodent of unusual size)",10,10,6,2,2)


character_health = character.health()
character_mac_health = character.max_health()
character_attack = character.attack()
character_defence = character.defence()
character_evasion = character.evasion()


#name = input("what is your name :")
name = "Destom"
print ("hello " + name)


print  ("Your stats are \n Health " + str(character_health) + " out of " + str(character_mac_health) + '\n' + "Attack " + str(character_attack) + '\n' + "Defence " + str(character_defence) + '\n' + "Evasion " + str(character_evasion) + '\n' + '\n' + '\n')


print ("Availible opponents are 'Rat' and 'RUS' (Rodent of unusual size)")
enemy_input =  input("pick your enemy: ")
enemy = enemy_input.lower()

e = eval(enemy)

enemy_health = e.health
enemy_mac_health = e.max_health
enemy_attack = e.attack
enemy_defence = e.defence
enemy_evasion = e.evasion

print ("The %s's stats are " %(e.name) + "\n" +
"Health " + str(e.health) + " out of " + str(e.max_health) + '\n' +
"Attack " + str(e.attack) + '\n' +
"Defence " + str(e.defence) + '\n' +
"Evasion " + str(e.evasion))

print ("what do you want to do: ")


while character_health > 0 and enemy_health > 0:
    action = input ("Attack /a, Defend /d ")
    if action == "a":
        enemy_health = enemy_health - (character_attack - enemy_defence)
    if action =="d":
        character_defence += 1
    print ("The " + e.name +"'s health is now " + str(e.health))
    print ("Your defence is now " + str(character_defence))
    print ("The " + e.name + " attacks")
    if e.attack > character_defence:
        character_health = character_health - (e.attack - character_defence)
    else:
        character_health = character_health
    print ("Your health is now " + str(character_health) + " out of " + str(character_mac_health))

if character_health > 0:
    print ("congratulations " + name + " you won the fight")
else:
    print ("aww too bad")
