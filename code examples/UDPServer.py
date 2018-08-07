from socket import*

serverPort = 12000
clientsocket = socket(AF_INET,SOCK_DGRAM)

serverSocket.bind(('',serverPort))
message = row_input("The server is ready to receive")
while True:
    message,clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)