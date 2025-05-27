class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"📝 Added: {description} ")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks yet.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_complete()
            print(f"✅ Task {task_number} marked as complete.")
        else:
            print("⚠️ Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed = self.tasks.pop(task_number - 1)
            print(f"🗑️ Removed: {removed.description}")
        else:
            print("⚠️ Invalid task number.")


def run_todo_app():
    todo = ToDoList()

    while True:
        print("\n📋 To-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Choose an option (1-5):")

        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == "3":
            try:
                number = int(input("Enter task number to complete: "))
                todo.complete_task(number)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == "4":
            try:
                number = int(input("Enter task number to remove: "))
                todo.remove_task(number)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye! Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


run_todo_app()
