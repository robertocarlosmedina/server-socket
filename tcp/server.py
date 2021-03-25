from socket import *
serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
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
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = reverte(sentence)
    connectionSocket.send(capitalizedSentence.encode())
    # connectionSocket.close()