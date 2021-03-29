from socket import *
serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print('The server is ready to receive.')

# Revert
def reverte(string):
    l = list(string)
    i = 0
    for s in l:
        if s.upper() != s:
            l[i] = l[i].upper()
        else:
            l[i] = l[i].lower()
        i += 1

    return ''.join(l)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = reverte(message.decode())
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
