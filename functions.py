def get_todos(filepath="todos/todos.txt"):
    """ Read a text file and return a list of todo items """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write(todos_arg, filepath="todos/todos.txt"):
     with open(filepath, 'w') as file:
            file.writelines(todos_arg)