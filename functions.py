"""File helpers for the todo CLI
   keeping these functions small and predictable makes the CLI simpler
   """
from pathlib import Path


FILEPATH = Path("todos.txt")

def get_todos(filepath = FILEPATH):
    """Read a text file and return a list of to-do items"""

    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read().splitlines()

def write_todos(todos, filepath=FILEPATH):
    """Write a list of to-do items to a text file"""

    with open(filepath,'w', encoding="utf-8") as file:
        for item in todos:
            file.write(item + "\n")