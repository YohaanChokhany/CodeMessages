from Functions.colours import Colours
from Functions.settingsFunctions.settingsOptions import settingsOptions
from Functions.settingsFunctions.changeUsername import changeUsername
from Functions.settingsFunctions.changeName import changeName
from Functions.settingsFunctions.changePassword import changePassword
from Functions.settingsFunctions.clearMessages import clearMessages
from Functions.settingsFunctions.deleteAccount import deleteAccount
from time import sleep as wait


def settings(info):
    settings_playing = True
    while settings_playing:
        option = settingsOptions()
        if option == 'exit':
            return False
        elif option == 'change username':
            info = changeUsername(info)
            if not info:
                continue
            else:
                try:
                    if info == 'menu':
                        break
                except:
                    return info
        elif option == 'change name':
            info = changeName(info)
            if not info:
                continue
            else:
                try:
                    if info == 'menu':
                        break
                except:
                    return info
        elif option == 'change password':
            info = changePassword(info)
            if not info:
                continue
            else:
                try:
                    if info == 'menu':
                        break
                except:
                    return info
        elif option == 'clear messages':
            cleared_info = clearMessages(info)
            if cleared_info:
                info = cleared_info
                return info
        elif option == 'delete account':
            info = deleteAccount(info)
            return info
