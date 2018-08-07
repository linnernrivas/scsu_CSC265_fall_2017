from socket import *
import threading
import sys

class Talk:
    clientIP= 'localhost'
    clientPort=12000
    serverPort=13000
    
    def _init_(self,c_ip,c_port,s_port):
        self.clientIP= c_ip
        self.clientPort=c_port
        self.serverPort=s_port
        
    def send(self):
        print('Client is ready!')
        while True:
            try:
                msg=input()
                clientSocket = socket(AF_INET,SOCK_STREAM)
                clientSocket = connect((self.clientIP,self.clientPort))
                clientSocket.send(msg.encode())
                clientSocket.close()
                
            except :
                break   
            
    def recv(self):
        serverSocket=socket(AF_INET,SOCK_STREAM)
        serverSocket.bind('',)
        
        
    def run(self):
        t1=threading.Thread(target=self.recv)
        t2=threading.Thread()
    