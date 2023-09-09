from Functions.colours import Colours
import json
from time import sleep as wait
import os
import sys


def profile(info):
    print(Colours.ResetAll + '')
    wait(.1)
    print(Colours.ResetAll + Colours.underline + 'PROFILE' + Colours.ResetAll)
    wait(.1)
    file_name = 'People/' + info['username'].lower() + '.json'
    json_file = open(file_name, 'r')
    info = json.load(json_file)
    json_file.close()
    print(Colours.ResetAll + '')
    wait(.1)
    print(Colours.ResetAll + 'Username:', info['username'])
    wait(.1)
    print(Colours.ResetAll + 'Name:', info['name'])
    wait(.1)
    print(Colours.ResetAll + 'Password:', info['password_string'])
    wait(.1)
    print(Colours.ResetAll + 'Unread Messages:', str(len(info['unread'])))
    wait(.1)
    print(Colours.ResetAll + "Read Messages:", str(len(info['read'])))
    wait(.1)
    print(Colours.ResetAll + '')
    wait(.1)
    foot = input(Colours.ResetAll + "Press 'ENTER' to continue" + Colours.darkGray)
    wait(.1)
    if foot.lower() == "log out":
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
        wait(1)
        os.execv(sys.executable, ['python'] + sys.argv)
    return info
