from socket import *

class Server:

    serverName = "localhost"
    serverPort = 12001
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(1)
    sentence = ''

    print('The server id on state Run.')
    # Revert
    def reverte(self, string):
        l = list(string)
        i = 0
        for s in l:
            # if s.upper() != s:
            #     l[i] = l[i].upper()
            # else:
            #     l[i] = l[i].lower()
            if s.upper() == s:
                l[i] = l[i].lower()
            i += 1

        return ''.join(l)
    # class Server:
    def runServer(self):
        connectionSocket, addr = self.serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode()
        self.sentence += '/'+sentence
        capitalizedSentence = self.reverte(self.sentence)
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()

    def startServer(self):
        while True:
            self.runServer()

server = Server()
server.startServer()
        



# serverName = "localhost"
# serverPort = 12000
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind((serverName, serverPort))
# serverSocket.listen(1)

# print('The server id on state Run.')
# # Revert
# def reverte(string):
#     l = list(string)
#     i = 0
#     for s in l:
#         if s.upper() != s:
#             l[i] = l[i].upper()
#         else:
#             l[i] = l[i].lower()
#         i += 1

#     return ''.join(l)
# # class Server:

    

# while True:
#     connectionSocket, addr = serverSocket.accept()
#     sentence = connectionSocket.recv(1024).decode()
#     capitalizedSentence = reverte(sentence)
#     connectionSocket.send(capitalizedSentence.encode())
    
#     connectionSocket.close()