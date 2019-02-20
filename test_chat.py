import socket
from threading import Thread
import sys

        
print "What are you going to be ?(one must be server,one must be client.)"
print "1 - Client"
print "2 - Server"

mode = input(": ")
if mode == 1:
    TCP_IP = raw_input("Type server's ip adress.")
    TCP_PORT = input("Type server's port.")
    BUFFER_SIZE = 20


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    def recv():
        while True:
            data = s.recv(1024)
            if not data: sys.exit(0)
            print ''
            print "Person : ",data
         
    def send():
        while True:
            message = raw_input()
            if message == "quit()" and len(message) == 6:s.close()
            s.send(message)
            print "You: ", message



    print 'Connection address:', TCP_IP,":",TCP_PORT
    print "Connected to server successfully."
    s.send("You have connected.")
        
    Thread(target=send).start()     
    Thread(target=recv).start()

elif mode == 2:
    TCP_IP = raw_input("Type -'your'- ip adress.")
    TCP_PORT = input("Type which port you are going to connect.")
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    # s.setblocking(False)
    conn, addr = s.accept()
    
    def recv():
        while True:
            data = conn.recv(1024)
            if not data: sys.exit(0)
            print ''
            print "Person : ",data
         
        
    def send():
        while True:
            message = raw_input()
            if message == "quit()" and len(message) == 6:conn.close()
            conn.send(message)
            print "You: ", message


        
    print 'Connection address:', addr
    Thread(target=send).start()     
    Thread(target=recv).start()




    
    
            
    
    
    
            
         




    

    
    
    
    
    
    
    
    
    