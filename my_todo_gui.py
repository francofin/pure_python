from utils import todo_functions
import tkinter
import searcher
import PySimpleGUI as sg

layout = [[sg.Text('Add Your Items for the Week')],
            [sg.Text('Enter a new Item'), sg.InputText(tooltip="Enter Todo", key="todo")],
            [sg.Text('Do you want to edit an entry'),sg.InputText(key='edit'), sg.Combo([x for x in range(len(todo_functions.get_todos()))], key="index_to_edit")],
            [sg.Text('Do you want to create a new file (optional)'),sg.InputText(tooltip="File Name", key="file_name"), sg.Button("Create File")],
            [sg.Button('Add'), sg.Button('Edit'), sg.Button('Show'), sg.Button('Save'), sg.Button('Cancel'), sg.Button('Exit')] ]
window = sg.Window("Your Personal Reminder", layout=layout, font=('Helvetica', 15))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todo = values['todo']
            todos = todo_functions.get_todos()
            todos.append(todo+"\n")
            todo_functions.write_todos(todos)
        case 'Edit':
            todos = todo_functions.get_todos()
            edited_entry = values['edit']
            item_to_edit = values['index_to_edit']
            item = int(item_to_edit)
            todos[item] = edited_entry+"\n"
            todo_functions.write_todos(todos)
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
# if event[0] == 'Show':
#     items =todo_functions.get_todos()
#     for idx, item in enumerate(items):
#         layout.append(sg.Text(f"{idx}. {item}"))

window.close()