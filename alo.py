import socket, ssl, pprint
#print("Подключено")
import json
import ntpath
from pathlib import Path
import os


def otprtinf(z):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header = 'INFO CTCP'
    print("введите путь\n")
    path = input()
    path = '"path":"' + path + '"'
    data = '{"session":' + '"' + z + '",' + path + '}'
    size = data.__len__()
    final_data = header + "\n" + size.__str__() + "\n" + data
    sock.sendall(final_data.encode())
    while True:
        data1 = sock.recv(1024)
        if not data1:
            break

        else:
            break
    sock.close()
    text = data1.decode('utf-8')
    y1 = text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Ошибка")
    else:
        textjson = text.split("\n")[2]
        jsondata = json.loads(textjson)
        filestructure = jsondata["structure"]
        for item in filestructure:
            isfile = True
            name = item["name"]
            try:
                size = item["size"]
            except KeyError:
                isfile = False
            if isfile == True:
                print("name = "+name+" Это файл")
                print("size = "+size.__str__())
            else:
                print("name = " + name + " Это директория")


def otprreg(login, email, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header ='REG CTCP'
    data = '{"username":' + '"' + login + '"' + ',' + '"email":' + '"' + email + '"' + ',' + '"password":' + '"' + password + '"' + '}'
    size = data.__len__()
    final_data = header+"\n"+size.__str__()+"\n"+data
    #print(final_data)
    sock.sendall(final_data.encode())
    while True:
        data1 = sock.recv(1024)
        if not data1:
            break
        else:
            break
    text = data1.decode('utf-8')
    print(text)
    y1 = text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Ошибка при регистрации, потвторите попытку")
    else:
        print("Вы зарегистрированы, ", email)

    sock.close()


def otprvhod(email, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header ='AUTH CTCP'
    data = '{"email":' + '"' + email + '"' + ',' + '"password":' + '"' + password + '"' + '}'
    size = data.__len__()
    final_data = header+"\n"+size.__str__()+"\n"+data
    sock.sendall(final_data.encode())
    while True:
        data1 = sock.recv(1024)
        if not data1:
            break
        else:
            break
    text = data1.decode('utf-8')
    print(text)
    y1= text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Неправилное имя пользователя или пароль")
    else:
        y = text.split("\n")[2]
        y = json.loads(y)
        z = y["session"]
        print("Вы вошли, ", email)

    sock.close()
    return z


def otprup(z, path1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header ='UPLOAD CTCP'
    file1 = path1
    f = open(file1, 'rb')
    f.seek(0, os.SEEK_END)
    filesize = f.tell()
    f.close()
    print("введите путь куда хотите загрузить\n")
    path = input()+ntpath.basename(path1)
    path = '"path":"'+path+'"'
    data = '{"session":'+'"'+z+'",'+path+',"size":'+'"'+filesize.__str__()+'"}'
    size = data.__len__()
    final_data = header+"\n"+size.__str__()+"\n"+data
    #print(final_data)
    sock.sendall(final_data.encode())
    f = open(file1, 'rb')
    l = f.read(filesize)
    while (l):
        print('Sending...')
        sock.send(l)
        l = f.read(filesize)
    print("Done Sending")
    sock.shutdown(socket.SHUT_WR)
    f.close()
    #sock.close()
    while True:
        data1 = sock.recv(1024)
        if not data1:
           break
        else:
           break
    text = data1.decode('utf-8')
    y1 = text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Ошибка")
    else:
        print("Файл загружен")
    sock.close()


def otprdown(z):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header = 'DOWNLOAD CTCP'
    a = os.getlogin()
    print("введите путь до файла, который хотите скачать\n")
    path = input()
    type = path.split(".")[1]
    name = path.split(".")[0]
    path = '"path":"' + path + '"'
    data = '{"session":'+'"'+z+'",'+path+'}'
    size = data.__len__()
    final_data = header+"\n"+size.__str__()+"\n"+data
    sock.sendall(final_data.encode())
    filename = 'C:/Users/'+a+'/Downloads/'+name+'.'+type
    f = open(filename,'wb')
    while True:
        data1 = sock.recv(1024)
        if not data1:
            break

        else:
            break

    text = data1.decode('utf-8')
    y1 = text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Ошибка")
    else:
        y = text.split("\n")[2]
        y = json.loads(y)
        print("Размер файла: ", y["size"])
        filesize = y["size"]
        print("Receiving...")
        file = sock.recv(filesize)
        while (file):
            f.write(file)
            file = sock.recv(filesize)
        print("Received")
        f.close()
    sock.close()



def otprdel(z):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('26.245.128.62', 5050))
    header = 'DELETE CTCP'
    print("введите путь до файла, который хотите удилать\n")
    path = input()
    path = '"path":"' + path + '"'
    data = '{"session":' + '"' + z + '",' + path + '}'
    size = data.__len__()
    final_data = header + "\n" + size.__str__() + "\n" + data
    sock.sendall(final_data.encode())
    while True:
        data1 = sock.recv(1024)
        if not data1:
            break

        else:
            break

    text = data1.decode('utf-8')
    y1 = text.split("\n")[0]
    if y1 == 'BAD CTCP':
        print("Ошибка")
    else:
        print("Файл удален")
    sock.close()
