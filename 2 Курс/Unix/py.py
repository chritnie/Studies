import socket
from datetime import datetime
from pathlib import Path
from wsgiref.handlers import format_date_time
from threading import Thread


ROOT = 'www'


def get_timestamp():
    return format_date_time(datetime.utcnow().timestamp())


def get_body_length(body):
    return len(body.encode())


def get_resource_path(request):
    resource = request.split('\n')[0].split()[1][1:]
    if not resource:
        resource = 'index.html'
    return Path(ROOT, resource)


def get_response(body):
    return f"""HTTP/1.1 200 OK
Date: {get_timestamp()}
Server: SelfMadeServer v0.0.1
Content-Type: text/html
Content-Length: {get_body_length(body)}
Connection: close

{body}"""


def handle(conn):
    with conn:
        request = conn.recv(8192).decode()
        print(request)
        resource_path = get_resource_path(request)
        body = resource_path.read_text()
        conn.send(get_response(body).encode())


def _main():
    with socket.socket() as sock:
        try:
            sock.bind(('', 80))
            print("Using port 80")
        except OSError:
            sock.bind(('', 8080))
            print("Using port 8080")
        sock.listen()
        while True:
            conn, addr = sock.accept()
            print("Connected", addr)
            Thread(target=handle, args=[conn]).start()


if __name__ == '__main__':
    _main()