import smtplib
from functions.general import get_email_config


def send_email_to_wolves(wolves = [], villagers = []):
    config = get_email_config()

    SMTP_SERVER = config['smtp_server']
    SMTP_PORT = int(config['smtp_port'])
    SMTP_LOGIN = config['smtp_login']
    SMTP_PASSWORD = config['smtp_password']
    EMAIL_FROM = config['email_from']

    the_recipients = []

    for i, recipient in enumerate(wolves):
        the_recipients.append(recipient[1])

    message = f'''\
        Subject: Werewolf Game

        You are wolves. Communicate with each other privately in MSTeams.
        Wolves: 
        {wolves}

        These are the villagers that you can kill: 
        {villagers}
    '''
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, the_recipients, message)
        print('Wolf email sent')


def send_email_to_others(recipients = [], subject: str = ''):
    if len(recipients) == 0:
        return
        
    config = get_email_config()

    SMTP_SERVER = config['smtp_server']
    SMTP_PORT = int(config['smtp_port'])
    SMTP_LOGIN = config['smtp_login']
    SMTP_PASSWORD = config['smtp_password']
    EMAIL_FROM = config['email_from']

    the_recipients = []

    for i, recipient in enumerate(recipients):
        the_recipients.append(recipient[1])
    
    message = f'''\
        Subject: Werewolf Game

        You are a {subject}.
    '''
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, the_recipients, message)

        print(f'email for {subject} sent')
        #for recipient in the_recipients:
        #    server.sendmail(EMAIL_FROM, recipient, message)
        #    print(f'email for {subject} sent to {recipient}')
