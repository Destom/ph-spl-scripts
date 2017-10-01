class character:
        def __init__(self,name,health,max_health,attack,defence,evasion):
            self.name = name
            self.health = health
            self.max_health = max_health
            self.attack = attack
            self.defence = defence
            self.evasion = evasion

#Playable characters
hero_name=""
your_character = character(hero_name,10,10,4,2,2)

#NPCs

#opponents
rat = character("Rat",10,10,4,2,2)
rous = character("ROUS(rodent of unusual size)",10,10,6,2,2)
