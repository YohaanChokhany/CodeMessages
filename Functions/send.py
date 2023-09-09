from Functions.colours import Colours
import os
from time import sleep as wait
import json
import sys


def send(info):
    print('')
    wait(.1)
    print(Colours.ResetAll + Colours.underline + 'Send Message' + Colours.ResetAll)
    wait(.1)
    print(Colours.ResetAll + '')
    wait(.1)
    typing_recipient = True
    while typing_recipient:
        recipient = str(input(Colours.ResetAll + 'Recipient: ' + Colours.darkGray))
        wait(.1)
        recipient_file_name = 'People/' + recipient.lower() + '.json'
        if os.path.isfile(recipient_file_name):
            typing_recipient = False
            typing_subject = True
            while typing_subject:
                subject = str(input(Colours.ResetAll + 'Subject:   ' + Colours.darkGray))
                wait(.1)
                if subject == '':
                    print(Colours.ResetAll + Colours.lightRed + 'Subject field cannot be empty' + Colours.ResetAll)
                    wait(.1)
                    continue
                elif subject.lower() == 'exit':
                    typing_recipient = True
                    break
                elif subject.lower() == 'menu':
                    return False
                elif subject.lower() == "log out":
                    print(Colours.ResetAll + '')
                    wait(.1)
                    print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                    wait(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                else:
                    typing_subject = False
                    typing_message = True
                    while typing_message:
                        message = str(input(Colours.ResetAll + 'Message:   ' + Colours.darkGray))
                        wait(.1)
                        if message == '':
                            print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Message field cannot be empty' + Colours.ResetAll)
                            wait(.1)
                            continue
                        elif message.lower() == 'exit':
                            typing_subject = True
                            break
                        elif message.lower() == 'menu':
                            return False
                        elif message.lower() == "log out":
                            print(Colours.ResetAll + '')
                            wait(.1)
                            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
                            wait(1)
                            os.execv(sys.executable, ['python'] + sys.argv)
                        else:
                            with open(recipient_file_name) as recipient_json_file:
                                recipient_info = json.load(recipient_json_file)

                            recipient_info['unread'].append({'from': info['username'], 'subject': subject,
                                                             'message': message})
                            with open(recipient_file_name, "w") as recipient_json_file:
                                json.dump(recipient_info, recipient_json_file)
                                recipient_json_file.close()
                                print(Colours.ResetAll + Colours.green + Colours.bold + 'Message sent!' + Colours.ResetAll)
                                return True
        elif recipient.lower() == 'exit' or recipient.lower() == 'menu':
            return False
        elif recipient.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            print(Colours.ResetAll + Colours.lightRed + 'Recipient Not Found!' + Colours.ResetAll)
            wait(.1)
            continue
