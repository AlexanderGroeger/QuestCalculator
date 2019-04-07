import random as rand
import entity as en
effects = {}
class Effect:
    def __init__(self,name = 'NoEffect', import_file = 'standard', parent = None, type = 'Unknown', elements = {},
                effective = 'Always', rounds = 0, chances = None, stack = None,
                stats = None, restoration = None):
        self.name = str(name)
        self.import_file = str(import_file)
        self.parent = parent
        self.type = str(type)
        self.elements = {n: v for n, v in elements.iteritems()}
        self.effective = str(effective) # OnHit, OnAttack, OnStep, Always
        self.rounds = rounds
        self.chances = {
            'apply': 100, # Chance of effect coming on
            'fade': 0, # Chance of effect going away
            'inflict': 100 # Chance of effect being applied
        }
        if chances:
            for n, v in chances.items():
                self.chances[n] = v
        self.stack = str(stack)
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
            'pow': 100
        }
        if stats:
            for n, v in stats.iteritems():
                self.stats[n] = v
        self.restoration = {
            'hp': {
                'fixed': 0,
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # hp is changed upon use. Integer if > 1 < else Percent if >0 and <1
            'sp': {
                'fixed': 0,
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # sp is changed upon use.
            'food': {
                'fixed': 0,
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # food is changed upon use.
            'targets': None
        }
        if restoration:
            for n,v in restoration.iteritems():
                if n != 'targets':
                    for m,x in v.iteritems():
                        self.restoration[n][m] = x
                else:
                    self.restoration[n] = v
        effects[GetNewId()] = self

    def Apply(self):
        # Decrement rounds in necessary
        self.rounds = max(0,self.rounds-1) if self.rounds >= 1 else self.rounds
        entity = self.parent
        if isinstance(ent,sk.Skill):
            return
        elif not isinstance(ent,en.Entity):
            entity = entity.parent
        if self.type == 'DataChange':
            if self.restoration['targets'] == 'Self':
                entity.Restore(self.restoration)
            elif self.restoration['targets'] == 'All':
                for entity2 in en.entities:
                    entity2.Restore(self.restoration)
            elif self.restoration['targets'] == 'Team':
                for entity2 in en.entities:
                    if entity2.player['team'] == entity.player['team']:
                        entity2.Restore(self.restoration)

    def Delete(self, backup = False):
        if backup:
            global effects
            effects.remove(self)
        self.parent.effects.remove(self)
        del self

def GetNewId():
    ids = effects.keys()
    if ids == []:
        return '0'
    else:
        ids = [str(a) for a in range(len(ids)+1) if str(a) not in ids]
        return ids[0]
