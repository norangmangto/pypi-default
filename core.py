import copy

def default(new, base):
    base = copy.deepcopy(base)
    new = copy.deepcopy(new)
    for key in new.keys():
        base[key] = new[key]

    return base
