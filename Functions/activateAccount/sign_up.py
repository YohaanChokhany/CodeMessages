from Functions.colours import Colours
import json
import os
from time import sleep as wait
import bcrypt
import getpass


def signup():
    typing_username = True
    while typing_username:
        print(Colours.ResetAll + Colours.underline + "CREATE NEW ACCOUNT" + Colours.ResetAll)
        wait(.1)
        username = input(Colours.ResetAll + 'Username: ' + Colours.darkGray)
        wait(.1)
        character_username_present = False
        for character in username:
            if not character.isalnum() and character != '_':
                character_username_present = True
                break
        if username.lower() == 'exit':
            print(Colours.ResetAll + '')
            wait(.1)
            return False
        elif character_username_present:
            print(Colours.ResetAll + '')
            wait(.1)
            print(Colours.ResetAll + Colours.lightRed + Colours.bold +
                  "Username can only contain alphanumeric characters and '_'")
            wait(.1)
            print(Colours.ResetAll + "")
            wait(.1)
            continue
        elif username.lower() == "menu" or username.lower() == "log out":
            print('')
            wait(.1)
            print(Colours.ResetAll + Colours.bold + Colours.lightRed + "Invalid Username")
            wait(.1)
            print(Colours.ResetAll + "")
            wait(.1)
            continue
        file_name = 'People/' + username.lower() + '.json'
        if os.path.isfile(file_name):
            print("")
            wait(.1)
            print(Colours.ResetAll + Colours.lightRed + Colours.bold + username, 'is taken' + Colours.ResetAll)
            wait(.1)
            print(Colours.ResetAll + '')
            wait(.1)
        else:
            typing_username = False
            typing_name = True
            while typing_name:
                name = input(Colours.ResetAll + 'Full Name: ' + Colours.darkGray)
                wait(.1)
                character_present = False
                i = 0
                for character in name:
                    if not character.isalpha() and character != ' ':
                        character_present = True
                        break
                if character_present:
                    print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Please enter letters only'
                          + Colours.ResetAll)
                    wait(.1)
                    print(Colours.ResetAll + '')
                    wait(.1)
                    continue
                elif name.lower() == 'exit':
                    typing_username = True
                    print(Colours.ResetAll + '')
                    wait(.1)
                    break
                else:
                    typing_password = True
                    while typing_password:
                        password = getpass.getpass(prompt=Colours.ResetAll + 'Password: ' + Colours.darkGray)
                        wait(.1)
                        if password.lower() == 'exit':
                            typing_username = True
                            print(Colours.ResetAll + '')
                            wait(.1)
                            break
                        elif password.lower() == 'menu':
                            continue
                        confirm_password = getpass.getpass(prompt=Colours.ResetAll + 'Confirm Password: '
                                                                  + Colours.darkGray)
                        wait(.1)
                        if password == confirm_password:
                            i = 0
                            password_string = ''
                            while i < len(password):
                                password_string += '*'
                                i += 1
                            info = {'name': name, 'username': username,
                                    'password': bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
                                    'unread': [], 'read': [], 'password_string': password_string}
                            json_file = open(file_name, 'w')
                            json.dump(info, json_file)
                            json_file.close()
                            wait(.1)
                            print(Colours.ResetAll + '')
                            wait(.1)
                            print(Colours.ResetAll + Colours.underline + "HELP" + Colours.ResetAll)
                            wait(.1)
                            print(Colours.ResetAll + "Type 'Help' when in the Main Menu to see this list")
                            wait(.1)
                            print(Colours.ResetAll + "")
                            wait(.1)
                            print(Colours.ResetAll + 'Profile            See your profile')
                            wait(.1)
                            print(Colours.ResetAll + 'Settings           Edit your profile')
                            wait(.1)
                            print(Colours.ResetAll + 'Send               Send messages to your friends')
                            wait(.1)
                            print(Colours.ResetAll + 'Inbox              View the messages your friends have sent you')
                            wait(.1)
                            print(Colours.ResetAll + 'Sign Out           Sign out from your account')
                            wait(.1)
                            print(Colours.ResetAll + '')
                            wait(.1)
                            print(Colours.ResetAll + "'menu'             Returns to Main Menu")
                            wait(.1)
                            print(Colours.ResetAll + "'exit'             Returns to the previous menu")
                            wait(.1)
                            print(Colours.ResetAll + "'delete'           Deletes message in Inbox")
                            wait(.1)
                            print(Colours.ResetAll + "'log out'          Log out of your account")
                            wait(.1)
                            print(Colours.ResetAll + '')
                            wait(.1)
                            print(Colours.ResetAll + "Press 'ENTER' to continue" + Colours.darkGray)
                            wait(.1)
                            input("")
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
                            input('')
                            wait(.1)
                            return info
                        elif confirm_password.lower() == 'exit':
                            typing_username = True
                            typing_password = False
                            print(Colours.ResetAll + '')
                            wait(.1)
                            continue
                        else:
                            print(Colours.ResetAll + Colours.lightRed + Colours.bold + 'Passwords do not match'
                                  + Colours.ResetAll)
                            wait(.1)
                            print(Colours.ResetAll + '')
                            wait(.1)
