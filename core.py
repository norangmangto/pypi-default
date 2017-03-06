import copy

def default(new, base):
    new = {} if new is None else new
    base = {} if base is None else copy.deepcopy(base)

    for key in new.keys():
        base[key] = new[key]

    return base
