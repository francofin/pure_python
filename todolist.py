todos = []

while True:
    action = input("Enter add, show or exit")
    match action:
        case 'add':
            todo = input("Enter Item to do")
            todos.append(todo)
        case 'show':
            for i in range(0, len(todos)):
                print(todos[i])
        case 'exit':
            break

print('Bye')
