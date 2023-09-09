from Functions.colours import Colours
from time import sleep as wait
import json
import sys
import os


def changeName(info):
    typing_new_name = True
    print('')
    wait(.1)
    while typing_new_name:
        print(Colours.ResetAll + Colours.underline + 'Change Name' + Colours.ResetAll)
        wait(.1)
        print(Colours.ResetAll + '')
        wait(.1)
        print('Old Name:', info['name'])
        wait(.1)
        new_name = str(input(Colours.ResetAll + 'Name: ' + Colours.darkGray))
        wait(.1)
        character_present = False
        i = 0
        for character in new_name:
            if not character.isalpha() and character != ' ':
                character_present = True
                break
        if new_name == "":
            print('')
            wait(.1)
            print(Colours.lightRed + "This field cannot be left empty" + Colours.ResetAll)
            wait(.1)
            print("")
            wait(.1)
            continue
        if character_present:
            print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Please enter letters only'
                  + Colours.ResetAll)
            wait(.1)
            print(Colours.ResetAll + '')
            wait(.1)
            continue
        if new_name.lower() == info['name'].lower():
            print('')
            wait(.1)
            print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'You cannot enter the same name')
            wait(.1)
            continue
        elif new_name.lower() == 'exit':
            return False
        elif new_name.lower() == 'menu':
            return 'menu'
        elif new_name.lower() == "log out":
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.green + Colours.bold + 'Logged out successfully' + Colours.ResetAll)
            wait(1)
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            rechecking_name = True
            while rechecking_name:
                recheck_name = str(input(Colours.ResetAll + 'Do you want to change your name to '
                                         + new_name + '? (yes/no) ' + Colours.darkGray))
                wait(.1)
                if recheck_name.lower() == 'no':
                    break
                elif recheck_name.lower() == 'yes':
                    file_name = 'People/' + info['username'].lower() + '.json'
                    info['name'] = new_name
                    with open(file_name, 'w') as json_file_name_change:
                        json.dump(info, json_file_name_change)
                    print(Colours.ResetAll + 'New Name:', info['name'])
                    wait(.1)
                    return info
                elif recheck_name.lower() == 'menu':
                    return 'menu'
                elif recheck_name.lower() == "log out":
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
