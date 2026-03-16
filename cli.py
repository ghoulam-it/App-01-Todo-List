import time
from functions import get_todos, write_todos


# Define the main program function
def run_cli():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"It is {now}")

    while True:
        user_input = input("Type add, show, edit, complete or exit: ").strip()

        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if command == "add":
            if arg:
                todos = get_todos()
                todos.append(arg)
                write_todos(todos)
            else:
                print("Error: Specify a task (e.g., 'add buy groceries').")

        elif command == "show":
            todos = get_todos()
            if not todos:
                print("The list is empty.")
            for index, item in enumerate(todos):
                print(f"{index + 1}- {item}")

        elif command == "edit":
            try:
                index = int(arg) - 1
                todos = get_todos()
                new_todo = input("Enter the new todo: ").strip()
                todos[index] = new_todo
                write_todos(todos)
            except (ValueError, IndexError):
                print("Error: Provide a valid item number (e.g., 'edit 1').")

        elif command == "complete":
            try:
                index = int(arg) - 1
                todos = get_todos()
                removed = todos.pop(index)
                write_todos(todos)
                print(f"Todo '{removed}' was completed and removed.")
            except (ValueError, IndexError):
                print("Error: Provide a valid item number to complete.")

        elif command == "exit":
            break

        else:
            print("Command not recognized. Please try again.")

    print("Bye!")


if __name__ == "__main__":
    run_cli()