def Disadvantages(element = None):
    if not element:
        return None
    w = []
    for key, value in element_matrix[element].items():
        if value == -1:
            w.append(key)
    return w
def Advantages(element =  None):
    if not element:
        return None
    s = []
    for key, value in element_matrix[element].items():
        if value == 1:
            s.append(key)
    return s

element_matrix = {
    'fire': {
        'fire': 0,
        'water': -1,
        'grass': 1,
        'electric': 0,
        'rock': -1,
        'air': 0,
        'ice': 1,
        'machine': 1,
        'light': -1,
        'dark': 0
    },
    'water': {
        'fire': 1,
        'water': 0,
        'grass': -1,
        'electric': -1,
        'rock': 1,
        'air': 0,
        'ice': 0,
        'machine': 1,
        'light': -1,
        'dark': 0
    },
    'grass': {
        'fire': -1,
        'water': 1,
        'grass': 0,
        'electric': 0,
        'rock': 1,
        'air': 0,
        'ice': 0,
        'machine': 0,
        'light': -1,
        'dark': 0
    },
    'electric': {
        'fire': 0,
        'water': 1,
        'grass': 0,
        'electric': -1,
        'rock': -1,
        'air': 1,
        'ice': 0,
        'machine': 1,
        'light': -1,
        'dark': 0
    },
    'rock': {
        'fire': 1,
        'water': -1,
        'grass': -1,
        'electric': 1,
        'rock': 0,
        'air': 1,
        'ice': 1,
        'machine': 0,
        'light': -1,
        'dark': 0
    },
    'air': {
        'fire': 1,
        'water': 0,
        'grass': 1,
        'electric': 0,
        'rock': 0,
        'air': -1,
        'ice': 0,
        'machine': -1,
        'light': -1,
        'dark': 0
    },
    'ice': {
        'fire': -1,
        'water': 1,
        'grass': 1,
        'electric': 0,
        'rock': 0,
        'air': 0,
        'ice': -1,
        'machine': 0,
        'light': -1,
        'dark': 0
    },
    'machine': {
        'fire': -1,
        'water': -1,
        'grass': -1,
        'electric': 1,
        'rock': 1,
        'air': 1,
        'ice': 1,
        'machine': 1,
        'light': -1,
        'dark': -1
    },
    'light': {
        'fire': 0,
        'water': 0,
        'grass': 0,
        'electric': 0,
        'rock': 0,
        'air': 0,
        'ice': 0,
        'machine': 0,
        'light': 0,
        'dark': 1
    },
    'dark': {
        'fire': 1,
        'water': 1,
        'grass': 1,
        'electric': 1,
        'rock': 1,
        'air': 1,
        'ice': 1,
        'machine': 1,
        'light': -1,
        'dark': 1
    },
}
