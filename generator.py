import random as rand
import entity as en
import item as it
import effect as ef
import skill as sk
import names as na
import adjectives as adj
import element as el
import pickle

def RandomEntity(team = None):
    if not team:
        e = rand.choice(en.entities)
    else:
        entities = [a for a in en.entities if e.player.team == team]
        e = rand.choice(entities)
    print(e.name + ' was rolled')
    return e

def NewRandomEntity(name = None, type = 'player', lvl = 50, print_on = False):

    ''' Create Name '''
    if not name:
        name = RandomName(type)
    entity = en.Entity(name)
    if print_on:
        print('___ '+name+' ___\n')

    ''' Assign Stats '''
    entity.data['lvl'] = lvl
    for n,v in entity.stats.items():
        entity.stats[n] = RandomNumber(entity.data['lvl'],entity.data['lvl']*2)
        #print(entity.name + ' has ' + str(entity.stats[n]) + ' ' + n)
    entity.stats['hp'] = RandomNumber(entity.data['lvl']*15,entity.data['lvl']*30)
    entity.data['hp'] = entity.stats['hp']
    entity.data['hunger'] = RandomNumber(20,100)
    #print(entity.name + ' has ' + str(entity.stats['hp']) + ' hp')

    ''' Assign elements '''
    elements = rand.sample([e for e, v in el.element_matrix.items()],RandomNumber(1,2))

    ''' Assign items '''
    type_exclude = ['weapon']
    item = NewRandomItem(entity.items, elements = elements, type = 'weapon', lvl = entity.data['lvl'], print_on = print_on)
    entity.GiveItem(item, True, print_on=False)
    if item.requirements['ammo']:
        item = NewRandomItem(entity.items, elements = elements, type = 'ammo', lvl = entity.data['lvl'], print_on = print_on)
        entity.GiveItem(item, True, print_on = False)
        type_exclude.append('ammo')
    for i in range(RandomNumber(int(lvl**.5),int(lvl**.5)+1)):
        item = NewRandomItem(entity.items, elements = elements, lvl = entity.data['lvl'], exclude = type_exclude, print_on = print_on)
        entity.GiveItem(item, True, print_on = False)

    ''' Assign skills '''
    # for i in range(RandomNumber(0,3)):
    #     entity.skills.append(NewRandomSkill())

    return entity

def NewRandomItem(items = None, elements = None, type = None, exclude = [], lvl = 50, rarity = None, print_on = False):
    item = it.Item()


    ''' Determine type of item '''

    if not type:
        all_types = ['weapon','ammo']+na.types['armor'].keys()+na.types['accessories'].keys()
        if items:
            # Remove any equipped types
            all_types = list(set(all_types)-set([a.type for a in items if a.equipped]))
        all_types = list(set(all_types)-set(exclude))
        type = rand.choice(all_types)
    item.type = type



    ''' Determine stats '''

    main_list = []
    if item.type in na.types['armor'].keys():
        main_list = rand.sample(['dfn','spdfn'],RandomNumber(1,2))
        stat_list = rand.sample(['hp','eva','bless'],RandomNumber(0,3))

    elif item.type == 'weapon' or item.type == 'ammo':
        main_list = rand.sample(['atk','spatk'],RandomNumber(1,2))
        stat_list = rand.sample(['acc','crit'],RandomNumber(0,2))

    elif item.type in na.types['accessories'].keys():
        stat_list = rand.sample(['hp','dfn','spdfn','eva','bless','sp','atk','spatk','acc','crit'],RandomNumber(1,4))

    for n in stat_list:
        if n == 'hp':
            item.stats[n] = RandomNumber(int(lvl*4),int(lvl*10))
        else:
            item.stats[n] = RandomNumber(int(lvl)/5,int(lvl/2))
    for n in main_list:
        if n == 'atk' or n == 'spatk':
            item.stats[n] = RandomNumber(int(lvl)*2,int(lvl*4))
        else:
            item.stats[n] = RandomNumber(int(lvl),int(lvl*2))


    ''' Determine requirements '''

    for stat in rand.sample(item.stats.keys(),RandomNumber(0,len([a for a,v in item.stats.items() if v!=0]) ) ):
        item.requirements[stat] = RandomNumber(int(lvl),int(lvl*2))

    if rand.random()<.25:
        item.requirements['lvl'] = [lvl - RandomNumber(1,7), lvl + RandomNumber(1,7)]
    else:
        item.requirements['lvl'] = [lvl - RandomNumber(0,7), -1]

    if rand.random()<.25 and item.type == 'weapon':
        item.requirements['ammo'] = True


    ''' Determine elements '''

    if not elements:
        elements = rand.sample([e for e, v in el.element_matrix.items()],RandomNumber(0,2))
    if len(elements)>0:
        for ie in rand.sample(elements,RandomNumber(0,len(elements))):
            item.elements[ie] = RandomNumber(1,2)
            #print(ie + ': ' + str(item.elements[ie]))
        if len(item.elements.keys()) > 0:
            item.name = RandomName(type = item.type, requires_ammo = item.requirements['ammo'], element = item.elements.keys(), print_on = False)
        else:
            item.name = RandomName(type = item.type, requires_ammo = item.requirements['ammo'], print_on = False)
    else:
        item.name = RandomName(type = item.type, requires_ammo = item.requirements['ammo'], print_on = False)
    if print_on:
        print('___ '+item.name + ' ___\n' + str({a:v for a, v in item.stats.items() if v != 0}) + '\n' + str({a:v for a, v in item.requirements.items() if v != 0}) + '\n' + str(item.elements) + '\n')


    return item

