from functions import get_todos, write_todos
import time

now = time.strftime("%Y-%m-%d %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, sho, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Invalid input.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed successfully."
            print(message)
        except ValueError:
            print("Invalid input.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command.")

print("Bye!")


