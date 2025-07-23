# client.py
import socket

def send_request(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 9100))  # 호스트 서버에 연결
        s.sendall(data.encode())        # 데이터 전송
        response = s.recv(4096)         # 응답 받기
        return response.decode()

if __name__ == "__main__":
    user_input = input("보낼 요청을 입력하세요: ")
    result = send_request(user_input)
    print("서버 응답:", result)