from Functions.colours import Colours
from time import sleep as wait
import os
import json
import sys


def changeUsername(info):
    print('')
    wait(.1)
    typing_new_username = True
    while typing_new_username:
        print(Colours.ResetAll + Colours.underline + 'Change Username' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        print('Old Username:', info['username'])
        wait(.1)
        new_username = str(input(Colours.ResetAll + 'Username: ' + Colours.darkGray))
        wait(.1)
        if new_username == info['username']:
            print(Colours.ResetAll + Colours.lightRed + 'You cannot enter the same username')
            continue
        elif new_username.lower() == 'exit':
            return False
        elif new_username.lower() == 'menu':
            return 'menu'
        elif new_username.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            rechecking_username = True
            while rechecking_username:
                recheck_username = str(input(Colours.ResetAll + 'Do you want to change your username to '
                                             + new_username + '? (yes/no) ' + Colours.darkGray))
                wait(.1)
                if recheck_username.lower() == 'no':
                    break
                elif recheck_username.lower() == 'yes':
                    new_file_name = 'People/' + new_username.lower() + '.json'
                    file_name = 'People/' + info['username'].lower() + '.json'
                    info['username'] = new_username
                    with open(file_name, 'w') as json_file_name_change:
                        json.dump(info, json_file_name_change)
                    os.rename(file_name, new_file_name)
                    print(Colours.ResetAll + 'New Username:', info['username'])
                    wait(.1)
                    print(Colours.ResetAll + '')
                    wait(.1)
                    return info
                elif recheck_username.lower() == 'menu':
                    return 'menu'
                elif recheck_username.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                else:
                    print(Colours.ResetAll + Colours.lightRed + "Please answer in 'YES' or 'NO' only"
                          + Colours.ResetAll)
                    wait(.1)
                    print(Colours.ResetAll + '')
                    wait(.1)
