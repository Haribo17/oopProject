# host.py
import socket
import subprocess
import threading

def handle_client(conn):
    data = conn.recv(4096).decode()
    print(f"[요청 수신] {data}")

    # 동적 서버 호출 예시
    response = call_dynamic_server(data)
    conn.sendall(response.encode())
    conn.close()

def call_dynamic_server(data):
    # 서버 동적 로딩 or 모듈 호출
    from server import process_request
    return process_request(data)

def start_host_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 9100))
        s.listen()
        print("[호스트] 클라이언트 요청 대기 중...")

        while True:
            conn, _ = s.accept()
            threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    start_host_server()
