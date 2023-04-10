from utils import todo_functions
import tkinter
import searcher
import time
import os
import PySimpleGUI as sg

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass

sg.theme('DarkAmber')
clock = sg.Text(' ', key='clock')
list_box = sg.Listbox(values=[x for x in todo_functions.get_todos()], enable_events=True, size=(25,5), key='todos')
layout = [[clock], [sg.Text('Add Your Items for the Week, Generates a todos.txt file for you.')],
            [sg.Text('Enter a new Item'), sg.InputText(tooltip="Enter Todo", key="todo")],
            [sg.Text('Do you want to edit an entry'),sg.InputText(tooltip='select an item to edit', key='edit'), sg.Combo([x+1 for x in range(0, len(todo_functions.get_todos()))], key='index_to_edit')],
            [sg.Text('Do you want to create a new file (optional)'),sg.InputText(tooltip="File Name", key="file_name"), sg.Button("Create File")],
            [sg.Text("Currently left to do"), list_box],
            [sg.Button('Add'), sg.Button('Edit'), sg.Button('Show'), sg.Button('Save'), sg.Button('Cancel'), sg.Button('Exit')] ]
window = sg.Window("Your Personal Reminder", layout=layout, font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todo = values['todo']
            todos = todo_functions.get_todos()
            todos.append(todo+"\n")
            todo_functions.write_todos(todos)
            window['todos'].update(values=todos)
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
            exit()
# if event[0] == 'Show':
#     items =todo_functions.get_todos()
#     for idx, item in enumerate(items):
#         layout.append(sg.Text(f"{idx}. {item}"))

window.close()