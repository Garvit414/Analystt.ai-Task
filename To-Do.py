class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f'Task "{deleted_task["task"]}" deleted.')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index + 1}. {task['task']} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "3":
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
