FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """ it reads to-do items from todos.txt.
    """
    with open(filepath, 'r') as file:
        local_todos = file.readlines()
    return local_todos

def write_todos(todos_arg,filepath=FILEPATH):
    """ it writes to-do items from todos_arg.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello.")