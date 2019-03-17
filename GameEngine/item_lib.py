class item:
    def __init__(self,name,value,max_health_up,health_up):
        self.name = name
        self.value = value
        self.max_health_up = max_health_up
        self.health_up = health_up

potion = item('potion',10,0,5)
super_potion = item('super_potion',20,0,10)


inventory_basic = ['potion']
inventory_advanced = ['potion','super_potion']
