import pickle
file = open('names.txt', 'r')
names = []
with file as f:
    c = f.readlines()
    names = [x.strip() for x in c]

file.close()
file2 = open('names.pickle', 'wb')
pickle.dump(names,file2)
file2.close()
