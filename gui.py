import functions
import FreeSimpleGUI as sg
import time
sg.theme("GreenTan")

clock= sg.Text("", key="clock")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values= functions.get_todos(), key="todos", enable_events=True, size=(30, 10))
edit_button = sg.Button("Edit")

exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")

window = sg.Window("My Todo App", layout=[[clock],
                                          [label],
                                          [input_box, add_button],
                                          [list_box, edit_button, complete_button],
                                          [exit_button]], font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y, %H: %M: %S"))
    match event:
        case 'Add':
            try:
                todos = functions.get_todos()
                new_todo = values["todo"]
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window["todo"].update(value="")
            except Exception:
                sg.popup("Please write the todo")

        case 'Edit':
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo 
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except Exception:
                sg.popup("Please select an item", font=("helvetica", 10))

        case 'todos':
            window["todo"].update(value=values["todos"][0])

        case "Exit":
            break

        case "Complete":
            try:
                todos = functions.get_todos()
                todo_to_complete = values["todos"][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window["todo"].update(value="")
            except Exception:
                sg.popup("Please select an item", font=("helvetica", 10))


        case sg.WIN_CLOSED:
            break


window.close()