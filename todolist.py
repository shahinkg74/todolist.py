from datetime import datetime
from task import Task 

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task_id:
                del self.tasks[i]
                print(f"Task ID {task_id} has been removed.")
                return
        print(f"Task ID {task_id} not found.")

    def edit_task(self, task_id, new_title=None, new_state=None, new_date=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if new_title is not None:
                    task.title = new_title
                if new_state is not None:
                    if new_state:
                        task.done()
                    else:
                        task.undone()
                if new_date is not None:
                    task.date_of_finishing = new_date
                print(f"Task ID {task_id} has been updated.")
                return
        print(f"Task ID {task_id} not found.")

    def display_all(self):
        if not self.tasks:
            print("No tasks in the todo list.")
        else:
            for task in self.tasks:
                print(task)

    def search_by_name(self, name):
        found_tasks = [task for task in self.tasks if name.lower() in task.title.lower()]
        if found_tasks:
            for task in found_tasks:
                print(task)
        else:
            print("No tasks found with that name.")

    def search_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                print(task)
                return
        print(f"Task ID {task_id} not found.")

    def filter_by_status(self, done=None):
        filtered_tasks = [task for task in self.tasks if task.state == done]
        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
        else:
            status = "completed" if done else "pending"
            print(f"No {status} tasks found.")


def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Display All Tasks")
        print("5. Search Task by Name")
        print("6. Search Task by ID")
        print("7. Filter Completed Tasks")
        print("8. Filter Pending Tasks")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == '1':
            task_id = int(input("Enter Task ID: "))
            title = input("Enter Task Title: ")
            date_input = input("Enter Expected Completion Date (YYYY-MM-DD) or leave blank: ")
            date_of_finishing = datetime.strptime(date_input, "%Y-%m-%d") if date_input else None
            task = Task(task_id, title, date_of_finishing=date_of_finishing)
            todo_list.add_task(task)
            print(f"Task '{title}' added.")

        elif choice == '2':
            task_id = int(input("Enter Task ID to remove: "))
            todo_list.remove

        elif choice == '3':
            task_id = int(input("Enter Task ID to edit: "))
            new_title = input("Enter new title (or leave blank to keep current): ")
            new_state_input = input("Enter new state (done/pending or leave blank to keep current): ")
            new_state = None
            if new_state_input.lower() == 'done':
                new_state = True
            elif new_state_input.lower() == 'pending':
                new_state = False
            new_date_input = input("Enter new expected completion date (YYYY-MM-DD) or leave blank to keep current: ")
            new_date = datetime.strptime(new_date_input, "%Y-%m-%d") if new_date_input else None
            
            todo_list.edit_task(task_id, new_title if new_title else None, new_state, new_date)

        elif choice == '4':
            todo_list.display_all()

        elif choice == '5':
            name = input("Enter the name or part of the name to search: ")
            todo_list.search_by_name(name)

        elif choice == '6':
            task_id = int(input("Enter Task ID to search: "))
            todo_list.search_by_id(task_id)

        elif choice == '7':
            todo_list.filter_by_status(done=True)

        elif choice == '8':
            todo_list.filter_by_status(done=False)

        elif choice == '9':
            print("Exiting the Todo List application. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 9.")

if __name__ == "__main__":
    main()