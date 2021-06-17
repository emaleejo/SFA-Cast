import os
import platform
import threading


# Gets the Operating System the computer is running
# Ex: "Windows", "Darin" - for Mac, "Linux"
def getOS():
    ostype = platform.system()
    return ostype


# Threads to quit and close all windows
def start_quit():
    quit_t = threading.Thread(target=quit, args=())
    quit_t.start()


# Runs/Launches the code by passing a command to the command line
# The getos() is used here because different OS systems use different commands#
def run(file):
    ostype = getOS()
    if(ostype == 'Windows'):
        os.system('py {file}')
    else:
        os.system("python3 {file}")


# pathname = "~/SFACAST-Screenshots" #Defaults path to Desktop if not changed
# pathname() sets the pathnane to .../SFA-CAST/SFACAST-Screenshots
# This sets it to the file in which the program is#
def pathname():
    pathname = "~/SFA-CAST"
    newpath = pathname + "/SFACAST-Screenshots"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath
