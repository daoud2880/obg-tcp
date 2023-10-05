from socket import *

serverName = "localhost"
serverPort = 40000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentenceForCommand = input('Choose between Random,Subtract,Add,')

sentence = sentenceForCommand

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())


while sentence!='exit':
    clientSocket.send(sentence.encode())
    modifiedSentence=clientSocket.recv(1024)
    print('from server',modifiedSentence.decode())
    sentence=input(sentenceForCommand)
clientSocket.send('exit'.encode())
clientSocket.close()