from socket import*
serverName='Localhost'
serverPort=12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
msg=input("Input lowercase sentence: ")
clientSocket=clientSocket.recv(1024)
print(modifiedMsg.decode())
clientSocket.close()