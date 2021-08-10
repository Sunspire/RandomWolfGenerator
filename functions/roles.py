import random


def assign_role(role_name: str, amount: int, villagers = []):
    wolves = []
    witches = []
    cupids = []

    i = 1
    the_villagers = villagers
    while i <= amount:
        index = random.randrange(0, len(the_villagers))
        if role_name == 'wolf':
            wolves.append(villagers[index])
        elif role_name == 'witch':
            witches.append(the_villagers[index])
        elif role_name == 'cupid':
            cupids.append(the_villagers[index])
        the_villagers.pop(index)
        i += 1

    if role_name == 'wolf':
        return [wolves, the_villagers]
    elif role_name == 'witch':
        return [witches, the_villagers]
    elif role_name == 'cupid':
        return [cupids, the_villagers]

def assign_wolves(number_of_wolves: int, villagers = []):
    i = 1
    wolves = []
    the_villagers = villagers
    while i <= number_of_wolves:
        index = random.randrange(0, len(the_villagers))
        wolves.append(villagers[index])
        the_villagers.pop(index)
        i += 1
    return [wolves, the_villagers]

def assign_witches(number_of_witches: int, villagers = []):
    i = 1
    witches = []
    the_villagers = villagers
    while i <= number_of_witches:
        index = random.randrange(0, len(the_villagers))
        witches.append(the_villagers[index])
        the_villagers.pop(index)
        i += 1
    return [witches, the_villagers]

def assign_cupids(number_of_cupids: int, villagers = []):
    i = 1
    cupids = []
    the_villagers = villagers
    while i <= number_of_cupids:
        index = random.randrange(0, len(the_villagers))
        cupids.append(the_villagers[index])
        the_villagers.pop(index)
        i += 1
    return [cupids, the_villagers]
