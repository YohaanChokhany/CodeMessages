from Functions.colours import Colours
from time import sleep as wait
from Functions.inboxFeatures.unreadMessage import unreadMessage
import json
import os
import sys


def unread(info):
    choosing_message = True
    while choosing_message:
        json_file = open('People/' + info['username'] + '.json', 'r')
        info = json.load(json_file)
        json_file.close()
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.underline + 'UNREAD' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        if len(info['unread']) > 0:
            i = 0
            for message in info['unread']:
                from_text = message['from']
                while len(from_text) < 20:
                    from_text += ' '
                print(str(i + 1) + '. From:', from_text, 'Subject:', message['subject'])
                wait(.1)
                i += 1
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + 'Choose Message' + Colours.darkGray)
            wait(.1)
            message_choice = input('')
            wait(.1)
            try:
                message_choice = int(message_choice)
                if message_choice <= len(info['unread']):
                    unread_message_info = unreadMessage(info, message_choice - 1)
                    if unread_message_info:
                        if unread_message_info == 'menu':
                            return 'menu'
                        else:
                            info = unread_message_info
                    else:
                        choosing_message = True
                        continue
                else:
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'INVALID' + Colours.ResetAll)
                    wait(.1)
            except:
                if message_choice.lower() == 'menu':
                    return 'menu'
                elif message_choice.lower() == 'exit' or message_choice.lower() == '':
                    return False
                elif message_choice.lower() == 'delete' or message_choice.lower() == 'delete all':
                    info['unread'] = []
                    json_file = open('People/' + info['username'] + '.json', 'w')
                    json.dump(info, json_file)
                    json_file.close()
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'All messages deleted!'
                          + Colours.ResetAll)
                    wait(.1)
                else:
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Please enter only integer values'
                          + Colours.ResetAll)
                    wait(.1)
                return info
        else:
            print(Colours.ResetAll + 'You have read all messages!')
            wait(.1)
            print('')
            wait(.1)
            print(Colours.ResetAll + "Press 'ENTER' to continue" + Colours.darkGray)
            wait(.1)
            allRead = input('')
            wait(.1)
            if allRead == 'menu':
                return 'menu'
            elif allRead == 'exit':
                return False
            elif allRead.lower() == "log out":
                print(Colours.ResetAll + '')
                wait(.1)
                print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                wait(1)
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                return False
