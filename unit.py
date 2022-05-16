from json import load
import random as rd
from enum import Enum
import weapon

unit_id_val = {
     # Allies
    'Roy'       : 0,   
    'Marcus'    : 1,
    'Alen'      : 2,
    'Lance'     : 3,
    'Wolt'      : 4,
    'Bors'      : 5,
    # Enemies
    'Fighter'   : 6,
    'Brigand'   : 7,
    'Archer'    : 8,
    'Damas'     : 9
}

unit_stats = {
    'lvl' : 0,
    'str' : 1,
    'skl' : 2,
    'spd' : 3,
    'lck' : 4,
    'dfn' : 5,
    'res' : 6,
    'con' : 7,
    'mov' : 8}

weapon_stats = {
    'rnk' : 0, 
    'rng' : 1,
    'use' : 2,
    'wgt' : 3,
    'pwr' : 4, 
    'hit' : 5, 
    'crt' : 6, 
    'cst' : 7}

class Cunit:
    def __init__(self, unit_id, start_pos ) -> None:
        with open('data/base_stats.json', 'r') as f:
            self.data = load(f)

        self.id         = unit_id
        self.bases      = self.data['unit_stats'][unit_id]['bases']
        self.growths    = self.data['unit_stats'][unit_id]['growths']
        self.weapons    = self.data['unit_stats'][unit_id]['weapons']
        self.exp        = 0

        # Allied units have a unique start position 
        # If statment is used for setting the start postion of duplicate enemy types
        # IE there are ten enemies of type fighter(ID:)
        if(start_pos):
            self.pos = start_pos
        else:
            self.pos        = self.data['unit_stats'][unit_id]['start_pos']
        return

    # alternate constructor for enemy units, as multiple units share base stats
    # but have different starting position
    def set_pos(self, new_pos):
        self.pos = new_pos
        return

    def check_exp(self, gained_exp):
        if (self.exp + gained_exp) > 99:
            self.level_up()
            self.exp -= 100
        return

    def level_up(self):
        # 10 stats for 10 growths
        
        # Level Increase
        self.bases[0] += 1
        
        # Ensures the player always recieves at least 1 stat gain
        no_gain = True
        
        # Str, skill, speed, luck, def, res
        
        for i in range(1, 6):
            val = rd.randint(0,100)
            if self.growths[i] > val:
                no_gain = False
                self.bases[i] += 1
        print('First Try: ', self.bases)
        if no_gain: # If no stats gained a point roll again for mercy
            for i in range(1, 6):
                val = rd.randint(0,100)
                if self.growths[i] > val:
                    self.bases[i] += 1
            print('Second Try: ', self.bases)
        pass

    def print_data(self):
        print(self.id, '\n')
        print(self.bases, '\n')
        print(self.growths, '\n')
        print(self.weapons, '\n')
        print(self.exp, '\n')
        print(self.pos, '\n')

class Cinventory(Cunit):
    def __init__(self, unit_id) -> None:
        pass

    def gain_item(self):
        pass

    def lose_item(self):
        pass

    def lose_uses(self):
        pass

test = Cunit(unit_id_val['Damas'], [1,1])
test1 = Cunit(unit_id_val['Roy'], False)

test.print_data()
test1.print_data()