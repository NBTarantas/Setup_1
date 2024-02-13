import shutil
import keyboard
import sys
import os

shutil.os.mkdir("C:\\secret")
os.system("attrib +h C:\\secret")

source = "C:\\Users\\User\\Documents\\Electronic Arts\\The Sims 4"
destination = "C:\\secret"
shutil.move(source, destination)

def restore():
    source = "C:\\secret\\The Sims 4"
    destination = "C:\\Users\\User\\Documents\\Electronic Arts"
    shutil.move(source, destination)
    shutil.os.rmdir("C:\\secret")
    
keyboard.wait("ctrl+alt+z")
restore()

sys.exit()