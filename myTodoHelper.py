from utils import todo_functions
import time

while True:
    action = input("Enter add, edit, show, save or exit: ")
    action = action.strip()
    match action:
        case 'add':

            todo = input("Enter Item to do") + "\n"

            todos = todo_functions.get_todos()
            todos.append(todo+ '\n')
            todo_functions.write_todos(todos)
        case 'show':
            todos = todo_functions.get_todos()
            for index, i in enumerate(todos):
                print(index, ". ", i)

        case 'edit':
            todos = todo_functions.get_todos()
            print("Existing Todos ", todos)
            for idx, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{idx}. {item}")

            edited_item = input("Which item would you like to edit, enter number: ")
            item = int(edited_item)

            edit_item = input("What is the New Item")
            todos[item] = edit_item
            print("Your New To DOs are: ")
        case 'save':
            todos = todo_functions.get_todos()
            if len(todos) == 0:
                print("No items in list please enter items before saving")
            else:
                todo_functions.write_todos(todos)
        case 'exit':
            break
        case default:
            print("Please Enter an approproate choice")
