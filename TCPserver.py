from socket	import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()