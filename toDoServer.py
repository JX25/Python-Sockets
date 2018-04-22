import socket
import threading
import sys


class Server:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        print("Server running...")
        self.s.bind(('0.0.0.0',7575))
        self.s.listen(1)

    @staticmethod
    def chosen_function( choose ):
        if choose == "1":
            return "Wyświetlam liste zadań"
        elif choose == "2":
            return "Dodaje nowe zadanie"
        elif choose == "3":
            return "Usuwam zadanie"
        elif choose == "4":
            return "Wyświetlam liste zadań z priorytetem (H/M/L)"
        else:
            return "Wybierz dzialanie"


    def handler(self,c,a):
        newLine = '\n\r'
        while True:
            data = c.recv(2048).decode('Windows-1250')
            for conn in self.connections:
                data = data.upper()
                print(data)
                action = self.chosen_function(data)
                conn.send(action.encode('utf-8'))
            if not data or data == "QUIT" or data == "0":
                self.connections.remove(c)
                c.close()
                break


    def run(self):
        while True:
            c, a = self.s.accept()
            clientThread = threading.Thread(target=self.handler, args=(c,a))
            clientThread.daemon = True
            clientThread.start()
            self.connections.append(c)
            print("Connected: "+ a[0] +":"+str(a[1]) +'\n')

server = Server()
server.run()