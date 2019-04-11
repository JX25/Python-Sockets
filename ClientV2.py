import socket
import sys
import json

class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    operations = "\nOperacje:\n"+"1) Wyświetl listę zadań\n"+"2) Dodaj nowe zadanie\n"+"3) Usuń zadanie\n"+"4) Wyświetl liste zadań z priorytetem (H/M/L)\n0. Wyjdź\n"

    def showAllTasks(self):
        print("Printing all tasks\n")
        data = {}
        data ['option'] = "1"
        data = json.dumps(data)
        self.s.send(bytes(data.encode()))
        data = self.s.recv(2048)
        if not data:
            print("No data to show")
        else:
            data = json.loads(data)
            print("ID\tNAME\tPRIORITY\tDESCRIPTION")
            for i in range(len(data['tasks'])):
                print(str(data['tasks'][i]['id']) +"\t"+data['tasks'][i]['title'] + "\t" +data['tasks'][i]['priority']
                      + "\t" + data['tasks'][i]['description'])

    def createNewTask(self):
        print("Create new task:\n")
        taskTitle = input("Task title: ")
        taskDescription = input("Task description: ")
        taskPriority = input("Task priority: (H\M\L)")
        taskPriority = taskPriority.upper()
        if taskPriority != "H" and taskPriority != "M" and taskPriority != "L":
            taskPriority = "L"
        data = {}
        data ['option'] = "2"
        data ['title'] = taskTitle
        data ['description'] = taskDescription
        data ['priority'] = taskPriority
        data = json.dumps(data)
        self.s.send(bytes(data.encode()))
        data = self.s.recv(2048)
        if not data:
            print("No data to show")
        else:
            data = json.loads(data)
            print(data)

    def deleteTask(self):
        print("Type task ID which you want to delete: ")
        deleteID = input()
        data = {}
        data ['option'] = "3"
        data ['deleteID'] = deleteID
        data = json.dumps(data)
        self.s.send(bytes(data.encode()))
        data = self.s.recv(2048)
        if not data:
            print("No data to show")
        else:
            data = json.loads(data)
            if data['info'] == False:
                print("Task cannot be deleted, no task with this id")
            else:
                print("Task deleted")

    def showTaskWithPriority(self):
        print("Type tasks prio which list do you want to see: (H\M\L)\n")
        prio = input()
        prio = prio.upper()
        if prio != 'H' and prio != 'M' and prio != 'L':
            prio = 'L'
        data = {}
        data ['option'] = "4"
        data ['prio'] = prio
        data = json.dumps(data)
        self.s.send(bytes(data.encode()))
        data = self.s.recv(2048)
        if not data:
            print("No data to show")
        else:
            data = json.loads(data)
            print("ID\tNAME\tPRIORITY\tDESCRIPTION")
            for i in range(len(data['tasks'])):
                print(str(data['tasks'][i]['id']) +"\t"+data['tasks'][i]['title'] + "\t" +data['tasks'][i]['priority']
                      + "\t" + data['tasks'][i]['description'])


    def exitApp(self):
        print("\nExiting application...")
        data = {}
        data['option'] = "0"
        data = json.dumps(data)
        self.s.send(bytes(data.encode()))
        exit(0)

    def __init__(self, address):
        self.s.connect((address,7575))

        while True:
            print(self.operations)
            choice = input("\n>> ")

            if choice == 1 or choice == '1':
                self.showAllTasks()
            elif choice == 2 or choice == '2':
                self.createNewTask()
            elif choice == 3 or choice == '3':
                self.deleteTask()
            elif choice == 4 or choice == '4':
                self.showTaskWithPriority()
            elif choice == 0 or choice == '0' or str(choice).lower() == 'q':
                self.exitApp()
            else:
                print("No actions with this option!\n")

            #data = self.s.recv(2048)
            #if not data:
            #    print('KONIEC')
            #    break
            #print(str(data,'utf-8'))
            #print('\n')
client = Client(sys.argv[1])