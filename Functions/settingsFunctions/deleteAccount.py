from Functions.colours import Colours
import os
from time import sleep as wait
import sys


def deleteAccount(info):
    os.remove('People/' + info['username'] + '.json')
    print(Colours.ResetAll + Colours.lightRed + Colours.bold + info['username'], 'has been deleted' + Colours.ResetAll)
    wait(1)
    os.execv(sys.executable, ['python'] + sys.argv)
