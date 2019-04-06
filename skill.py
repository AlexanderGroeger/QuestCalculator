skills = []
class Skill:
    def __init__(self, name = 'Untitled', import_file = 'standard', parent = None, spcost = 0,
                stats = None, restoration = None, effects = []):
        self.name = str(name)
        self.import_file = str(import_file)
        self.parent = parent
        self.spcost = int(spcost)
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
            ###
            'pow': 0
        }
        if stats:
            for n, v in stats.items():
                self.stats[n] = v
        self.restoration = {
            # max is a percentage of the entity's max stat
            # missing is a percentage of how much stat is missing from its max
            # damage is a raw set value
            'hp': {
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # hp is changed upon use. Integer if > 1 < else Percent if >0 and <1
            'sp': {
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # sp is changed upon use.
            'hunger': {
                'max': 0,
                'missing': 0,
                'damage': 0
            }, # hunger is changed upon use.
            'targets': None
        }
        if restoration:
            for n,v in restoration.iteritems():
                if n != 'targets':
                    for m,x in v.iteritems():
                        self.restoration[n][m] = x
                else:
                    self.restoration[n] = v
        self.effects = [e for e in effects]
        skills.append(self)
        return self

    def ChangeInfo(self, parent, name, spcost, stats, restoration, effects):
        self.parent = parent
        self.name = name
        self.spcost = spcost
        self.stats = stats
        self.restoration = restoration
        self.effects = effects

    def Delete(self, list = False):
        if list:
            global skills
            skills.remove(self)
        self.parent.skills.remove(self)
        del self
