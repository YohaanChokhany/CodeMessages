from Functions.colours import Colours
from time import sleep as wait
from Functions.inboxFeatures.readMessage import readMessage
import json
import os
import sys


def read(info):
    choosing_message = True
    while choosing_message:
        json_file = open('People/' + info['username'] + '.json', 'r')
        info = json.load(json_file)
        json_file.close()
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.underline + 'READ' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        i = 0
        if len(info['read']) > 0:
            for message in info['read']:
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
                if message_choice <= len(info['read']):
                    read_message_info = readMessage(info, message_choice - 1)
                    if read_message_info:
                        if read_message_info == 'menu':
                            return 'menu'
                        else:
                            info = read_message_info
                    else:
                        choosing_message = True
                        continue
                else:
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'INVALID' + Colours.ResetAll)
                    wait(.1)
            except:
                if message_choice == 'menu':
                    return 'menu'
                elif message_choice == 'exit' or message_choice == '':
                    return False
                elif message_choice.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                elif message_choice.lower() == 'delete' or message_choice.lower() == 'delete all':
                    info['read'] = []
                    json_file = open('People/' + info['username'] + '.json', 'w')
                    json.dump(info, json_file)
                    json_file.close()
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'All messages deleted!'
                          + Colours.ResetAll)
                    wait(.1)
                else:
                    choosing_message = True
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Please enter only integer values'
                          + Colours.ResetAll)
                    wait(.1)
                    continue
        else:
            print(Colours.ResetAll + 'You have no messages!')
            wait(.1)
            print('')
            wait(.1)
            print(Colours.ResetAll + "Press 'ENTER' to continue")
            wait(.1)
            allRead = input(Colours.darkGray + '')
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
