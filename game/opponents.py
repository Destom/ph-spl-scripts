class opponent:
        def __init__(self,name,health,max_health,attack,defence,evasion):
            self.name = name
            self.health = health
            self.max_health = max_health
            self.attack = attack
            self.defence = defence
            self.evasion = evasion

rat = opponent("Rat",10,10,6,2,2)
rous = opponent("ROUS(rodent of unusual size)",10,10,6,2,2)
