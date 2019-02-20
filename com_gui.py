# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:17:02 2019

@author: emrec
"""

from Tkinter import *
import tkMessageBox
from socket import *
from threading import *
from ScrolledText import *
import sys

cors = 0
SERVER_IP = ""
SERVER_PORT = 0
global flag
# flag = False

def modeChooser(mode):
    cors = mode
    tkMessageBox.showinfo("Info","Mode has choosed.")
    if cors == 1:
        withDraw(top)
        Thread(target = serverMode()).start()
        
    return cors


def withDraw(form):
    global top
    form.withdraw()
    
    
def testFunc():
    print("saknk")
    #print(flag)
    flag = True
    print(flag)
    ipValue = SERVER_IP
    portValue = SERVER_PORT
    root = Toplevel(top)
    root.title('Chat')
    app = App(root,SERVER_IP,SERVER_PORT).start()
    root.mainloop()
    

class Receive():
    def __init__(self, server, gettext):
    #Thread.__init__(self)
        self.server = server
        self.gettext = gettext
        while 1:
            try:
                text = self.server.recv(1024)
                if not text: break
                self.gettext.configure(state=NORMAL)
                self.gettext.insert(END,'Person >> %s\n'%text)
                self.gettext.configure(state=DISABLED)
                self.gettext.see(END)
            except:
                break

class App(Thread):
    print("Starting app ...")
    def __init__(self, master,SERVER_IP,SERVER_PORT):
        Thread.__init__(self)
        server = socket()
        server.bind((SERVER_IP,SERVER_PORT))
        server.listen(5)
        client,addr = server.accept()
        frame = Frame(master)
        frame.pack()
        self.gettext = ScrolledText(frame, height=10,width=100, state=NORMAL)
        self.gettext.pack()
        sframe = Frame(frame)
        sframe.pack(anchor='w')
        self.pro = Label(sframe, text="You >>");
        self.sendtext = Entry(sframe,width=80)
        self.sendtext.focus_set()
        self.sendtext.bind(sequence="<Return>", func=self.Send)
        self.pro.pack(side=LEFT)
        self.sendtext.pack(side=LEFT)
        self.gettext.insert(END,'Welcome to Chat\n')
        self.gettext.configure(state=DISABLED)
    def Send(self, args):
        self.gettext.configure(state=NORMAL)
        text = self.sendtext.get()
        if text=="": text=" "
        self.gettext.insert(END,'You >> %s \n'%text)
        self.sendtext.delete(0,END)
        self.client.send(text)
        self.sendtext.focus_set()
        self.gettext.configure(state=DISABLED)
        self.gettext.see(END)
    def run(self):
        Receive(self.client, self.gettext)
          

def serverMode():
    
    selectedWindow = Toplevel(top)
    ipLabel = Label(selectedWindow,text = "IP Address : ").pack(side = TOP,anchor = W)
    ipEntry = Entry(selectedWindow)
    ipEntry.pack()
    # ipButton = Button(selectedWindow,text = "Save",command = lambda : buttonFlag()).pack(side = BOTTOM)
    ipButton = Button(selectedWindow,text = "Save",command = lambda : testFunc())
    ipButton.pack(side = BOTTOM)
    portButton = Button(selectedWindow,text = "Test",command = lambda : testFunc()).pack(side = BOTTOM)
    portLabel = Label(selectedWindow,text = "Port : ").pack(side = TOP,anchor = W)
    portEntry = Entry(selectedWindow)
    portEntry.pack()
    global ipValue
    ipValue = ipEntry.get()
    global portValue
    portValue = portEntry.get()
    print flag
    selectedWindow.mainloop()
    
top = Tk()
quitButton = Button(top, text="Quit", command = lambda : withDraw()).pack()
serverButton = Button(top,text = "Server",command = lambda : modeChooser(1))
clientButton = Button(top,text = "Client",command = lambda : modeChooser(2))
serverButton.pack()
clientButton.pack()
top.mainloop()
# elif cors == 2:












        

    



   