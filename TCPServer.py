from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)

# 포트를 해당 소켓에 명시적으로 할당(바인드)한다. 그러면 패킷이 해당 소켓으로 전달된다.
serverSocket.bind(('', serverPort))

# serverSocket은 대기(환영) 소켓이다. 인자는 최대 커넥션 수
serverSocket.listen(1)

print("The server is ready to receive")
while True:
    # 패킷의 데이터는 message에, 소스 주소는 clientAddress에 할당된다.
    print('Receiving Transmission...')

    # 특정 클라이언트가 연결을 시도하면 새 소켓을 생성한다. clientSocket과 connectionSocket 간의 TCP 연결이 수립된다.
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode().upper().encode()
    print('Sending...')
    connectionSocket.send(message)

    # serverSocket은 계속 열려있으므로 다른 클라이언트의 요청도 받을 수 있다.
    connectionSocket.close()
    print('Finished')
