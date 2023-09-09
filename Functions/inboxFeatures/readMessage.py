from Functions.colours import Colours
from time import sleep as wait
import json
import sys
import os


def readMessage(info, index):
    message = info['read'][index]
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
    if message_input.lower() == 'delete':
        info['read'].pop(index)
        json_file = open('People/' + info['username'] + '.json', 'w')
        json.dump(info, json_file)
        json_file.close()
        print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Message deleted' + Colours.ResetAll)
        wait(.1)
        return info
    elif message_input.lower() == 'menu':
        return 'menu'
    elif message_input.lower() == 'exit':
        return False
    elif message_input.lower() == "log out":
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
        wait(1)
        os.execv(sys.executable, ['python'] + sys.argv)
    elif message_input.lower() == 'unread':
        info['read'].pop(index)
        info['unread'].insert(0, message)
        json_file = open('People/' + info['username'] + '.json', 'w')
        json.dump(info, json_file)
        json_file.close()
    else:
        return info
