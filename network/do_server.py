import socket

sk = socket.socket()         # 创建客户套接字
#sk.bind(('ip','port'))
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #在bind前加入一条socket配置，重用ip和端口
sk.bind(('127.0.0.1',8088))  #把地址绑定到套接字
sk.listen()                  #监听链接
conn,addr = sk.accept()   #接受客户端链接，请求的address 

while True:
    ret = conn.recv(1024).decode('utf-8')      #接收客户端信息
    if ret == 'bye':
        sk.send(b'bye')  
        break
    
    print(ret)                 #打印客户端信息
    info = input('>>>')
    conn.send(bytes(info,encoding = 'utf-8'))  #向客户端发送信息， bytes类型


conn.close()               #关闭客户端套接字

sk.close()              #关闭服务器套接字(可选)