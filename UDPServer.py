from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)

# 포트를 해당 소켓에 명시적으로 할당(바인드)한다. 그러면 패킷이 해당 소켓으로 전달된다.
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    # 패킷의 데이터는 message에, 소스 주소는 clientAddress에 할당된다.
    print('Receiving Transmission...')
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Accept client...')
    modifiedMesage = message.decode().upper()
    print('Sending...')
    serverSocket.sendto(modifiedMesage.encode(), clientAddress)
    print('Finished')
