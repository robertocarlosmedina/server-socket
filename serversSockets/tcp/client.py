from socket import *

class User:

    serverName = 'localhost'
    serverPort = 12000
    menssages = None
    
    def serverConectAndSend(self, sentence):
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((self.serverName, self.serverPort))
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        self.menssages = modifiedSentence.decode()
        clientSocket.close()
        return self.menssages
    
    def serverConnectAndGet(self, origin, destination):
        pass



## ________server codes________

# serverName = 'localhost'
# serverPort = 12000
# while True:
#     clientSocket = socket(AF_INET, SOCK_STREAM)
#     clientSocket.connect((serverName, serverPort))
#     sentence = input('Input lowercase sentence: ')
#     clientSocket.send(sentence.encode())
#     modifiedSentence = clientSocket.recv(1024)
#     print('From Server: ', modifiedSentence.decode())
#     clientSocket.close()