import entity as en
items = {}
item_types = ['weapon','head','chest','back','legs','feet','accessory','item']
class Item:
    def __init__(self, name = 'Untitled', import_file = 'standard', parent = None, stats = None, type = 'None',
                    attack_types = {}, elements = {}, requirements = None, equipped = False, quantity = None,
                    restoration = None, value = None, effects = []):
        self.name = str(name)
        self.import_file = str(import_file)
        self.parent = parent
        self.stats = {
            'hp': 0, # Health Points
            'sp': 0, #
            ###
            'atk': 0, # Attack
            'dfn': 0, # Defense
            ###
            'spatk': 0, # Special Attack
            'spdfn': 0, # Special Defense
            ###
            'acc': 0, # Accuracy
            'eva': 0, # Evasion
            ###
            'crit': 0, # Critical Chance
            'bless': 0, # Blessing
        }
        if stats:
            for n, v in stats.iteritems():
                self.stats[n] = v
        self.type = str(type) # String value, the item is a necklace, bracelet, ring, weapon, armor
        self.attack_types = [n for n in attack_types]
        self.elements = {n: v for n,v in elements.iteritems()} # Use (-1) to represent impervious
        self.requirements = {
            'lvl': [1,-1],
            'ammo': None,
        }
        if requirements:
            for n, v in requirements.iteritems():
                self.requirements[n] = v
        self.equipped = bool(equipped)
        self.quantity = [-1, 1] # Number of copies to be consumed. If -1, item will not be consumed
        # Number of items of the same class allowed to be equipped
        if quantity:
            for i,n in enumerate(quantity):
                self.quantity[i] = n
        self.restoration = {
            # 'max' - Restore percent of max
            # 'lost' - Restore percent of max - current
            # 'fixed' - Restore a fixed number
            'hp': {},
            'sp': {},
            'xp': {},
            'food': {},
            'targets': None
            # Targets is a string. Either 'self', 'team', or 'other'
        }
        if restoration:
            for n,v in restoration.iteritems():
                if n != 'targets':
                    for m,x in v.iteritems():
                        self.restoration[n][m] = x
                else:
                    self.restoration[n] = v
        self.value = {
            'gold': 0,
            'jewels': 0
        }
        if value:
            for n, v in value.iteritems():
                self.value[n] = v
        self.effects = [e for e in effects]

        items[GetNewId()] = self

    def GetId(self):
        return items.index(self)

    def Equip(self, print_on):
        can_equip = True
        for key, value in self.requirements.iteritems():
            if key != 'ammo':
                if key == 'lvl':
                    if self.parent.data[key] < self.requirements[key][0] or self.parent.data[key] > self.requirements[key][1]:
                        can_equip = False
                        break
                else:
                    if self.parent.stats[key] >= self.requirements[key]:
                        can_equip = False
                        break
        if can_equip and self.type not in [a.type for a in self.parent.items if a.equipped]:
            can_equip = False
        if can_equip:
            self.equipped = True
            if print_on:
                print(str(self.parent.name) + ' equipped ' + str(self.name))
        else:
            print('Item cannot be equipped.')

    def Unequip(self):
        self.equipped = False
        for stat, value in self.stats.iteritems():
            self.parent.ChangeStats({stat:-value})
            if stat in self.parent.data.keys():
                self.parent.ChangeData({stat:-value})
        print(str(self.parent.name) + ' unequipped ' + str(self.name))

    def Sell(self):
        if not self.parent:
            print("You can't sell this item if nobody owns it.")
            return
        value = self.value
        self.parent.stats['gold'] += value['gold']
        self.parent.stats['jewels'] += value['jewels']
        print(self.parent.name + ' sold ' + self.name + ' for ' + str(value['gold']) + ' gold and ' + str(value['jewels']) + 'jewels')
        self.Delete()

    def Delete(self):
        if not self.parent:
            del self
            return
        self.parent.items.remove(self)
        del self

def ClearItems():
    global items
    items = []

def GetNewId():
    ids = items.keys()
    print(ids)
    if ids == []:
        print(0)
        return '0'
    else:
        ids = [str(a) for a in range(len(ids)+1) if str(a) not in ids]
        return ids[0]

def ShowNonDefaults(item_list = None):
    global items
    if item_list:
        for i in item_list:
            keys = []
            dummy = CreateItem()
            for key, value in i.iteritems():
                for dkey, dvalue in dummy.iteritems():
                    if key == dkey and value != dvalue: # If we have a unique value log it,
                        keys.append(key)
            for key in keys:
                print(key + ': ' + str(i[key]))
            print('---Next Item---')
        return
    return
