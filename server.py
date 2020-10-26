import socket
s= socket.socket()
s.bind(('192.168.3.7',12345))
s.listen()
while True:
       text = input('command=====>>>')
       c,addr=s.accept()
       c.send(bytes(text,encoding='utf8'))


