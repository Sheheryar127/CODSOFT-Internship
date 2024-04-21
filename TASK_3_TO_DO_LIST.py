#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists

#First make the class by the name of to do list
class Todo_List:
    def __init__(self):
        self.tasks = [] #Empty List

    #Function to add the task
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully")
    #Function to delete the task
    def delete_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
    #Function to display the task
    def display_task(self):
        if self.tasks:
            print("The To do List is : ")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("your to do list is empty")

def main():
    todo_list = Todo_List()

    while True:
        print("To Do List is given below : ")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Task")
        print("4. exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            Task = input("add Task : ")
            todo_list.add_task(Task)
        elif choice == "2":
            task_index = int(input("Enter the index you want to delete : ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            todo_list.display_task()
        elif choice == "4":
            print("exit")
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()

