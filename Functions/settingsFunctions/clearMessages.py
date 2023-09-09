from Functions.colours import Colours
from time import sleep as wait
import json


def clearMessages(info):
    totalMessages = len(info['read']) + len(info['unread'])
    if totalMessages > 0:
        info['read'] = []
        info['unread'] = []
        json_file = open('People/' + info['username'] + '.json', 'w')
        json.dump(info, json_file)
        json_file.close()
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.lightRed + str(totalMessages), 'messages have been deleted' + Colours.ResetAll)
        wait(.1)
        return info
    else:
        print(Colours.ResetAll + '')
        wait(.1)
        print(Colours.ResetAll + Colours.lightRed + 'Error! You have no messages')
        wait(.1)
        return False
