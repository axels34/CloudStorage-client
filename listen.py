def listen():
    import socket
    #import logging

    #import time

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.bind(('127.0.0.1', 5050))
    #sock.listen()
    #conn, addr = sock.accept()
    while True:
        data = sock.recv(1024)
        if not data:
            break
        text1 = data.decode('utf-8')
    return text1