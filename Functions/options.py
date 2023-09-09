from time import sleep as wait
from Functions.colours import Colours
import os
import sys


def options(info):
    print(Colours.ResetAll + '')
    wait(.1)
    printing = True
    while printing:
        print(Colours.ResetAll + Colours.underline + 'MAIN MENU' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        i = 0
        inbox = 'Inbox (' + str(len(info['unread'])) + ')'
        print_options = ['Profile', 'Settings', 'Send', inbox, 'Help', 'Log Out']
        while i < len(print_options):
            print(Colours.ResetAll + str(i + 1) + '. ' + print_options[i])
            i += 1
            wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + 'Choose a function')
        wait(.1)
        option = str(input(Colours.darkGray + ''))
        wait(.1)
        option = option.lower()
        if option == 'profile' or option == '1':
            return 'profile'
        elif option == 'settings' or option == '2':
            return 'settings'
        elif option == 'send' or option == '3':
            return 'send'
        elif option == 'inbox' or option == '4':
            return 'inbox'
        elif option == 'help' or option == '5':
            return 'help'
        elif option == 'log out' or option == 'exit' or option == '6':
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print(Colours.ResetAll + Colours.lightRed + 'Please Enter a Valid Function' + Colours.ResetAll)
            wait(.1)
            print(Colours.ResetAll + '')
            wait(.1)
