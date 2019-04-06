import manage as m
import generator as gen
alex = gen.NewRandomEntity(name = 'Alex', type = 'player', lvl = 10, print_on = True)
isaac = gen.NewRandomEntity(name = 'Isaac', type = 'enemy', lvl = 10, print_on = True)
# alex = m.en.Entity('Alex')
# isaac = m.en.Entity('Isaac')
# for entity in m.en.entities:
#     entity.data['lvl'] = gen.RandomNumber(25,35)
#     for n,v in entity.stats.items():
#         entity.stats[n] = gen.RandomNumber(entity.data['lvl'],entity.data['lvl']*2)
#         #print(entity.name + ' has ' + str(entity.stats[n]) + ' ' + n)
#     entity.stats['hp'] = gen.RandomNumber(entity.data['lvl']*10,entity.data['lvl']*20)
#     entity.data['hp'] = entity.stats['hp']
#     entity.data['hunger'] = gen.RandomNumber(60,80)
#     #print(entity.name + ' has ' + str(entity.stats['hp']) + ' hp')
#     elements = gen.rand.sample([e for e, v in m.ba.el.element_matrix.items()],gen.RandomNumber(1,2))
#
#     for i in range(gen.RandomNumber(2,7)):
#         item = gen.NewRandomItem(entity.items, elements = elements, lvl = entity.data['lvl'], noweapon = True)
#         entity.GiveItem(item, True)
#     #elements = gen.rand.sample([e for e, v in m.ba.el.element_matrix.items()],gen.RandomNumber(1,2))
#     item = gen.NewRandomItem(entity.items, elements = elements, lvl = entity.data['lvl'], type = 'weapon')
#     entity.GiveItem(item, True)
        # item = m.it.Item()
        # entity.GiveItem(item)
        # if gen.rand.random()<.5 and len(elements)>0:
        #     for ie in gen.rand.sample(elements,gen.RandomNumber(1,len(elements))):
        #         item.elements[ie] = gen.RandomNumber(1,3)
        #         #print(ie + ': ' + str(item.elements[ie]))
        #     item.name = gen.RandomName(type = 'armor', element = item.elements.keys(), print_on = True)
        # else:
        #     item.name = gen.RandomName(type = 'armor', print_on = True)
        # item.type = item.name.split(' ')[1]
        # item.Equip()
        # for n in gen.rand.sample(['hp','dfn','spdfn','eva','bless'],gen.RandomNumber(1,5)):
        #     item.stats[n] = gen.RandomNumber(10,40)
        #     #print(item.name + ' has ' + str(item.stats[n]) + ' ' + n)

    # weapon = m.it.Item(type = 'weapon')
    # entity.GiveItem(weapon)
    #
    # if gen.rand.random()<1 and len(elements)>0:
    #     for ie in gen.rand.sample(elements,gen.RandomNumber(1,len(elements))):
    #         weapon.elements[ie] = gen.RandomNumber(1,3)
    #         #print(ie + ': ' + str(weapon.elements[ie]))
    #     weapon.name = gen.RandomName(type = 'weapon', element = weapon.elements.keys(), print_on = True)
    # else:
    #     weapon.name = gen.RandomName(type = 'weapon', print_on = False)
    # weapon.Equip()
    # for n in gen.rand.sample(['atk','spatk','acc','crit'],gen.RandomNumber(1,4)):
    #     weapon.stats[n] = gen.RandomNumber(30,80)
    #     #print(weapon.name + ' has ' + str(weapon.stats[n]) + ' ' + n)
for i in range(4):
    phys = gen.rand.choice([False,True])
    spec = gen.rand.choice([False,True])
    if not phys:
        spec = True
    m.ba.Fight(alex,[isaac],None,phys,spec)
    phys = gen.rand.choice([False,True])
    spec = gen.rand.choice([False,True])
    if not phys:
        spec = True
    m.ba.Fight(isaac,[alex],None,phys,spec)
