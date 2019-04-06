import item as it
import entity as en
import battle as ba
import effect as ef
import skill as sk
import os.path as op
import pickle
import os

data = {
    'entities': {},
    'items': {},
    'skills': {},
    'effects': {},
}
def Load(name = './saves/file1'):
    global data
    if op.isdir(name):
        # Load packs
        for key, list in data.iteritems():
            if op.isdir(name+'/'+key):
                for filename in os.listdir(name+'/'+key):
                    if filename.endswith(".pickle"):
                        file = open(name+'/'+key+'/'+filename,'rb')
                        new_data = pickle.load(file)
                        for obj in new_data:
                            obj.import_file = filename[:-7]
                            new_obj = AdaptNewObject(obj)
                            list[GetNewId(list.keys())] = new_obj
                        # list+=new_data
                        file.close()
            else:
                os.mkdir(name+'/'+key)
            if key == 'entities':
                en.entities = list
            elif key == 'items':
                it.items = list
            elif key == 'skills':
                sk.skills = list
            elif key == 'effects':
                ef.effects = list


        # Load music
    en.entities = data['entities']
    it.items = data['items']
    ef.effects = data['effects']
    sk.skills = data['skills']

def UpdateData():
    global data
    data = {
        'entities': en.entities,
        'items': it.items,
        'skills': sk.skills,
        'effects': ef.effects,
    }

def Close(name = './saves/file1'):
    global data
    UpdateData()

    # If there is no profile directory 'name', then make one
    if not op.isdir(name):
        os.mkdir(name)

    if op.isdir(name):
        # Save packs
        for key, list in data.iteritems():
            # If no directory exists for our save, then make one
            if not op.isdir(name+'/'+key):
                os.mkdir(name+'/'+key)
            # If we have successfully made a directory for our data, then save it
            if op.isdir(name+'/'+key):
                # Get all the files (packs) and assign objects to their packs
                files = {filename: [open(name+'/'+key+'/'+filename,'wb'),[]] for filename in os.listdir(name+'/'+key) if filename.endswith(".pickle")}
                for id, obj in list.iteritems():
                    if not obj.import_file:
                        obj.import_file = name+'/'+key+'/standard'
                    if (obj.import_file+'.pickle') in files.keys():
                        files[(obj.import_file+'.pickle')][1].append(obj)
                    else:
                        files[obj.import_file+'.pickle'] = [open(name+'/'+key+'/'+obj.import_file+'.pickle','wb'),[obj]]
                for filename, data in files.iteritems():
                    pickle.dump(data[1],data[0])
                    data[0].close()

                # for filename in os.listdir(name+'/'+key):
                #     if filename.endswith(".pickle"):
                #         # Open file
                #         file = open(name+'/'+key+'/'+filename,'wb')
                #         save_data = []
                #         # From our objects, we save them to the correct file
                #         for obj in list:
                #             if (filename == obj.import_file) or (filename == 'standard.pickle' and not obj.import_file):
                #                 save_data.append(obj)
                #         pickle.dump(save_data,file)
                #         file.close()
                # # If we have no standard file yet, make one
                # if not op.isfile(name+'/'+key+'/standard.pickle'):
                #     file = open(name+'/'+key+'/standard.pickle','wb')
                #     save_data = []
                #     # From our objects, we save them to the correct file
                #     for obj in list:
                #         if obj.import_file == 'standard.pickle' or not obj.import_file:
                #             save_data.append(obj)
                #     pickle.dump(save_data,file)
                #     file.close()


def CopyItemToEntity(item = None, entity = None):
    if isinstance(entity, en.Entity):
        entity = en.GetId(entity)
    if isinstance(item, str):
        item = it.GetId(item)
    if item and entity: # We check and send a copy over
        en.entities[entity]['items'].append(it[item].copy())

def GetNewId(ks):
    ids = ks
    if ids == []:
        return '0'
    else:
        ids = [str(a) for a in range(len(ids)+1) if str(a) not in ids]
        return ids[0]

def AdaptNewObject(obj):
    if isinstance(obj,en.Entity):
        new_obj = en.Entity()
    elif isinstance(obj,it.Item):
        new_obj = it.Item()
    elif isinstance(obj,sk.Skill):
        new_obj = sk.Skill()
    elif isinstance(obj,ef.Effect):
        new_obj = ef.Effect()
    for attribute in vars(new_obj).keys():
        if hasattr(obj,attribute):
            if not isinstance(getattr(obj,attribute),dict):
                setattr(new_obj,attribute,getattr(obj,attribute))
            else:
                for sub_attribute, value in getattr(obj,attribute).iteritems():
                    getattr(new_obj,attribute)[sub_attribute] = value
    return new_obj
