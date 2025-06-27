# Read Tasks
def read_tasks():
    with open ('tasks.txt', 'r') as task_list:
        # print(task_list.readline())
        # print(task_list.readline())
        # print(task_list.readline())
        # print(len(task_list.readline()))

        for line in task_list:
            print(line, end= "")

        
# Create Tasks
def create_tasks():
    task = input("Enter the task: ")

    # Open the file in read+append mode
    with open('tasks.txt', 'r+') as task_list:
        lines = task_list.readlines()
        task_num = len(lines)

        # Move cursor to end to write
        task_list.seek(0, 2)

        if task_num == 0:
            print("File is empty")
            task_num += 1
            task_list.write(f"Task {task_num}: {task}")
        else:
            task_num += 1
            task_list.write(f"\nTask {task_num}: {task}")

    print("Task added successfully.")
               
                
            


    
    


# Update Tasks
def update_tasks():
    with open ('tasks.txt','r+') as task_list:
        content = task_list.read()
        print(task_list.seek(0))
        task_list.seek(0)
        updated = content.replace("old text", "new text")
        print(task_list.readline())
        print(task_list.readline())



# Delete Tasks

create_tasks()
# read_tasks()




