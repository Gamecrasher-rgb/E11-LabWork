import os
from tkinter import Tk      # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import filedialog as fd
import subprocess
import os
import os.path
import ntpath
import shutil
import fnmatch
from typing import Pattern


execommand = r"cp /etc/skel/.bashrc  ~/.bashrc"
execommand2 = r"cp /etc/skel/.profile  ~/.profile"
os.system(execommand)
os.system(execommand2)
print("Hopefully your colors are fixed now!")
input("Press enter to exit :)")