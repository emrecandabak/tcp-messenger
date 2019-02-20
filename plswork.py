# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 21:02:29 2019

@author: emrec
pls work that tyme m8
"""
#!/usr/bin/python

from Tkinter import *
from threading import *
import tkMessageBox
import time
import os

global ipcik
ipcik = ""
portcuk = ""
flag = False

# serverBatch = "python Server.py -ip",ip,"-port",port

def quitWindow(window):
    window.destroy()
class test:
    @staticmethod
    def ipListener(ip1=ipEntry):
        ipcik = ip1.get()
        print ipcik
        return ipcik

def portListener(port1):
    portcuk = port1.widget.get()
    print portcuk
    os.system("python Server.py -ip "+test.ipListener()+" -port "+portcuk+"& pause")
    print "python Server.py -ip "+test.ipListener()+" -port "+portcuk+"& pause"


def modeChooser(mode):
    if mode == 0:
        choosedWindow = Tk()
        quitWindow(firstWindow)
        time.sleep(0.5)
        ipLabel = Label(choosedWindow,text = "IP Address :").pack()
        ipEntry = Entry(choosedWindow)
        ipEntry.bind('<Return>',ipListener)
        ipEntry.pack()
        portLabel = Label(choosedWindow,text = "Port :").pack()
        portEntry = Entry(choosedWindow)
        portEntry.bind('<Return>',portListener)
        portEntry.pack()
        choosedWindow.mainloop()
        
        
    
    
    
firstWindow = Tk()
quitButton = Button(firstWindow,text="Quit",command = lambda : quitWindow(firstWindow)).pack()
serverButton = Button(firstWindow,text = "Server",command = lambda : modeChooser(0)).pack()
firstWindow.mainloop()



