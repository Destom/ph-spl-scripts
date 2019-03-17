import character
import Action-lib

class character:
        def __init__(self,name,health,max_health,attack,defence,evasion):
            self.name = name
            self.health = health
            self.max_health = max_health
            self.attack = attack
            self.defence = defence
            self.evasion = evasion

rat = character("Rat",10,10,4,2,2)
rous = character("ROUS(rodent of unusual size)",10,10,6,2,2)




#name = input("what is your name :")
name = "Destom"
print ("hello " + name)
your_character = character(name,10,10,4,2,2)

print  ("Your stats are \n Health " + str(your_character.health) + " out of " + str(your_character.max_health) + '\n' + "Attack " + str(your_character.attack) + '\n' + "Defence " + str(your_character.defence) + '\n' + "Evasion " + str(your_character.evasion) + '\n' + '\n' + '\n')


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


while your_character.health > 0 and enemy_health > 0:
    action = input ("Attack /a, Defend /d ")
    if action == "a":
        enemy_health = enemy_health - (your_character.attack - enemy_defence)
    if action =="d":
        your_character.defence += 1
    print ("The " + e.name +"'s health is now " + str(e.health))
    print ("Your defence is now " + str(your_character.defence))
    print ("The " + e.name + " attacks")
    if e.attack > your_character.defence:
        your_character.health = your_character.health - (e.attack - your_character.defence)
    else:
        your_character.health = your_character.health
    print ("Your health is now " + str(your_character.health) + " out of " + str(your_character.max_health))



if character_health > 0:
    print ("congratulations " + name + " you won the fight")
else:
    print ("aww too bad")
