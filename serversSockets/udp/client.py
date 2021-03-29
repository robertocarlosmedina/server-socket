from socket import *
serverName = "localhost"
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = input('Input lowercase sentence: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print('From Server: ', modifiedMessage.decode())
    clientSocket.close()