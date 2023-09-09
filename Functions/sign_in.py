from Functions.colours import Colours
import sys
from time import sleep as wait


def checkSigninMode():
    signing_in = True
    while signing_in:
        print(Colours.ResetAll + Colours.bold + Colours.underline + "LOGIN OR SIGN UP" + Colours.ResetAll)
        wait(.1)
        signin_type = input(Colours.ResetAll + "" + Colours.darkGray)
        wait(.1)
        try:
            signin_type = int(signin_type)
            print(Colours.ResetAll + Colours.red + Colours.bold + 'Please enter a string value' + Colours.ResetAll)
            wait(.1)
        except:
            if signin_type.lower() == 'exit':
                print(Colours.ResetAll + '', end='')
                sys.exit()
            elif signin_type.lower() == 'login':
                mode = 'login'
                print(Colours.ResetAll + '')
                wait(.1)
                return mode
            elif signin_type.lower() == 'sign up':
                mode = 'signup'
                print(Colours.ResetAll + '')
                wait(.1)
                return mode
            else:
                print(Colours.ResetAll + Colours.red + Colours.bold
                      + "Please enter the values 'login' or 'sign up' only" + Colours.ResetAll)
                wait(.1)
                print(Colours.ResetAll + '')
                wait(.1)
