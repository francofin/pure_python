FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as f:
        todos_local = f.readlines()
    return todos_local

def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, 'w') as f:
        f.writelines(todos_args)

if __name__ == "__main__":
    print("File Ready")