from Functions.colours import Colours
from time import sleep as wait
import json
import os
import sys


def unreadMessage(info, index):
    message = info['unread'][index]
    print(Colours.ResetAll + '')
    wait(.1)
    print(Colours.ResetAll + 'From:   ', message['from'])
    wait(.1)
    print(Colours.ResetAll + 'Subject:', message['subject'])
    wait(.1)
    print(Colours.ResetAll + 'Message:', message['message'])
    wait(.1)
    message_input = input(Colours.darkGray + '')
    wait(.1)
    info['unread'].pop(index)
    if message_input.lower() == 'delete':
        json_file = open('People/' + info['username'] + '.json', 'w')
        json.dump(info, json_file)
        json_file.close()
        print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Message deleted' + Colours.ResetAll)
        wait(.1)
        return info
    else:
        info['read'].insert(0, message)
        json_file = open('People/' + info['username'] + '.json', 'w')
        json.dump(info, json_file)
        json_file.close()
        if message_input.lower() == 'menu':
            return 'menu'
        elif message_input.lower() == 'exit':
            return False
        elif message_input.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            return info
