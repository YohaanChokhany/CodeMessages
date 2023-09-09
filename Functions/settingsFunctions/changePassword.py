from Functions.colours import Colours
import getpass
from time import sleep as wait
import bcrypt
import json
import os
import sys


def changePassword(info):
    checking_password = True
    print('')
    wait(.1)
    while checking_password:
        check_password = getpass.getpass(prompt=Colours.ResetAll + 'Type Your Password: ')
        if bcrypt.checkpw(check_password.encode(), info['password'].encode()):
            print('')
            wait(.1)
            checking_password = False
            typing_new_password = True
            while typing_new_password:
                print(Colours.ResetAll + Colours.underline + 'Change Password' + Colours.ResetAll)
                wait(.1)
                print(Colours.ResetAll + 'Old Password:', info['password_string'])
                wait(.1)
                new_password = getpass.getpass(prompt=Colours.ResetAll + 'Password: ' + Colours.darkGray)
                wait(.1)
                if new_password.lower() == 'exit':
                    return False
                elif new_password.lower() == 'menu':
                    return 'menu'
                elif new_password.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                elif bcrypt.checkpw(new_password.encode(), info['password'].encode()):
                    print(Colours.ResetAll + Colours.lightRed + 'You cannot enter the same password' + Colours.ResetAll)
                    wait(.1)
                    print('')
                    wait(.1)
                    continue
                confirm_new_password = getpass.getpass(prompt=Colours.ResetAll + 'Confirm Password: '
                                                              + Colours.darkGray)
                wait(.1)
                if confirm_new_password.lower() == 'exit':
                    print('')
                    wait(.1)
                    continue
                elif confirm_new_password.lower() == 'menu':
                    return 'menu'
                elif confirm_new_password.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                elif confirm_new_password == new_password:
                    hashed_password = bcrypt.hashpw(confirm_new_password.encode(), bcrypt.gensalt()).decode()
                    info['password'] = hashed_password
                    i = 0
                    password_string = ''
                    while i < len(confirm_new_password):
                        password_string += '*'
                        i += 1
                    info['password_string'] = password_string
                    json_file = open('People/' + info['username'].lower() + '.json', 'w')
                    json.dump(info, json_file)
                    json_file.close()
                    print(Colours.ResetAll + 'New Password:', info['password_string'])
                    wait(.1)
                    print('')
                    wait(.1)
                    return info
                else:
                    print(Colours.ResetAll + Colours.lightRed + 'Passwords do not match' + Colours.ResetAll)
        elif check_password.lower() == 'exit':
            return False
        elif check_password.lower() == 'menu':
            return 'menu'
        elif check_password.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print(Colours.ResetAll + Colours.lightRed + 'Wrong Password' + Colours.ResetAll)
            wait(.1)
            print('')
            wait(.1)
