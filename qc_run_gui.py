ENEMY = 'enemy'
PLAYER = 'player'
DATACHANNEL = 256

import copy

from PyQt5 import QtCore, QtGui, QtWidgets
import img_gui
import qt_gui

import entity
import item
import skill
import effect
import battle
import manage
import generator

from pygame import mixer
mixer.init()
mixer.music.load('.\\QCGUI\\JourneysUntold.mid')
mixer.music.play(99)

SELECT_SOUND = mixer.Sound('.\\QCGUI\\Select.wav')
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = qt_gui.Ui_MainWindow()
ui.setupUi(MainWindow)

last_selected_entity = None
delete_player_confirmation = False
delete_enemy_confirmation = False
entity_stats_change_type = 0
entity_stats_check_boxes = {
    "gold": ui.entity_change_status_gold,
    "jewels": ui.entity_change_status_jewels,
    "xp": ui.entity_change_status_exp,
    "hp": ui.entity_change_status_hp,
    "sp": ui.entity_change_status_sp,
    "food": ui.entity_change_status_food,
    "strength": ui.entity_change_status_strength,
    "dexterity": ui.entity_change_status_dexterity,
    "constitution": ui.entity_change_status_constitution,
    "intelligence": ui.entity_change_status_intelligence,
    "integrity": ui.entity_change_status_integrity,
}

last_selected_item = None
delete_item_confirmation = False

save_file = None

def OutputPrint(msg):
    print(msg)
    ui.output_list.addItem(msg)
    if ui.output_list.count() > 150:
        item = ui.output_list.takeItem(0)
        del item

def UpdateEntityGui(player_list_item = None):
    global last_selected_entity
    if player_list_item:
        last_selected_entity = player_list_item.data(DATACHANNEL)
    if not last_selected_entity:
        return None

    ui.entity_name_box.setText(last_selected_entity.name)
    ui.entity_level_box.setValue(last_selected_entity.data['lvl'])
    ui.entity_element_label.setText(str(last_selected_entity.player['element']))
    ui.entity_exp_bar.setMaximum(entity.GetExpNeededForLevel(last_selected_entity.data['lvl']))
    ui.entity_exp_bar.setValue(last_selected_entity.data['xp'])
    ui.entity_gold_box.setValue(last_selected_entity.data['gold'])
    ui.entity_jewels_box.setValue(last_selected_entity.data['jewels'])
    ui.entity_hp_bar.setMaximum(last_selected_entity.stats['hp'])
    ui.entity_hp_bar.setValue(last_selected_entity.data['hp'])
    ui.entity_sp_bar.setMaximum(last_selected_entity.stats['sp'])
    ui.entity_sp_bar.setValue(last_selected_entity.data['sp'])
    ui.entity_food_bar.setValue(last_selected_entity.data['food'])
    ui.entity_attack_box.setValue(last_selected_entity.stats['atk'])
    ui.entity_defense_box.setValue(last_selected_entity.stats['dfn'])
    ui.entity_special_attack_box.setValue(last_selected_entity.stats['spatk'])
    ui.entity_special_defense_box.setValue(last_selected_entity.stats['spdfn'])
    ui.entity_accuracy_box.setValue(last_selected_entity.stats['acc'])
    ui.entity_evasion_box.setValue(last_selected_entity.stats['eva'])
    ui.entity_critical_box.setValue(last_selected_entity.stats['crit'])
    ui.entity_blessing_box.setValue(last_selected_entity.stats['bless'])
    ui.entity_strength_box.setValue(last_selected_entity.big_stats['strength'])
    ui.entity_dexterity_box.setValue(last_selected_entity.big_stats['dexterity'])
    ui.entity_constitution_box.setValue(last_selected_entity.big_stats['constitution'])
    ui.entity_intelligence_box.setValue(last_selected_entity.big_stats['intelligence'])
    ui.entity_integrity_box.setValue(last_selected_entity.big_stats['integrity'])

