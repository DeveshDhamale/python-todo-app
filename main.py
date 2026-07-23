tasks = ["1.python lerning","\n2.solve dsa1","\n3.go to gym"]
def add_task(a):
    # a = input("enter your task ")
    tasks.append(a)
    print("your task :-",a,"added into the tasks")

def delet_task(b):
    tasks.remove(b)
    print("your task is deleted")

def marks_complete():
    task_no = int(input("enter task no you wannt to mark as complete: = "))
    if task_no <=  len(tasks) and task_no >= 0 :
        tasks[task_no - 1] = "✅"+tasks[task_no - 1]
        print(tasks)
    else:
        print("is not valid, plese re enter")
        




while True:
    print("\n __________To-Do-list__________")
    print("1.add task")
    print("2.delete task")
    print("3.mark as complete task")
    print("4.show task list")
    print("5.exist task")

    choise = input("enter your choise from(1-5):- ")

    if(choise == "5"):
        print("app is closing")
        break
    elif(choise not in ["1","2","3","4","5"]):
        print("value is not valid plese enter correct choise")
        continue

    if(choise == "1"):
        a = input("enter your tas:-")
        add_task(a)
        print(tasks)

    if(choise == "2"):
        b = int(input("which task you wanted to delete:- "))
        delet_task(b)
        print(tasks)

    if(choise == "3"):
        marks_complete()

        
        



