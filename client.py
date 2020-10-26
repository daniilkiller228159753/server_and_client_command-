ip = '192.168.3.34'
def start():
       import socket
       import time
       import sys
       import os
       import re
       import smtplib
       import keyboard
       import pyautogui
       s= socket.socket()
       s.connect(('192.168.3.7',5050)) # тут ip
       while True:

              text = s.recv(1024).decode()
              print(text)
              if text == 'realtime':
                     ccc = smtplib.SMTP('smtp.mail.ru',587)
                     ccc.starttls()
                     ccc.login('daniilpro1234567890@mail.ru','Fastplaypro')
                     ccc.sendmail('daniilpro1234567890@mail.ru', 'daniilpro1234567890@mail.ru',time.ctime())
                     ccc.quit()
                     start()
              elif re.search(r'\bprint\b',text):
                     keyboard.write(text[8:],int(text[6:7]))
                     start()
                     os.execl(sys.executable, sys.executable, *sys.argv)
                     start()
              elif re.search(r'\bclick\b',text):
                     cor = int(text[6:8]),(text[10:12])
                     print(cor)
                     pyautogui.click(cor)
                     start()
                     os.execl(sys.executable, sys.executable, *sys.argv)
              elif text== 'skip':
                     pyautogui.click(1871, 1003)
                     start()
              elif text== 'pouse':
                     pyautogui.click(500, 500)
                     start()
              elif text== 'quit':
                     os.system('shutdown -s -t 5')
                     start()
              elif text== 'skip2':
                     pyautogui.click(1221, 964)
                     start()
              elif re.search(r'\bkey\b', text):
                     keyboard.press_and_release(str(text[4:]))
                     start()
              else:
                     start()

              os.execl(sys.executable,sys.executable,* sys.argv)
input()              
start()


#########################################################
#realtime время * на почту *
#skip пропустить рекламу
#skip2 пропустить баннер
#quit выкл комп
#click *** ***(click 121 953) кликнуть на кординаты
#pouse пауза
#print (1) text (пример: 'print 0.1 hello') напечатать на клв
#########################################################

