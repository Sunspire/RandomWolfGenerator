import random
import smtplib


participants = [
                ['name1','email1@somedomain.com'], 
                ['name2','email2@somedomain.com'], 
                ['name3','email3@somedomain.com'], 
                ['name4','email4@somedomain.com']]
wolves = []
witches = []
number_of_wolves = 2
number_of_witches = 2

SMTP_SERVER = 'localhost'
SMTP_PORT = 25
SMTP_LOGIN = 'login'
SMTP_PASSWORD = 'password'
EMAIL_FROM = 'sender@somedomain.com'


def assign_wolves():
    i = 1
    while i <= number_of_wolves:
        index = random.randrange(0, len(participants))
        wolves.append(participants[index])
        participants.pop(index)
        i += 1


def assign_witches():
    i = 1
    while i <= number_of_witches:
        index = random.randrange(0, len(participants))
        witches.append(participants[index])
        participants.pop(index)
        i += 1


def send_email_to_wolves(recipients):
    the_recipients = []

    for i, recipient in enumerate(recipients):
        the_recipients.append(recipient[1])

    message = f'''\
        Subject: Wolves - HangarWW Werewolf Game

        You are wolves. Communicate with each other privately in MSTeams.
        {recipients}
    '''

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, the_recipients, message)


def send_email_to_others(recipients, subject):
    the_recipients = []

    for i, recipient in enumerate(recipients):
        the_recipients.append(recipient[1])
    
    message = f'''\
        Subject: {subject} - HangarWW Werewolf Game

        You are a {subject}.
    '''
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)

        for recipient in the_recipients:
            server.sendmail(EMAIL_FROM, recipient, message)


if __name__ == "__main__":
    assign_wolves()
    assign_witches()

    print()
    print(f'Villagers: {participants}' )
    print(f'Wolves: {wolves}')
    print(f'Witches: {witches}')
    print()
    
    #send_email_to_wolves(wolves)
    #send_email_to_others(witches, 'Witch')
    #send_email_to_others(participants, 'Villager')