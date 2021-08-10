from functions.general import get_player_config, get_game_config
from functions.roles import assign_role
from functions.local_email import send_email_to_wolves, send_email_to_others


def main():
    villagers = get_player_config()
    game_config = get_game_config()
    number_of_wolves = int(game_config['wolf'])
    number_of_witches = int(game_config['witch'])
    number_of_cupids = int(game_config['cupid'])
    send_email = bool(int(game_config['send_email']))

    wolves = []
    wolves_and_remaining_villagers = assign_role(number_of_wolves, villagers)
    wolves = wolves_and_remaining_villagers[0]
    villagers = wolves_and_remaining_villagers[1]

    witches = []
    witches_and_remaining_villagers = assign_role(number_of_witches, villagers)
    witches = witches_and_remaining_villagers[0]
    villagers = witches_and_remaining_villagers[1]

    cupids = []
    cupids_and_remaining_villagers = assign_role(number_of_cupids, villagers)
    cupids = cupids_and_remaining_villagers[0]
    villagers = cupids_and_remaining_villagers[1]

    all_villagers = villagers + witches + cupids
    print()
    print(f'Villagers: {villagers}' )
    print(f'Wolves: {wolves}')
    print(f'Witches: {witches}')
    print(f'Cupids: {cupids}')
    print()
    
    if send_email:
        send_email_to_wolves(wolves, all_villagers)
        send_email_to_others(witches, 'Witch')
        send_email_to_others(cupids, 'Cupid')
        send_email_to_others(villagers, 'Villager')
    else:
        print('Emails are disabled')

if __name__ == "__main__":
    main()