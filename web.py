import streamlit as st
import functions


# Load the current todos
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    if todo:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My To-Do App")
st.subheader("This is my Todo App")
st.text("This app is to increase your productivity")

# Display current todos
for index, todo in enumerate(todos):
    # Create a checkbox for each todo
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# Input box to add new items
st.text_input(label="Enter a new task: ",
              placeholder="Add a new todo...",
              on_change=add_todo,
              key="new_todo")
