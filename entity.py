import item as it
import effect as ef
import random

data = [
'lvl',
'xp',
'hp',
'sp',
'food',
'gold',
'jewels'
]

big_stats = [
    'strength',
    'dexterity',
    'constitution',
    'intelligence',
    'integrity'
]

entities = {}
class Entity:
    def __init__(self, name = "Untitled", import_file = 'standard', player = None, data = None, stats = None,
                    big_stats = None, effects = [], skills = [], items = [], money = None):
        self.name = str(name)
        self.import_file = str(import_file)
        self.player = {
            'team': 'player',
            'class': None,
            'element': None
        }
        if player:
            for n, v in player.iteritems():
                self.player[n] = v
        self.data = {
            'hp': 10,
            'sp': 10,
            'xp': 0,
            'lvl': 1,
            'food': 100,
            'gold': 0,
            'jewels': 0
        }
        if data:
            for n, v in data.iteritems():
                self.data[n] = v
        self.stats = {
            'hp': 10, # (8,9,10,11,12) based on class
            'sp': 10, # Special Points
            ###
            'atk': 1, # Attack
            'dfn': 1, # Defense
            ###
            'spatk': 1, # Special Attack
            'spdfn': 1, # Special Defense
            ###
            'acc': 1, # Accuracy
            'eva': 1, # Evasion
            ###
            'crit': 1, # Critical Chance
            'bless': 1, # Blessing
        }
        if stats:
            for n, v in stats.iteritems():
                self.stats[n] = v
        self.big_stats = {
            'strength': 0,
            'dexterity': 0,
            'constitution': 0,
            'intelligence': 0,
            'integrity': 0
        }
        if big_stats:
            for n, v in big_stats.iteritems():
                self.big_stats[n] = v
        self.skills = [s for s in skills]
        self.effects = [e for e in effects]
        self.items = [i for i in items]

        entities[GetNewId()] = self

    def GetId(self):
        return entities.index(self)

    def ClearEffects(self):
        self.effects = []

    def ChangeData(self, data_list = {}, set = False):
        cur_hp = self.data['hp']

        for d, value in data_list.iteritems():
            if d == 'hp' or d == 'sp':
                dmax = self.stats[d]
            elif d == 'lvl' or d == 'food':
                dmax = 100
            else:
                dmax = 10**9 # Billion max
            if set:
                self.data[d] = int(min(max(value,0),dmax))
            else:
                self.data[d] = int(min(max(self.data[d]+value,0),dmax))

        if cur_hp != 0 and self.data['hp']==0:
            print(self.name + ' has died!')

    def ChangeStats(self, stat_list = {}, set = False):
        for key, value in stat_list.iteritems():
            if set:
                self.stats[key] = max(value,0)
            else:
                self.stats[key] += max(value,0)

    def GiveItem(self,item,equip = False,print_on = False):
        self.items.append(item)
        item.parent = self
        if equip:
            item.Equip(print_on)

    def GiveExp(self, newxp = 0):
        lvl = self.data['lvl']
        curxp = self.data['xp']
        while curxp + newxp >= int(5*((lvl+1)/2+2)**2+5*lvl):
            newxp -= int(5*((lvl+1)/2+2)**2+5*lvl)
            lvl += 1
        self.data['lvl'] = int(min(max(0,lvl),999))
        self.data['xp'] = int(max(0,curxp+newxp))

    def GiveEffects(effects = None):
        for v in effects:
            if isinstance(v, int):
                self.effects.append(ef.effects[v])
                self.effects[self.effects.index(ef.effects[v])].parent = self
            else:
                self.effects.append(v)
                self.effects[self.effects.index(v)].parent = self

    def Restore(self, rd):
        for res, d in rd.iteritems():
            max = d['max']
            miss = d['missing']

            if res != 'food':
                stat_max = 100
            else:
                stat_max = self.stats[res]

            if isinstance(max,int):
                self.data[res] += max
            else:
                self.data[res] += int(stat_max * (1 + max))
            if isinstance(miss,int):
                self.data[res] += miss
            else:
                self.data[res] += int((stat_max - self.data[res]) * (1 + miss))

            self.data[res] = max(0,min(self.data[res],stat_max))

    # def ApplyEffects(self):
    #     for v in self.effects:
    #         # If we have negative rounds left, use v['rounds'] for chance
    #         v['rounds'] = 0 if rand.rand() < abs(v['rounds']) and abs(v['rounds']) < 1 else v['rounds']
    #         # Decrement rounds in necessary
    #         v['rounds'] = max(0,v['rounds']-1) if v['rounds'] >= 1 else v['rounds']
    #         if v['type'] == 'DataChange':
    #             for d, dv in v['stats']:
    #                 max_val = self.stats[d]
    #                 if d == 'food':
    #                     max_val = 100
    #                 if abs(dv)>0 and abs(dv)<1: # If we use a percentage
    #                     self.data[d] = min( max(0,self.data[d]+self.stats[d]*dv), max_val)
    #                 else:
    #                     self.data[d] = min( max(0,self.data[d]+dv), max_val)

def ClearEntities():
    global entities
    entities = []

def GetExpNeededForLevel(level):
    return 10*level*(level+4)

def GetEntityById(id):
    if id in entities.keys():
        return entities[id]
    else:
        return None

def GetNewId():
    ids = entities.keys()
    print(ids)
    if ids == []:
        print(0)
        return '0'
    else:
        ids = [str(a) for a in range(len(ids)+1) if str(a) not in ids]
        return ids[0]
