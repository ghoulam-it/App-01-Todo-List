import functions
import FreeSimpleGUI as sg
import time

sg.theme('black')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key="task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), enable_events=True, key="todos", size=(45, 10))

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button,complete_button],
                       [exit_button]],
                   font=('Consolas', 20))


while True:
    event, values = window.read(timeout=200)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["task"].strip()
            if not new_todo:
                sg.popup("Pleas add a task")
                window['task'].update(value='')
                continue

            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['task'].update(value='')

        case "Edit":
            try:
                print(event, values)
                todo_to_edit = values['todos'][0]
                new_todo = values["task"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Pleas select a task first")

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Pleas select a task first")

        case "todos":
            window['task'].update(value=values['todos'][0])


window.close()