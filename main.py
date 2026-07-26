tasks = []
def load_task():
    try:
        with open("todo_data.txt","r") as file:
                for line in file:
                    tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_task():
    with open("todo_data.txt","w")as f:
                for task in tasks:
                    f.write(task + "\n")
    
        
    
def add_task(task):
    tasks.append(task)
    save_task()
    print(f'"{task}"added task sucsessfully')

def show_task():
    if(len(tasks)== 0):
        print("no task exist to show")
        return 
    
    print("\n__________YOUR TASKS__________")

    for index,task in enumerate(tasks,start=1):
        print(f"{index}.{task}")
        

def delete_task():
    if(len(tasks)==0):
        print("no task exist to delete")
        return
    
    try:
        task_no = int(input("inter task no"))
        deleted = tasks.pop(task_no - 1)
        save_task()
        print(f"your task{deleted}.delete sucseffuly")
        show_task()

    except ValueError:
        print("enter correct task no ..")

def marks_complete():
    show_task()
    if(len(tasks) == 0):
        print("your dont have nby task to mark complete")
        return
    

    try:
        task_no = int(input("enter task no to mark as complete:-"))
        if 1 <= task_no <= len(tasks):
            if(tasks[task_no - 1].startswith("✅")):
                
                print("your task is alredy completed")
                return
            tasks[task_no-1] = "✅" + tasks[task_no-1]
            save_task()
            show_task()

    except ValueError:
        print("eneter valid task no..")

load_task()
while True:
    print("\n========== TO-DO APP ==========")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Complete")
    print("4. Show Tasks")
    print("5. Exit")

    choise = input("enter your choise (1-5) : - ")

    if(choise == "1"):
        task = input("enter your task:- ")
        add_task(task)

    elif(choise == "2"):
        delete_task()

    elif(choise == "3"):
        marks_complete()

    elif(choise == "4"):
        show_task()

    elif(choise == "5"):
        print("to do app is closing....")
        break

    else:
        print("enter a valid choise from(1-5)")
    







    

    




    
    


    