def ChangeEntityName(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.name = object
    # ui.entity_name_box.setText(last_selected_entity.name)
    if last_selected_entity.player['team'] == PLAYER:
        if ui.player_list.currentItem():
            ui.player_list.currentItem().setText(last_selected_entity.name)
    elif last_selected_entity.player['team'] == ENEMY:
        if ui.enemy_list.currentItem():
            ui.enemy_list.currentItem().setText(last_selected_entity.name)


def ChangeEntityLevel(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.data['lvl'] = int(object)
    ui.entity_level_box.setValue(int(last_selected_entity.data['lvl']))
    ui.entity_exp_bar.setMaximum(entity.GetExpNeededForLevel(int(last_selected_entity.data['lvl'])))

def ChangeEntityXP(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.GiveExp(max(0,object-last_selected_entity.data['xp']))
    ui.entity_exp_bar.setValue(int(last_selected_entity.data['xp']))
    ui.entity_exp_bar.setMaximum(entity.GetExpNeededForLevel(int(last_selected_entity.data['lvl'])))
    ui.entity_level_box.setValue(int(last_selected_entity.data['lvl']))

def ChangeEntityGold(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.data['gold'] = int(object)
    ui.entity_gold_box.setValue(int(last_selected_entity.data['gold']))

def ChangeEntityJewels(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.data['jewels'] = int(object)
    ui.entity_jewels_box.setValue(int(last_selected_entity.data['jewels']))

def ChangeEntityHP(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    object = max(min(int(object),int(last_selected_entity.stats['hp'])),0)
    last_selected_entity.data['hp'] = object
    ui.entity_hp_bar.setValue(object)
    ui.entity_hp_bar.setMaximum(int(last_selected_entity.stats['hp']))

def ChangeEntitySP(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    object = max(min( int(object), int(last_selected_entity.stats['sp']) ),0)
    last_selected_entity.data['sp'] = object
    ui.entity_sp_bar.setValue(object)
    ui.entity_sp_bar.setMaximum(int(last_selected_entity.stats['sp']))

def ChangeEntityFood(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    object = max(min(int(object),100),0)
    last_selected_entity.data['food'] = object
    ui.entity_sp_bar.setValue(object)
    ui.entity_sp_bar.setMaximum(100)

def ChangeEntityStrength(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.big_stats['strength'] = int(object)
    ui.entity_strength_box.setValue(int(last_selected_entity.big_stats['strength']))

def ChangeEntityDexterity(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.big_stats['dexterity'] = int(object)
    ui.entity_dexterity_box.setValue(int(last_selected_entity.big_stats['dexterity']))

def ChangeEntityConstitution(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.big_stats['constitution'] = int(object)
    ui.entity_constitution_box.setValue(int(last_selected_entity.big_stats['constitution']))

def ChangeEntityIntelligence(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.big_stats['intelligence'] = int(object)
    ui.entity_intelligence_box.setValue(int(last_selected_entity.big_stats['intelligence']))

def ChangeEntityIntegrity(object):
    global last_selected_entity
    if not last_selected_entity:
        return None
    last_selected_entity.big_stats['integrity'] = int(object)
    ui.entity_integrity_box.setValue(int(last_selected_entity.big_stats['integrity']))

entity_stats_functions = {
    "gold": ChangeEntityGold,
    "jewels": ChangeEntityJewels,
    "xp": ChangeEntityXP,
    "hp": ChangeEntityHP,
    "sp": ChangeEntitySP,
    "food": ChangeEntityFood,
    "strength": ChangeEntityStrength,
    "dexterity": ChangeEntityDexterity,
    "constitution": ChangeEntityConstitution,
    "intelligence": ChangeEntityIntelligence,
    "integrity": ChangeEntityIntegrity,
}

def AddEntityToList(ent):
    global last_selected_entity
    if isinstance(ent,entity.Entity):
        last_selected_entity = ent
        new_list_item = QtWidgets.QListWidgetItem()
        new_list_item.setData(DATACHANNEL,ent)
        new_list_item.setText(ent.name)
        new_list_item.setTextAlignment(4)
        if ent.player['team'] == PLAYER:
            ui.player_list.clearSelection()
            ui.player_list.clearFocus()
            ui.player_list.addItem(new_list_item)
            ui.player_list.setCurrentItem(new_list_item)
        elif ent.player['team'] == ENEMY:
            ui.enemy_list.clearSelection()
            ui.enemy_list.clearFocus()
            ui.enemy_list.addItem(new_list_item)
            ui.enemy_list.setCurrentItem(new_list_item)
        UpdateEntityGui(new_list_item)

def MakeEntity(team):
    new_entity = entity.Entity()
    new_entity.player['team'] = team
    OutputPrint("Created new " + team)
    AddEntityToList(new_entity)

def ToggleEntityDeleteMode(team):
    global delete_player_confirmation
    global delete_enemy_confirmation
    if team == PLAYER:
        if delete_player_confirmation:
            ui.player_add_button.setText("Add")
            ui.player_copy_button.setText("Copy")
            ui.player_delete_button.setText("Delete")
        else:
            ui.player_add_button.setText("Yes")
            ui.player_copy_button.setText("No")
            ui.player_delete_button.setText("Del?")
        delete_player_confirmation = not delete_player_confirmation
    elif team == ENEMY:
        if delete_enemy_confirmation:
            ui.enemy_add_button.setText("Add")
            ui.enemy_copy_button.setText("Copy")
            ui.enemy_delete_button.setText("Delete")
        else:
            ui.enemy_add_button.setText("Yes")
            ui.enemy_copy_button.setText("No")
            ui.enemy_delete_button.setText("Del?")
        delete_enemy_confirmation = not delete_enemy_confirmation

def CopyEntity(team):
    new_entity = None
    if team == PLAYER:
        new_entity = ui.player_list.currentItem()
    elif team == ENEMY:
        new_entity = ui.enemy_list.currentItem()
    if new_entity:
        new_entity = copy.deepcopy(new_entity.data(DATACHANNEL))
        entity.entities[entity.GetNewId()] = new_entity
        OutputPrint("Copied " + new_entity.name + " to " + team + " list")
    else:
        return None
    AddEntityToList(new_entity)

def DeleteEntity(team):
    # Update gui buttons
    ToggleEntityDeleteMode(team)
    # Pick a list based on team
    team_list = None
    if team == PLAYER:
        team_list = ui.player_list
    elif team == ENEMY:
        team_list = ui.enemy_list

    # Retireve the entity in the list
    old_entity = team_list.currentItem()
    print(old_entity)
    if old_entity:
        # Get the entity data that is being pointed to
        old_entity = old_entity.data(DATACHANNEL)
        OutputPrint("Deleted " + old_entity.name + " from "+team+" list")
        # Find the id of the entity
        entity_id = None
        for key, value in entity.entities.iteritems():
            if value is old_entity:
                entity_id = key
                break
        # if we can delete the entity then do so
        if entity_id in entity.entities.keys():
            del entity.entities[entity_id]
    else:
        return None

    # Now we need to destroy the item from the GUI
    row = team_list.currentRow()
    if row is None:
        return None
    destroyed_item = team_list.takeItem(row)
    del destroyed_item

    if row > 0:
        # Put the focus on the previous entity
        team_list.setCurrentRow(row-1)

        # Update the last selected entity and the stats GUI
        old_entity = team_list.item(team_list.currentRow())
        global last_selected_entity
        if old_entity:
            last_selected_entity = old_entity.data(DATACHANNEL)
        else:
            last_selected_entity = None
        UpdateEntityGui()

def EntityAddButtonPressed(team):
    global delete_player_confirmation
    global delete_enemy_confirmation
    if (team == PLAYER and delete_player_confirmation) or (team == ENEMY and delete_enemy_confirmation):
        DeleteEntity(team)
    else:
        MakeEntity(team)

def EntityCopyButtonPressed(team):
    global delete_player_confirmation
    global delete_enemy_confirmation
    if (team == PLAYER and delete_player_confirmation) or (team == ENEMY and delete_enemy_confirmation):
        ToggleEntityDeleteMode(team)
    else:
        CopyEntity(team)

def UpdateEntityChangeStatsBox(type):
    global entity_stats_change_type
    global entity_stats_check_boxes
    if type > 1:
        for stat in ['gold','jewels','strength','dexterity','constitution','intelligence','integrity']:
            entity_stats_check_boxes[stat].setChecked(False)
            entity_stats_check_boxes[stat].setCheckable(False)

    else:
        for stat in ['gold','jewels','strength','dexterity','constitution','intelligence','integrity']:
            entity_stats_check_boxes[stat].setCheckable(True)
        # If type is Fixed, then no suffix
        if type == 0:
            ui.entity_stats_change_box.setSuffix("")
        else:
            ui.entity_stats_change_box.setSuffix(" %")
    entity_stats_change_type = type

def EntityChangeStats(type):
    global entity_stats_check_boxes
    global entity_stats_change_type
    global last_selected_entity

    if not last_selected_entity:
        return None
    gui_val = int(ui.entity_stats_change_box.value())
    stat_val = 0
    if type == "Add":
        for stat, box in entity_stats_check_boxes.iteritems():
            if box.isChecked():
                if stat in entity.big_stats:
                    stat_val = last_selected_entity.big_stats[stat]
                elif stat in entity.data:
                    stat_val = last_selected_entity.data[stat]
                # If stats change type is fixed, just use raw value
                if entity_stats_change_type == 0:
                    entity_stats_functions[stat](stat_val+gui_val)
                # Add Percentage of current value
                elif entity_stats_change_type == 1:
                    entity_stats_functions[stat](int(stat_val*(1.0+gui_val/100.0)))

                elif stat in ['hp','sp','xp','food']:
                    # Food can only be maxed at 100
                    if stat == 'food':
                        # Add Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(stat_val+(100-stat_val)*(gui_val/100.0)))
                        # Add Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int(stat_val+(100)*(gui_val/100.0)))
                    # Xp is special
                    elif stat == 'xp':
                        # Add Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(stat_val+(entity.GetExpNeededForLevel(last_selected_entity.data['lvl'])-stat_val)*(gui_val/100.0)))
                        # Add Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int(stat_val+(entity.GetExpNeededForLevel(last_selected_entity.data['lvl']))*(gui_val/100.0)))
                    else:
                        # Add Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(stat_val+(last_selected_entity.stat[stat]-stat_val)*(gui_val/100.0)))
                        # Add Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int(stat_val+(last_selected_entity.stat[stat])*(gui_val/100.0)))
    elif type == "Set":
        for stat, box in entity_stats_check_boxes.iteritems():
            if box.isChecked():
                if stat in entity.big_stats:
                    stat_val = last_selected_entity.big_stats[stat]
                elif stat in entity.data:
                    stat_val = last_selected_entity.data[stat]
                # If stats change type is fixed, just use raw value
                if entity_stats_change_type == 0:
                    entity_stats_functions[stat](gui_val)
                # Set Percentage of current value
                elif entity_stats_change_type == 1:
                    entity_stats_functions[stat](int(stat_val*(gui_val/100.0)))

                elif stat in ['hp','sp','xp','food']:
                    # Food can only be maxed at 100
                    if stat == 'food':
                        # Set Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(100-(100-stat_val)*(gui_val/100.0)))
                        # Set Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int((100)*(gui_val/100.0)))
                    # Xp is special
                    elif stat == 'xp':
                        # Set Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(entity.GetExpNeededForLevel(last_selected_entity.data['lvl'])-(entity.GetExpNeededForLevel(last_selected_entity.data['lvl'])-stat_val)*(gui_val/100.0)))
                        # Set Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int((entity.GetExpNeededForLevel(last_selected_entity.data['lvl']))*(gui_val/100.0)))
                    else:
                        # Set Percentage of missing from max value
                        if entity_stats_change_type == 2:
                            entity_stats_functions[stat](int(last_selected_entity.stat[stat]+(last_selected_entity.stat[stat]-stat_val)*(gui_val/100.0)))
                        # Set Percentage of max value
                        elif entity_stats_change_type == 3:
                            entity_stats_functions[stat](int((last_selected_entity.stat[stat])*(gui_val/100.0)))

def UpdateItemGui(item_list_item = None):
    global last_selected_item
    if item_list_item:
        last_selected_item = item_list_item.data(DATACHANNEL)
    if not last_selected_item:
        return None

    ui.item_name_box.setText(last_selected_item.name)
    ui.item_level_box.setValue(last_selected_item.requirements['lvl'][0])
    ui.item_max_level_box.setValue(last_selected_item.requirements['lvl'][1]%1000)
    # ui.item_element_label.setText(str(last_selected_entity.player['element']))
    # ui.item_exp_bar.setMaximum(entity.GetExpNeededForLevel(last_selected_entity.data['lvl']))
    # ui.item_exp_bar.setValue(last_selected_entity.data['xp'])
    # ui.item_gold_box.setValue(last_selected_entity.data['gold'])
    # ui.item_jewels_box.setValue(last_selected_entity.data['jewels'])
    # ui.item_hp_bar.setMaximum(last_selected_entity.stats['hp'])
    # ui.item_hp_bar.setValue(last_selected_entity.data['hp'])
    # ui.item_sp_bar.setMaximum(last_selected_entity.stats['sp'])
    # ui.item_sp_bar.setValue(last_selected_entity.data['sp'])
    # ui.item_food_bar.setValue(last_selected_entity.data['food'])
    # ui.item_attack_box.setValue(last_selected_entity.stats['atk'])
    # ui.item_defense_box.setValue(last_selected_entity.stats['dfn'])
    # ui.item_special_attack_box.setValue(last_selected_entity.stats['spatk'])
    # ui.item_special_defense_box.setValue(last_selected_entity.stats['spdfn'])
    # ui.item_accuracy_box.setValue(last_selected_entity.stats['acc'])
    # ui.item_evasion_box.setValue(last_selected_entity.stats['eva'])
    # ui.item_critical_box.setValue(last_selected_entity.stats['crit'])
    # ui.item_blessing_box.setValue(last_selected_entity.stats['bless'])
    # ui.item_strength_box.setValue(last_selected_entity.big_stats['strength'])
    # ui.item_dexterity_box.setValue(last_selected_entity.big_stats['dexterity'])
    # ui.item_constitution_box.setValue(last_selected_entity.big_stats['constitution'])
    # ui.item_intelligence_box.setValue(last_selected_entity.big_stats['intelligence'])
    # ui.item_integrity_box.setValue(last_selected_entity.big_stats['integrity'])

def SortItemList(object):
    print(5)

def ChangeItemName(object):
    global last_selected_item
    if not last_selected_item:
        return None
    last_selected_item.name = object
    # ui.item_name_box.setText(last_selected_item.name)
    if ui.item_list.currentItem():
        ui.item_list.currentItem().setText(last_selected_item.name)

def ChangeItemLevel(object):
    global last_selected_item
    if not last_selected_item:
        return None
    last_selected_item.requirements['lvl'][0] = int(object)
    if last_selected_item.requirements['lvl'][0] > last_selected_item.requirements['lvl'][1]%1000:
        last_selected_item.requirements['lvl'][1] = int(object)

def ChangeItemMaxLevel(object):
    global last_selected_item
    if not last_selected_item:
        return None
    last_selected_item.requirements['lvl'][1] = int(object)
    if last_selected_item.requirements['lvl'][1] < last_selected_item.requirements['lvl'][0]:
        last_selected_item.requirements['lvl'][0] = int(object)

def AddItemToList(itm):
    global last_selected_item
    if isinstance(itm,item.Item):
        last_selected_item = itm
        new_list_item = QtWidgets.QListWidgetItem()
        new_list_item.setData(DATACHANNEL,itm)
        new_list_item.setText(itm.name)
        new_list_item.setTextAlignment(4)
        ui.item_list.clearSelection()
        ui.item_list.clearFocus()
        ui.item_list.addItem(new_list_item)
        ui.item_list.setCurrentItem(new_list_item)
        UpdateItemGui(new_list_item)

def MakeItem():
    new_item = item.Item()
    OutputPrint("Created new item")
    AddItemToList(new_item)

def CopyItem():
    new_item = None
    new_item = ui.item_list.currentItem()
    if new_item:
        new_item = copy.deepcopy(new_item.data(DATACHANNEL))
        item.items[item.GetNewId()] = new_item
        OutputPrint("Copied " + new_item.name + " to item list")
    else:
        return None
    AddItemToList(new_item)

def ToggleItemDeleteMode():
    global delete_item_confirmation
    if delete_item_confirmation:
        ui.item_add_button.setText("Add")
        ui.item_copy_button.setText("Copy")
        ui.item_delete_button.setText("Delete")
    else:
        ui.item_add_button.setText("Yes")
        ui.item_copy_button.setText("No")
        ui.item_delete_button.setText("Del?")
    delete_item_confirmation = not delete_item_confirmation

def DeleteItem():
    # Update gui buttons
    ToggleItemDeleteMode()

    # Retireve the item in the list
    old_item = ui.item_list.currentItem()
    if old_item:
        # Get the item data that is being pointed to
        old_item = old_item.data(DATACHANNEL)
        OutputPrint("Deleting " + old_item.name + " from memory")
        # Find the id of the item
        item_id = None
        for key, value in item.items.iteritems():
            if value is old_item:
                item_id = key
                break
        # if we can delete the item then do so
        if item_id in item.items.keys():
            del item.items[item_id]
            OutputPrint("Deleted " + old_item.name + " from memory")
        else:
            OutputPrint("Can't delete " + old_item.name + " from memory")
    else:
        return None

    # Now we need to destroy the item from the GUI
    row = ui.item_list.currentRow()
    if row is None:
        OutputPrint("Can't delete " + old_item.name + " from item list")
        return None
    destroyed_item = ui.item_list.takeItem(row)
    del destroyed_item

    if row > 0:
        # Put the focus on the previous item
        ui.item_list.setCurrentRow(row-1)

        # Update the last selected item and the stats GUI
        old_item = ui.item_list.item(ui.item_list.currentRow())
        global last_selected_item
        if old_item:
            last_selected_item = old_item.data(DATACHANNEL)
        else:
            last_selected_item = None
        UpdateItemGui()

def ItemAddButtonPressed():
    global delete_item_confirmation
    if delete_item_confirmation:
        DeleteItem()
    else:
        MakeItem()

def ItemCopyButtonPressed():
    global delete_item_confirmation
    if delete_item_confirmation:
        ToggleItemDeleteMode()
    else:
        CopyItem()

def LoadFile(fn):
    MainWindow.hide()
    global save_file
    save_file = './saves/file'+str(fn)
    ui.file_select_page.hide()
    ui.active_file_page.show()
    manage.Load(save_file)
    manage.UpdateData()
    OutputPrint("Loaded file at " + save_file)
    for id, entity in manage.data['entities'].iteritems():
        AddEntityToList(entity)
    for id, item in manage.data['items'].iteritems():
        AddItemToList(item)
    MainWindow.show()
    # UpdatePlayerGui(ui.player_list.currentItem())
def Shutdown():
    global save_file
    if save_file:
        print ("Thanks for playing! Saving to " + str(save_file))
        manage.Close(save_file)

# mixer.music.play()
''' File Select Buttons '''
ui.file_select_button1.clicked.connect(lambda: LoadFile(1))
ui.file_select_button2.clicked.connect(lambda: LoadFile(2))
ui.file_select_button3.clicked.connect(lambda: LoadFile(3))

'''
    ENTITY TAB
'''

''' Player List Buttons '''
ui.player_add_button.clicked.connect(lambda: EntityAddButtonPressed(PLAYER))
ui.player_copy_button.clicked.connect(lambda: EntityCopyButtonPressed(PLAYER))
ui.player_delete_button.clicked.connect(lambda: ToggleEntityDeleteMode(PLAYER))
ui.player_list.itemPressed.connect(UpdateEntityGui)
ui.player_list.selectionModel().currentChanged.connect(UpdateEntityGui)

''' Enemy List Buttons '''
ui.enemy_add_button.clicked.connect(lambda: EntityAddButtonPressed(ENEMY))
ui.enemy_copy_button.clicked.connect(lambda: EntityCopyButtonPressed(ENEMY))
ui.enemy_delete_button.clicked.connect(lambda: ToggleEntityDeleteMode(ENEMY))
ui.enemy_list.itemPressed.connect(UpdateEntityGui)
ui.enemy_list.selectionModel().currentChanged.connect(UpdateEntityGui)

''' Entity Box Value Change Events '''
ui.entity_level_box.valueChanged.connect(ChangeEntityLevel)
ui.entity_name_box.textChanged.connect(ChangeEntityName)
ui.entity_gold_box.valueChanged.connect(ChangeEntityGold)
ui.entity_jewels_box.valueChanged.connect(ChangeEntityJewels)

''' Entity Stats Buttons '''
ui.entity_stats_change_add_button.clicked.connect(lambda: EntityChangeStats("Add"))
ui.entity_stats_change_set_button.clicked.connect(lambda: EntityChangeStats("Set"))

''' Entity Stats Change Type '''
ui.entity_stats_change_type_box.currentIndexChanged.connect(UpdateEntityChangeStatsBox)

'''
    ITEM TAB
'''

''' Item List Buttons '''
ui.item_add_button.clicked.connect(ItemAddButtonPressed)
ui.item_copy_button.clicked.connect(ItemCopyButtonPressed)
ui.item_delete_button.clicked.connect(ToggleItemDeleteMode)
ui.item_list.itemPressed.connect(UpdateItemGui)
ui.item_list.selectionModel().currentChanged.connect(UpdateItemGui)

''' Item Box Value Change Events '''
ui.item_name_box.textChanged.connect(ChangeItemName)
ui.item_search_box.textChanged.connect(SortItemList)
ui.item_level_box.valueChanged.connect(ChangeItemLevel)
ui.item_max_level_box.valueChanged.connect(ChangeItemMaxLevel)

def PlaySelectSound():
    SELECT_SOUND.play()
ui.qc_tabs.tabBarClicked.connect(PlaySelectSound)

MainWindow.showFullScreen()

app.aboutToQuit.connect(Shutdown)

sys.exit(app.exec_())
