from socket import *
import threading 
import random

def handleClient(connectionSocket, addr):
    print(str(addr) + "has connected") #
    sentence = connectionSocket.recv(1024).decode()

    sentenceSplit = sentence.split(";",2)
    if "Random" == sentenceSplit[0]:
        sentence=str(random.randrange(int(sentenceSplit[1]),int(sentenceSplit[2])))
        connectionSocket.send(sentence.encode())
        print(sentence)
    
    sentenceSplit = sentence.split(";",2)
    if "Add" == sentenceSplit[0]:
        result = int(sentenceSplit[1]) + int(sentenceSplit[2])
        sentence = str(result)
        connectionSocket.send(sentence.encode())
        print(sentence)
    
    sentenceSplit = sentence.split(";",2)
    if "Subtract" == sentenceSplit[0]:
        sentence = str(int(sentenceSplit[1]) - int((sentenceSplit[2])))
        connectionSocket.send(sentence.encode())
        print(sentence)
    
    
    while sentence != "exit".strip():
        print("from client: " + sentence)
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        sentence = connectionSocket.recv(1024).decode()
    connectionSocket.close()



serverPort = 40000 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort))
serverSocket.listen(1) 
print('Server is ready to listen') 

while True: 
    connectionSocket, addr = serverSocket.accept() 
    threading.Thread(target=handleClient, args=(connectionSocket,addr)).start()

