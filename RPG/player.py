class player:
    def __init__(self,rpg_val, name = 'no name'):
        self.name = name
        rpg_types = ['mage','hunter','merc','no type']
        self.rpg_type = rpg_types[rpg_val]
        self.attack = 100   # attack power
        self.atk = 10
        self.defence = 100
        self.maxhp = 100
        self.hp = self.maxhp
        self.level = 1
        self.exp = 0

        if rpg_val == 0:
            self.maxhp -= 20
            self.hp = self.maxhp
            self.attack += 40
            self.defence -= 20
        elif rpg_val == 1:
            self.maxhp -= 20
            self.hp = self.maxhp
            self.attack -= 20
            self.defence += 40
        elif rpg_val == 2:
            self.maxhp += 40
            self.hp = self.maxhp
            self.attack -= 20
            self.defence -= 20

    def show(self):
        print('type',self.rpg_type)
        print('level',self.level)
        print(self.hp, self.attack, self.defence)