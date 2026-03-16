import functions
import FreeSimpleGUI as sg
import time


# 1. Improved UI Setup
sg.theme('DarkGrey9')


clock = sg.Text('', key='clock')
input_box = sg.InputText(tooltip="Enter todo", key="task",expand_x=True)
add_button = sg.Button("Add", size=8)

# Added a listbox with a scrollbar
list_box = sg.Listbox(values=functions.get_todos(),
                      enable_events=True,key="todos",size=(45,10))

edit_button = sg.Button("Edit Selected", size=(12, 1),key="Edit")
complete_button = sg.Button("Complete Task", size=(12, 1), key="Complete", button_color = 'green')
exit_button = sg.Button("Exit", size=8)

# Using a more organized structure
layout = [
    [clock],
    [sg.Text("Type in a todo:", font=('Helvetica', 12)), input_box, add_button],
    [sg.Text("Your To-Do list:", font=('Helvetica', 12))],
    [list_box],
    [
        edit_button,
        complete_button,
        sg.Stretch(),
        exit_button
    ]
]
window = sg.Window('To-Do List App',
                   layout=layout,
                   font=('Helvetica',14))

def update_list():
    """a function for updating the todos list"""
    window['todos'].update(values=functions.get_todos())
    window['task'].update(value='')

while True:
    event, values = window.read(timeout=200)

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            new_todo = values["task"].strip()
            if not new_todo:
                sg.popup_error("Please add a task before clicking Add.")
                continue

            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            update_list()

        case "Edit":
            try:
                selected_index = window['todos'].get_indexes()[0]
                new_todo = values["task"].strip()
                print(selected_index)

                if not new_todo:
                    sg.popup_error("Please add a task before clicking Edit.")
                    continue


                todos = functions.get_todos()
                todos[selected_index] = new_todo
                functions.write_todos(todos)
                update_list()
            except IndexError:
                sg.popup_error("Please select a task from the list to edit.")

        case "Complete":
            try:
                selected_index = window['todos'].get_indexes()[0]
                todos = functions.get_todos()
                todos.pop(selected_index)
                functions.write_todos(todos)
                update_list()
            except IndexError:
                sg.popup_error("Please select a task from the list to complete.")

        case "todos":
            if values['todos']:
                window['task'].update(value=values['todos'][0])

window.close()