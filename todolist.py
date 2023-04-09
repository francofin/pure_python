todos = []

while True:
    action = input("Enter add, edit, show, save or exit: ")
    action = action.strip()
    match action:
        case 'add':

            todo = input("Enter Item to do") + "\n"


            with open('todos.txt', 'r') as file:
                todos =file.readlines()

            todos.append(todo)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todo_current =file.readlines()
            print(todo_current)
            for index, i in enumerate(todo_current):
                print(index,". " , i)

            # file = open('todos.txt')
            # file.readlines()
            # file.close()
        case 'edit':
            # for i in range(0, len(todos)):
            #     print(str(i)+". "+todos[i])
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            print("Existing Todos ", todos)

            edited_item = input("Which item would you like to edit, enter number: ")
            item = int(edited_item)

            edit_item = input("What is the New Item")
            todos[item] = edit_item
            print("Your New To DOs are: ")
        case 'save':
            if len(todos) == 0:
                print("No items in list please enter items before saving")
            else:
                file = open('todos.txt', 'w')
                file.writelines(todos)
                file.close()

            for i in enumerate(todos):
                print(i)
        case 'exit':
            break
        case default:
            print("Please Enter an approproate choice")



print('Bye')


a = enumerate(['a', 'b', 'c'])
print(a)
print(list(a))
