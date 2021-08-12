import smtplib
from functions.general import get_email_config


def send_email_to_wolves(wolves = [], villagers = []):
    config = get_email_config()
    if int(config['send_email']) == 0:
        print('emails are disabled')
        return

    SMTP_SERVER = config['smtp_server']
    SMTP_PORT = int(config['smtp_port'])
    SMTP_LOGIN = config['smtp_login']
    SMTP_PASSWORD = config['smtp_password']
    EMAIL_FROM = config['email_from']

    the_recipients = []
    the_wolves = []
    for wolf in wolves:
        the_recipients.append(wolf[1])
        the_wolves.append(wolf[0])

    the_wolves.sort()
    the_wolves_to_string = ', '.join(the_wolves)
    
    the_villagers = []
    for villager in villagers:
        the_villagers.append(villager[0])
        
    the_villagers.sort()
    the_villagers_to_string = ', '.join(the_villagers)
    
    message = f'''Subject: Werewolf Game

        You are wolves. Communicate with each other privately in MSTeams.
        Wolves: 
        {the_wolves_to_string}

        These are the villagers that you can kill: 
        {the_villagers_to_string}
    '''
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, the_recipients, message)
        print('Wolf email sent')


def send_email_to_others(recipients = [], subject: str = ''):
    config = get_email_config()    
    if int(config['send_email']) == 0:
        print('emails are disabled')
        return
    
    if len(recipients) == 0:
        return
    
    SMTP_SERVER = config['smtp_server']
    SMTP_PORT = int(config['smtp_port'])
    SMTP_LOGIN = config['smtp_login']
    SMTP_PASSWORD = config['smtp_password']
    EMAIL_FROM = config['email_from']

    the_recipients = []

    for recipient in recipients:
        the_recipients.append(recipient[1])
    
    message = f'''Subject: Werewolf Game

        You are a {subject}.
    '''
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, the_recipients, message)

        print(f'email for {subject} sent')
        #for recipient in the_recipients:
        #    server.sendmail(EMAIL_FROM, recipient, message)
        #    print(f'email for {subject} sent to {recipient}')
