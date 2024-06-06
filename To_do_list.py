class Task:
    def __init__(self, title, description=''):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = '✓' if self.completed else '✗'
        return f"{status} {self.title}: {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=''):
        task = Task(title, description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries", "Milk, Eggs, Bread")
    todo_list.add_task("Complete assignment")
    todo_list.add_task("Call Alice", "Wish her a happy birthday")
    
    print("To-Do List:")
    todo_list.display_tasks()
    
    print("\nMarking the first task as completed...\n")
    todo_list.mark_task_as_completed(0)
    
    print("Updated To-Do List:")
    todo_list.display_tasks()
    
    print("\nRemoving the second task...\n")
    todo_list.remove_task(1)
    
    print("Final To-Do List:")
    todo_list.display_tasks()


