import socket
HOST = '127.0.0.1'
PORT = 9997

#소켓 객체 생성
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 임의 데이터 송신
client.sendto(b'AAABBBCCC', (HOST, PORT))
# 응답 데이터 수신
data, address = client.recvfrom(4096)
print(data.decode('utf-8'))
print(address.decode('utf-8'))
client.close()

"""
< 가정 >
1. 연결 시도시 반드시 성공할 것으로 간주
2. 대상 서버가 클라이언트의 데이터 전송을 항상 먼저 기다리고 있음
3. 서버는 언제나 적절한 시기에 응답 데이터 전송
"""