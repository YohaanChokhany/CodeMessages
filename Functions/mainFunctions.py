import os
import json
from Functions.sign_in import checkSigninMode
from Functions.options import options
from Functions.activateAccount.login import login
from Functions.activateAccount.sign_up import signup
from Functions.profile import profile
from Functions.help import help
from Functions.send import send
from Functions.settings import settings
from Functions.inbox import inbox


def main():
    if not os.path.isdir('People'):
        os.makedirs('People')

    info = None
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')

    running = True
    while running:
        if not info:
            mode = checkSigninMode()

            if mode == 'login':
                info = login()
                if not info:
                    continue
            elif mode == 'signup':
                info = signup()
                if not info:
                    continue

        json_file = open('People/' + info['username'] + '.json', 'r')
        info = json.load(json_file)
        json_file.close()

        option = options(info)
        if option == 'profile':
            info = profile(info)
        elif option == 'help':
            help()
        elif option == 'send':
            sent = send(info)
            if not sent:
                continue
        elif option == 'settings':
            settings_info = settings(info)
            if settings_info:
                if type(settings_info) is str:
                    info = None
                else:
                    info = settings_info
        elif option == 'inbox':
            inbox_info = inbox(info['username'])
            if inbox_info:
                info = inbox_info
