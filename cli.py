# Import the time module to get the current date [cite: 1]
import time
# Import our custom file functions from functions.py [cite: 1]
from functions import get_todos, write_todos


# Define the main program function
def run_cli():
    # Get the current time and format it as a readable string [cite: 1]
    now = time.strftime("%b %d, %Y %H:%M:%S")
    # Display the current time to the user [cite: 1]
    print(f"It is {now}")

    # Start an infinite loop to keep the program running [cite: 1]
    while True:
        # Get input from the user and remove extra spaces [cite: 1]
        user_input = input("Type add, show, edit, complete or exit: ").strip()

        # Split the input into two parts: the command and the rest [cite: 1]
        parts = user_input.split(' ', 1)
        # The first word is the command, converted to lowercase [cite: 1]
        command = parts[0].lower()
        # The rest is the 'argument' (like the task name or number) [cite: 1]
        arg = parts[1] if len(parts) > 1 else ""

        # If the user wants to add a new task
        if command == "add":
            # Check if they actually typed a task name
            if arg:
                # Load the current list of tasks [cite: 1]
                todos = get_todos()
                # Add the new task to the list [cite: 1]
                todos.append(arg)
                # Save the updated list back to the file [cite: 1]
                write_todos(todos)
                # If they didn't type a task, show an error
            else:
                print("Error: Specify a task (e.g., 'add buy groceries').")

                # If the user wants to see their list
        elif command == "show":
            # Load the tasks from the file [cite: 1]
            todos = get_todos()
            # If the list is empty, let the user know
            if not todos:
                print("The list is empty.")
                # Loop through the list to print each task with a number [cite: 1]
            for index, item in enumerate(todos):
                # Print the position (starting at 1) and the task text [cite: 1]
                print(f"{index + 1}- {item}")

                # If the user wants to change an existing task
        elif command == "edit":
            # Try to run this code, but watch for mistakes
            try:
                # Convert the argument to a number and subtract 1 for the index [cite: 1]
                index = int(arg) - 1
                # Load the tasks [cite: 1]
                todos = get_todos()
                # Ask the user for the new text for that task [cite: 1]
                new_todo = input("Enter the new todo: ").strip()
                # Replace the old task with the new one [cite: 1]
                todos[index] = new_todo
                # Save the changes [cite: 1]
                write_todos(todos)
                # Catch errors if the user types a letter instead of a number [cite: 1]
            except (ValueError, IndexError):
                print("Error: Provide a valid item number (e.g., 'edit 1').")

                # If the user wants to remove a finished task
        elif command == "complete":
            # Try to run this code, but watch for mistakes
            try:
                # Convert the argument to the list index [cite: 1]
                index = int(arg) - 1
                # Load the tasks [cite: 1]
                todos = get_todos()
                # Remove the task from the list and store its name [cite: 1]
                removed = todos.pop(index)
                # Save the updated list (minus the removed task) [cite: 1]
                write_todos(todos)
                # Confirm to the user what was removed [cite: 1]
                print(f"Todo '{removed}' was completed and removed.")
                # Catch errors if the number is wrong or missing [cite: 1]
            except (ValueError, IndexError):
                print("Error: Provide a valid item number to complete.")

                # If the user wants to close the program
        elif command == "exit":
            # Break the while loop [cite: 1]
            break

            # If the user typed something else entirely
        else:
            print("Command not recognized. Please try again.")

            # Final message before the script ends [cite: 1]
    print("Bye!")


# Standard Python check to ensure the script runs only if executed directly
if __name__ == "__main__":
    # Start the program [cite: 1]
    run_cli()