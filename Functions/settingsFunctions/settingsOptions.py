from Functions.colours import Colours
from time import sleep as wait
import json
import os
import sys


def settingsOptions():
    print('')
    wait(.1)
    settings_options = ['Change Username', 'Change Name', 'Change Password', 'Clear Messages', 'Delete Account']
    setting = True
    while setting:
        print(Colours.ResetAll + Colours.underline + 'SETTINGS' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        i = 0
        while i < len(settings_options):
            print(Colours.ResetAll + str(i + 1) + '. ' + settings_options[i])
            wait(.1)
            i += 1
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + 'Choose a function')
        wait(.1)
        option = str(input(Colours.darkGray + ''))
        wait(.1)
        option = option.lower()
        if option.lower() == 'change username' or option.lower() == 'username' or option == '1':
            return 'change username'
        elif option.lower() == 'change name' or option.lower() == 'name' or option == '2':
            return 'change name'
        elif option.lower() == 'change password' or option.lower() == 'password' or option == '3':
            return 'change password'
        elif option.lower() == 'clear messages' or option.lower() == 'messages' or option == '4':
            return 'clear messages'
        elif option.lower() == 'delete account' or option.lower() == 'delete' or option == '5':
            rechecking_delete = True
            while rechecking_delete:
                print(Colours.ResetAll + '')
                wait(.1)
                recheck_delete = str(input(Colours.ResetAll + 'Do you want to delete your account? (yes/no) '
                                           + Colours.darkGray))
                wait(.1)
                if recheck_delete.lower() == 'no':
                    print(Colours.ResetAll + '')
                    wait(.1)
                    break
                elif recheck_delete.lower() == 'yes':
                    print(Colours.ResetAll + '')
                    wait(.1)
                    return 'delete account'
                elif recheck_delete.lower() == 'menu':
                    return 'exit'
                elif recheck_delete.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                else:
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.lightRed + "Please answer in 'YES' or 'NO' only"
                          + Colours.ResetAll)
                    wait(.1)
        elif option.lower() == 'exit' or option.lower() == '':
            return 'exit'
        elif option.lower() == 'menu':
            return 'exit'
        elif option.lower() == "log out":
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
