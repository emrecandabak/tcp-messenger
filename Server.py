from Tkinter import *
from socket import *
from threading import *
from ScrolledText import*
import argparse 

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
        self.gettext.insert(END,'client >> %s\n'%text)
        self.gettext.configure(state=DISABLED)
        self.gettext.see(END)
      except:
        break
class App(Thread):
  ap = argparse.ArgumentParser()
  ap.add_argument("-ip" , "--ip",required = True, help="IP address of server.")  
  ap.add_argument("-port","--port",required = True,help ="Which port you want to start server on",type = int)
  args = vars(ap.parse_args())
  SERVER_PORT = "{}".format(args["port"])
  server = socket()
  server.bind(("{}".format(args["ip"]),(int)(SERVER_PORT)))
  server.listen(5)
  client,addr = server.accept()
  def __init__(self, master):
    Thread.__init__(self)
    frame = Frame(master)
    frame.pack()
    self.gettext = ScrolledText(frame, height=10,width=100, state=NORMAL)
    self.gettext.pack()
    sframe = Frame(frame)
    sframe.pack(anchor='w')
    self.pro = Label(sframe, text="Person >>");
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
root = Tk()
root.title('Chat')
app = App(root).start()
root.mainloop()
