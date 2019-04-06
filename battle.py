import random as rand
import entity as en
import element as el
import time

def Step():

    ''' For all entities, apply step '''
    for entity in en.entities:

        entity.data['hunger'] -= 1

        ''' For each item on entity '''
        for item in entity.items:

            ''' Apply effects if necessary '''
            for effect in item.effects:
                if effect.effective == 'OnStep' and effect.parent:
                    if rand.random() < effect.chances['inflict']:
                        effect.Apply()
                    if rand.random() < effect.chances['off']:
                        effect.Delete()

            ''' Apply restoration if necessary '''
            if item.restoration['targets'] == 'Self':
                entity.Restore(item.restoration)
            elif item.restoration['targets'] == 'All':
                for entity2 in en.entities:
                    entity2.Restore(item.restoration)
            elif item.restoration['targets'] == 'Team':
                for entity2 in en.entities:
                    if entity2.player['team'] == entity.player['team']:
                        entity.Restore(item.restoration)


        ''' For each effect on entity, apply if necessary '''
        for effect in entity.effects:
            if effect.effective == 'OnStep' and effect.parent:
                if rand.random() < effect.chances['inflict']:
                    effect.Apply()
                if rand.random() < effect.chances['off']:
                    effect.Delete()




def Fight(attacker = None, defenders = [], skill = None, physical = True, special = False):

    ''' Validate attacker and defenders exist '''
    if not attacker or len(defenders)==0:
        return

    # It's possible to hit multiple entities! More targets means less damage!
    tgtr = int(100/(len(defenders)**.5))/100

    ''' Main loop for attacking each defender '''
    print(attacker.name + ' is attacking ' + ', '.join([a.name for a in defenders]) )

    ''' Get the equipped items from the attacker '''
    ateq = [i for i in attacker.items if i.equipped]

    ''' Read attacker's stats '''
    a_stats = attacker.stats
    atk = a_stats['atk']
    spatk = a_stats['spatk']
    acc = a_stats['acc']
    crit = a_stats['crit']
    lvl = attacker.data['lvl']


    # ''' Read stats from attacker's items '''
    # for item in ateq:
    #     atk+=item.stats['atk']
    #     spatk+=item.stats['spatk']
    #     acc+=item.stats['acc']
    #     crit+=item.stats['crit']


    ''' Read stats from attacker's effects '''
    for effect in attacker.effects:
        if effect.effective != "OnAttack":
            if isinstance(effect.stats['atk'], int):
                atk+=v
            else:
                atk*=v
            if isinstance(effect.stats['spatk'], int):
                spatk+=v
            else:
                spatk*=v
            if isinstance(effect.stats['acc'], int):
                acc+=v
            else:
                acc*=v
            if isinstance(effect.stats['crit'], int):
                crit+=v
            else:
                crit*=v


    ''' Read stats from skill '''
    if skill:
        print(attacker.name + ' is using a skill')
        if attacker.data['sp'] < skill.spcost:
            print(attacker.name + ' does not have enough sp to use ' + skill.name)
            skill = None
        else:
            # Charge attacker for using a skill
            attacker.ChangeData('sp', -skill.spcost)
            atk+=skill.stats['atk']
            dfn+=skill.stats['dfn']
            spatk+=skill.stats['spatk']
            spdfn+=skill.stats['spdfn']
            acc+=skill.stats['acc']
            eva+=skill.stats['eva']
            crit+=skill.stats['crit']
            bless+=skill.stats['bless']
            print(attacker.name + ' used ' + str(skill.spcost) + ' sp to use ' + skill.name)
            pow = skill.stats['pow']
    else:
        pow = 1


    ''' Calculate Efficiency '''
    eff = CalculateEfficiency(attacker.data['hunger'])


    for defender in defenders:

        ''' Get the equipped items from the defender '''
        dfeq = [e for e in defender.items if e.equipped]
        #print('___ '+ns.name + ' ___\n' + str({a:v for a, v in ns.stats.items() if v != 0}) + '\n' + str(ns.elements) + '\n' for ns in dfeq)


        ''' Read defender's stats '''
        d_stats = defender.stats
        dfn = d_stats['dfn']
        spdfn = d_stats['spdfn']
        eva = d_stats['eva']
        bless = d_stats['bless']


        # ''' Read stats from defender's items '''
        # for item in dfeq:
        #     dfn+=item.stats['dfn']
        #     spdfn+=item.stats['spdfn']
        #     eva+=item.stats['eva']
        #     bless+=item.stats['bless']


        ''' Read stats from defender's effects '''
        for effect in defender.effects:
            if effect.effective != "OnAttack":
                if isinstance(effect.stats['dfn'], int):
                    dfn+=v
                else:
                    dfn*=v
                if isinstance(effect.stats['spdfn'], int):
                    spdfn+=v
                else:
                    spdfn*=v
                if isinstance(effect.stats['eva'], int):
                    eva+=v
                else:
                    eva*=v
                if isinstance(effect.stats['bless'], int):
                    bless+=v
                else:
                    bless*=v

        print(attacker.name + ' has %d hp, %d attack, %d special attack, %d accuracy, and %d crit.' % (attacker.data['hp'],atk,spatk,acc,crit))
        print(defender.name + ' has %d hp, %d defense, %d special defense, %d evasion, and %d blessing.' % (defender.data['hp'],dfn,spdfn,eva,bless))

        print('Efficiency is %.1f' % (int(eff*1000)/10.0) + '%')

        ''' Calculate Hit Chance '''
        hit = CalculateAccuracy(acc,eva)
        print('Accuracy is %.1f' % (int(hit*eff*1000)/10.0) + '%')
        if hit * eff < rand.random():
            print(attacker.name + ' missed!')
            return False
        print(attacker.name + ' landed an attack on ' + defender.name + '!')

        if physical:
            ''' Calculate Initial Physical Damage '''
            dmg = CalculateDamage(lvl,pow,atk,dfn)
            print('Initial physical damage is %d' % dmg)


        if special:
            ''' Calculate Initial Special Damage '''
            sdmg = CalculateDamage(lvl,pow,spatk,spdfn)
            print('Initial special damage is %d' % sdmg)


        ''' Calculate Critical Chance '''
        cc = CalculateCritical(crit,bless)
        print('Crit chance is %.1f' % (int(cc*1000)/10.0) + '%')
        if cc * eff > rand.random():
            print(attacker.name + ' got a critical hit!')
            if physical:
                dmg *= 1.5
            if special:
                sdmg *= 1.5
        elif cc * eff / 10 > rand.random():
            print(attacker.name + ' got a deadly hit!')
            if physical:
                dmg *= 2
            if special:
                sdmg *= 2


        ''' Calculate Elemental Bonus '''
        elb = CalculateElementBonus(ateq,dfeq)
        print('Elemental Bonus is ' + str(elb) + 'x')

        ''' Multiply our damage by our efficiency, target ratio, element bonus, and randomness '''
        if physical:
            dmg = int( dmg * eff * tgtr * elb * (rand.random()/10 + .9))
            print('Total physical damage is %d' % dmg)
        if special:
            sdmg = int( sdmg * eff * tgtr * elb * (rand.random()/10 + .9) )
            print('Total special damage is %d' % sdmg)


        ''' Process hit damage '''
        tdmg = 0
        if physical:
            tdmg+=dmg
        if special:
            tdmg+=sdmg
        defender.ChangeData({'hp': -tdmg})
        print(defender.name + ' took ' + str(tdmg) + ' damage from ' + attacker.name)


        ''' Effects wear off defender '''
        for effect in defender.effects:
            if effect.chances['off'] > rand.random() or effect.rounds == 0:
                defender.effects.remove(effect)
                del effect


        ''' Apply effects from skill '''
        if skill:
            for effect in skill.effects:
                if effect.chances['on'] >= rand.random():
                    if effect.stack and effect in defender.effects:
                        if effect.stack == 'duplicate':
                            defender.effects.append(effect)
                            effect.parent = defender
                        elif effect.stack == 'additive':
                            defender.effects[defender.effects.index(effect)].rounds += effect.rounds
                        elif effect.stack == 'refresh':
                            defender.effects[defender.effects.index(effect)].rounds = effect.rounds
                    elif effect not in defender.effects:
                        defender.effects.append(effect)
                        effect.parent = defender


        ''' Apply effects from items '''
        for item in ateq:
            for effect in item.effects:
                if effect.chances['on'] >= rand.random():
                    if effect.stack and effect in defender.effects:
                        if effect.stack == 'duplicate':
                            defender.effects.append(effect)
                            effect.parent = defender
                        elif effect.stack == 'additive':
                            defender.effects[defender.effects.index(effect)].rounds += effect.rounds
                        elif effect.stack == 'refresh':
                            defender.effects[defender.effects.index(effect)].rounds = effect.rounds
                    elif effect not in defender.effects:
                        defender.effects.append(effect)
                        effect.parent = defender


        ''' Apply damage hp for defender '''
        for item in dfeq:
            dr = item.restoration['hp']['damage']
            if abs(dr) < 1 and abs(dr) != 0:
                defender.ChangeData({'hp': (tdmg)*dr})
            elif abs(dr) != 0:
                defender.ChangeData({'hp': dr})

        ''' Apply damage hp for attacker '''
        for item in ateq:
            dr = item.restoration['hp']['damage']
            if abs(dr) < 1 and abs(dr) != 0:
                attacker.ChangeData({'hp': (tdmg)*dr})
            elif abs(dr) != 0:
                attacker.ChangeData({'hp': dr})

        Step()




