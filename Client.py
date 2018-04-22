import socket
import threading

import sys


class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    showTaskList = "1) Wyświetl listę zadań\n"
    addTask = "2) Dodaj nowe zadanie\n"
    removeTask = "3) Usuń zadanie\n"
    showTaskListPriority = "4) Wyświetl liste zadań z priorytetem (H/M/L)\n"
    operations = "Operacje:\n"+showTaskList+addTask+removeTask+showTaskListPriority

    def sendMsg(self):
        while True:
            self.s.send(bytes(input(">>"),'Windows-1250'))

    def __init__(self, address):
        self.s.connect((address,7575))

        inputThread = threading.Thread(target=self.sendMsg)
        inputThread.daemon = True
        inputThread.start()

        while True:
            print(self.operations)
            data = self.s.recv(2048)
            if not data:
                print('KONIEC')
                break
            print(str(data,'utf-8'))
            print('\n')


client = Client(sys.argv[1])