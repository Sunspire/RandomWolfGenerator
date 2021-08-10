import random


def assign_role(amount: int, villagers = []):
    assigned_to_the_role = []
    the_villagers = villagers
    i = 1
    
    while i <= amount:
        index = random.randrange(0, len(the_villagers))
        assigned_to_the_role.append(villagers[index])
        the_villagers.pop(index)
        i += 1
    
    return [assigned_to_the_role, the_villagers]