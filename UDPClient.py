from socket import *

serverName = 'localhost'
serverPort = 8080

# AF_INET: IPv4 네트워크 사용
# SOCK_DGRAM: UDP 소켓 사용
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sesntence:').encode()

# 소켓을 통한 바이트 전송을 위해 encode()를 사용하여 문자열 타입 메시지를 바이트 타입으로 변환한다. 목적지 주소 및 포트를 메시지에 붙히고 그 패킷을 프로세스의 소켓인 clientSocket으로 보낸다. 클라이언트의 포트는 OS가 직접 할당한다.
clientSocket.sendto(message, (serverName, serverPort))

# 데이터 수신 대기
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