def RandomItem(type = None):
    if not type:
        i = rand.choice(it.items)
    else:
        items = [a for a in it.items if e.type == type]
        i = rand.choice(items)
    print(i.name + ' was rolled')
    return i

def RandomEffect(type = None):
    if not type:
        e = rand.choice(ef.effects)
    else:
        effects = [a for a in ef.effects if e.type == type]
        e = rand.choice(effects)
    print(e.name + ' was rolled')
    return e

def NewRandomSkill(type = None, elements = []):
    ns = sk.Skill(RandomName())
    return ns

def RandomSkill(type = None):
    if not type:
        s = rand.choice(sk.skills)
    else:
        skills = [a for a in sk.skills if s.type == type]
        s = rand.choice(skills)
    print(s.name + ' was rolled')
    return s

def RandomName(type = 'player', element = None, requires_ammo = False, print_on = False):
    if type == 'player':
        file = open('names.pickle','rb')
        names = pickle.load(file)
        n = rand.choice(names).rstrip('\n').rstrip('\r')
        file.close()
        if print_on:
            print(n + ' was rolled')
    else:
        if not element:
            element = 'None'
        if not isinstance(element,str):
            element = rand.choice(element)
        iadj = rand.choice(adj.adjectives[element])
        if type == 'weapon':
            if requires_ammo:
                noun = rand.choice(na.types['weapon']['ranged (ammo)'])
            else:
                noun = rand.choice([a for a in na.types['weapon'].keys() if a!='ranged (ammo)'])
                noun = rand.choice(na.types['weapon'][noun])
        elif type == 'ammo':
            noun = rand.choice(na.types['ammo'])
        elif type in na.types['armor'].keys():
            noun = rand.choice(na.types['armor'][type])
        elif type in na.types['accessories'].keys():
            noun = rand.choice(na.types['accessories'][type])

        n = iadj + ' ' + noun
        if print_on:
            print(n + ' was rolled')
    return n

def RandomNumber(a = 1, b = 100, print_on = False):
    r = rand.randint(a,b)
    if print_on:
        print(str(r) + ' was rolled')
    return r

def RandomRarity(bonus = 0):
    r = rand.random()
    rarities = [
    [53.5,-23.5],
    [25,6],
    [15,10],
    [5,4.8],
    [1,2],
    [.4,.6],
    [.1,.1]
    ]
    rarity_level = 0
    for rarity in rarities:
        if r < rarity[0]+rarity[1]*(1.0-(100.0/99.0)**(-.2)):
            break
        else:
            rarity_level += 1
    return rarity_level
#RandomName()
#RandomItem()
