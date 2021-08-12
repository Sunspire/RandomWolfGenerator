from functions.general import get_player_config, get_game_config
from functions.roles import assign_role
from functions.local_email import send_email_to_wolves, send_email_to_others
from termcolor import colored


def main():
    villagers = get_player_config()
    game_config = get_game_config()
    
    wolves_and_remaining_villagers = assign_role(int(game_config['wolf']), villagers)
    wolves = wolves_and_remaining_villagers[0]
    villagers = wolves_and_remaining_villagers[1]

    witches_and_remaining_villagers = assign_role(int(game_config['witch']), villagers)
    witches = witches_and_remaining_villagers[0]
    villagers = witches_and_remaining_villagers[1]

    cupids_and_remaining_villagers = assign_role(int(game_config['cupid']), villagers)
    cupids = cupids_and_remaining_villagers[0]
    villagers = cupids_and_remaining_villagers[1]
    
    seers_and_remaining_villagers = assign_role(int(game_config['seer']), villagers)
    seers = seers_and_remaining_villagers[0]
    villagers = seers_and_remaining_villagers[1]

    all_villagers = villagers + witches + cupids
    all_players = all_villagers + wolves
    
    print()
    print('====================')
    
    list_of_names = []
    for player in all_players:
        list_of_names.append(player[0])
    list_of_names.sort()
    print('Players: ' + ', '.join(list_of_names))
    
    list_of_names = []
    for villager in villagers:
        list_of_names.append(villager[0])
    list_of_names.sort()
    print(colored('Villagers: ', 'cyan') + ', '.join(list_of_names))

    list_of_names = []
    for wolf in wolves:
        list_of_names.append(wolf[0])
    list_of_names.sort()
    print(colored('Wolves: ', 'red') + ', '.join(list_of_names))
    
    list_of_names = []
    for witch in witches:
        list_of_names.append(witch[0])
    list_of_names.sort()
    print(colored('Witches: ', 'yellow') + ', '.join(list_of_names))
    
    list_of_names = []
    for cupid in cupids:
        list_of_names.append(cupid[0])
    list_of_names.sort()
    print(colored('Cupids: ', 'magenta') + ', '.join(list_of_names))
    
    list_of_names = []
    for seer in seers:
        list_of_names.append(seer[0])
    list_of_names.sort()
    print(colored('Seers: ', 'green') + ', '.join(list_of_names))
    
    print('====================')

    send_email_to_wolves(wolves, all_villagers)
    send_email_to_others(witches, 'Witch')
    send_email_to_others(cupids, 'Cupid')
    send_email_to_others(villagers, 'Villager')
    send_email_to_others(seers, 'Seer')
    
    print('====================')
    print()    
if __name__ == "__main__":
    main()