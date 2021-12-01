from tkinter import *
import tkinter
from tkinter.ttk import *
import time
import sys
import threading
def progressBar(run_time):
    ws = Tk()
    ws.title('Data Acquisition')
    ws.geometry('600x100')
    pb1 = Progressbar(ws, orient=HORIZONTAL, length=300, mode='determinate')
    pb1.pack(expand=True)
    n=0
    pb1.start(run_time*10*60)
    ws.after(run_time*60*1000,ws.destroy)
    ws.mainloop()
progressBar(2)