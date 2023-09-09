from Functions.colours import Colours
from time import sleep as wait
from Functions.inboxFeatures.unread import unread
from Functions.inboxFeatures.read import read
import json
import os
import sys


def inbox(username):
    choosing = True
    while choosing:
        json_file = open('People/' + username + '.json', 'r')
        info = json.load(json_file)
        json_file.close()
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.underline + 'INBOX' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + '1. Unread -', str(len(info['unread'])))
        wait(.1)
        print(Colours.ResetAll + '2. Read -', str(len(info['read'])))
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + "Choose 'READ' or 'UNREAD'")
        wait(.1)
        choose = str(input(Colours.darkGray + ''))
        wait(.1)
        if choose.lower() == 'unread' or choose == '1':
            unread_info = unread(info)
            if unread_info:
                if unread_info == 'menu':
                    return False
                else:
                    info = unread_info
            else:
                choosing = True
                continue
        elif choose.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        elif choose.lower() == "delete" or choose.lower() == "delete all":
            totalMessages = len(info['read']) + len(info['unread'])
            if totalMessages > 0:
                info['unread'] = []
                info['read'] = []
                json_file_delete = open("People/" + info['username'] + '.json', 'w')
                json.dump(info, json_file_delete)
                json_file_delete.close()
                print('')
                wait(.1)
                print(Colours.ResetAll + Colours.lightRed + str(totalMessages), 'messages have been deleted' + Colours.ResetAll)
                wait(.1)
            else:
                print(Colours.ResetAll + '')
                wait(.1)
                print(Colours.ResetAll + Colours.lightRed + 'Error! You have no messages')
                wait(.1)
        elif choose.lower() == 'read' or choose == '2':
            read_info = read(info)
            if read_info:
                if read_info == 'menu':
                    return False
                else:
                    info = read_info
            else:
                choosing = True
                continue
        elif choose.lower() == 'exit' or choose.lower() == 'menu' or choose.lower() == '':
            return False
        else:
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.lightRed + Colours.bold + "Please enter 'READ' or 'UNREAD' only"
                  + Colours.ResetAll)
            wait(.1)
