import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)

name=input('Enter your name please: ')

while True:

    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()
    if user_action.startswith('add'):
        todo=user_action[4:]+'\n'
        todos=functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos=functions.get_todos()
        for index,item in enumerate(todos):
            item=item.strip("\n")
            print(f"{index+1}-{item.title()}")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) -1
            todos = functions.get_todos()
            todos_to_remove=todos[number].strip('\n')
            todos.remove(todos[number])
            print(f"Todo '{todos_to_remove.title()}' was removed from the list.")
            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) -1
            todos = functions.get_todos()
            print(number + 1)
            todos[number]=input('Enter a new todo: ')+'\n'
            functions.write_todos(todos)

        except ValueError:
            print("This command is not valid!")
            continue

    elif user_action.startswith('exit'):
        break

    else :
        print("Unknown command!")

print("Have a nice day,",f"{name.capitalize()}! [:")
