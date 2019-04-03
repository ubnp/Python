import socket

sk = socket.socket()          # 创建客户套接字

sk.connect(('127.0.0.1',8088))   # 尝试连接服务器
while True:  
    info = input('>>>')
    sk.send(bytes(info.encode('utf-8')))

    ret = sk.recv(1024).decode('utf-8')
    print(ret)
    if ret == 'bye':
        sk.send(b'bye')   #返回bye从而使得服务器关闭
        break  
   
sk.close()            # 关闭客户套接字
