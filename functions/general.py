def get_player_config():
    players = []
    with open('configuration/player_config.ini', 'r') as f:
        rows = f.readlines()

        for y, cols in enumerate(rows):
            the_player = list(cols.replace('\n','').split(','))
            if the_player[0][0] != '#':
                players.append(the_player)
    
    return players

def get_game_config():
    config = {}
    with open('configuration/game_config.ini', 'r') as f:
        rows = f.readlines()

        for y, cols in enumerate(rows):
            the_list = list(cols.replace('\n','').split(','))
            config[the_list[0]] = the_list[1]

    return config
    
def get_email_config():
    config = {}
    with open('configuration/email_config.ini', 'r') as f:
        rows = f.readlines()

        for y, cols in enumerate(rows):
            the_list = list(cols.replace('\n','').split(','))
            config[the_list[0]] = the_list[1]

    return config