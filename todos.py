from functions import get_todos, write
import time

now = time.strftime("%b %d, %Y, %H: %M: %S")
print("It is", now)

while True:
    user_action=input("Enter 'add'| 'show'| 'edit'| 'complete' | 'exit' ")
    user_action=user_action.strip()

    if user_action.startswith('add'):
            todo = user_action[4:]

            todos = get_todos("todos/todos.txt")

            todos.append(todo + '\n')

            write(todos)


    elif user_action.startswith('show'):
            todos = get_todos("todos/todos.txt")

            for index,item in enumerate(todos):
                item= item.strip('\n')
                index+=1
                print(f"{index}:{item}")
                

    elif user_action.startswith('edit'):
            try:
                number = user_action[5:]
                number = int(number) - 1
                
                todos = get_todos("todos/todos.txt")

                new_todos=input("Enter new todo: ")
                todos[number]=new_todos + '\n'
                write(todos)

            except ValueError:
                print("Invalid Command!")
                continue
    

    elif user_action.startswith('complete'):
            try:
                todos = get_todos("todos/todos.txt")

                n = int(user_action[9:])
                removed_todo=todos.pop(n-1).strip('\n')

                write(todos)
                
            except Exception as e:
                print("Invalid Command!")
                continue

    elif user_action.startswith('exit'):
            break
    
    else:
        print("Command is not valid!")