"""File helpers for the todo CLI
   keeping these functions small and predictable makes the CLI simpler
   """
# Import Path for easier file and directory manipulation
from pathlib import Path


# Define the default filename as a Path object
FILEPATH = Path("todos.txt")

# Define function to read todos; returns a list of strings
def get_todos(filepath = FILEPATH):
    """Read a text file and return a list of to-do items"""

    # Check if the file exists to prevent errors
    if not filepath.exists():
        # Return an empty list if no file is found
        return []

    # Open the file in 'read' mode using a context manager
    with open(filepath, "r", encoding="utf-8") as file:
        # Read the file and split into a list, removing \n form each line
        return file.read().splitlines()

# Define function to save todos; takes a list and a path
def write_todos(todos, filepath=FILEPATH):
    """Write a list of to-do items to a text file"""

    # Open the file in 'write' mode (this clears the old content)
    with open(filepath,'w', encoding="utf-8") as file:
       # Loop through each item in our clean list
        for item in todos:
            # Write the text to the file and add the newline back
            file.write(item + "\n")