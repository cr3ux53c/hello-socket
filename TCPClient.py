from socket import *

serverName = 'localhost'
serverPort = 8080

# AF_INET: IPv4 네트워크 사용
# SOCK_STREAM: TCP 소켓 사용
clientSocket = socket(AF_INET, SOCK_STREAM)

# 데이터 통신 전 TCP 연결을 수행하기 위한 핸드쉐이킹
clientSocket.connect((serverName, serverPort))

# 소켓을 통한 바이트 전송을 위해 encode()를 사용하여 문자열 타입 메시지를 바이트 타입으로 변환한다.
message = input('Input lowercase sesntence:').encode()

# 클라이언트 소켓의 포트는 OS가 직접 할당한다.
clientSocket.send(message)

# 데이터 수신 대기
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
