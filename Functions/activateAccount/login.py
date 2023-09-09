from Functions.colours import Colours
import json
import os
from time import sleep as wait
import bcrypt
import getpass
import sys


def login():
    typing_username = True
    while typing_username:
        print(Colours.ResetAll + Colours.underline + "LOGIN TO EXISTING ACCOUNT" + Colours.ResetAll)
        wait(.1)
        username = input(Colours.ResetAll + 'Username: ' + Colours.darkGray)
        wait(.1)
        file_name = 'People/' + username.lower() + '.json'
        if os.path.isfile(file_name):
            json_file = open(file_name, 'r')
            info = json.load(json_file)
            typing_username = False
            typing_password = True
            while typing_password:
                password = getpass.getpass(prompt=Colours.ResetAll + "Password: " + Colours.darkGray)
                wait(.1)
                if bcrypt.checkpw(password.encode(), info['password'].encode()):
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Login Successful!!'
                          + Colours.ResetAll)
                    wait(.1)
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + 'Username:', info['username'])
                    wait(.1)
                    print(Colours.ResetAll + 'Name:', info['name'])
                    wait(.1)
                    print(Colours.ResetAll + 'Unread Messages:', str(len(info['unread'])))
                    wait(.1)
                    print(Colours.ResetAll + 'Read Messages:', str(len(info['read'])))
                    wait(.1)
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + "Press 'ENTER' to continue" + Colours.darkGray)
                    wait(.1)
                    foot = input("")
                    wait(.1)
                    if foot.lower() == "log out":
                        print(Colours.ResetAll + '')
                        wait(.1)
                        print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                        wait(1)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    return info
                elif password.lower() == 'exit':
                    typing_password = False
                    typing_username = True
                    continue
                else:
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Wrong Password' + Colours.ResetAll)
                    wait(.1)
        elif username.lower() == 'exit':
            print(Colours.ResetAll + '')
            wait(.1)
            return False
        else:
            print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Invalid Username' + Colours.ResetAll)
            wait(.1)
            print(Colours.ResetAll + '')
            wait(.1)