def CalculateAccuracy(acc,eva):
    return (4*acc + eva/10.0) / ( (1.25*eva)**0.9 + 4*acc)

def CalculateDamage(lvl = 1, pow = 1, atk = 1, dfn = 1):
    return int( ((2*lvl + 50) * pow * atk ** 1.5) / (5.0 * dfn + 275) ) + 2

def CalculateCritical(crit, bless):
    return (crit**1.1-bless)/(90.0*(bless**0.8+25)) + 1/30.0

def CalculateEfficiency(hung):
    if hung<=75:
        return (4.0/3*(hung/100.0))**0.25
    return 1

def CalculateElementBonus(ateq = [],dfeq = []):
    atk = {}
    dfn = {}
    atk_b = 3.0
    dfn_b = 3.0
    # Collect totals from both
    for item in ateq:
        if item.stats['atk']>0 or item.stats['spatk']>0:
            for element, con in item.elements.items():
                if con < 0:
                    atk[element] = con
                else:
                    if element not in atk.keys():
                        atk[element] = 0
                    atk[element] += con

    for item in dfeq:
        if item.stats['dfn']>0 or item.stats['spdfn']>0:
            for element, con in item.elements.items():
                if con < 0:
                    dfn[element] = con
                else:
                    if element not in dfn.keys():
                        dfn[element] = 0
                    dfn[element] += con
    print(atk)
    print(dfn)
    for element, con in atk.items():
        for element2, con2 in dfn.items():
            if con2 < 0 and element == element2:
                print(element2 + ' has immunity')
            else:
                if element2 in el.Disadvantages(element):
                    dfn_b += (con*con2)**.5
                if element2 in el.Advantages(element):
                    atk_b += (con*con2)**.5
    return int(1000*(atk_b/dfn_b)**.5)/1000.0

def TestAttack():
    for a in range(10,500,10):
        for d in range(10,500,10):
            print(str(a) + ' atk and ' + str(d) + ' dfn = ' + CalculateDamage(lvl,pow,atk,dfn) + '%')
            time.sleep(.1)
