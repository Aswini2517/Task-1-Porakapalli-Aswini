tasks=[]
while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Exit\n")
    choice=input("Enter your choice:")
    if choice=="1":
        task=input("Enter task:")
        tasks.append(task)
        print("\nTask added successfully!")
    elif choice=="2":
        print("\nTasks:")
        if len(tasks)==0:
            print("No tasks available")
        else:
            for i,task in enumerate(tasks,start=1):
                print(i,".",task)
    elif choice=="3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")