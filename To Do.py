# TO DO List

def add(ToDo):
    file = open("ToDo.txt",'w')
    for i in ToDo:
        file.write(f"{i}\n")
    file.close()
    return 'successfully updated'

def view():
    file = open("ToDo.txt", 'r')
    show = file.read()
    print(show)
    file.close()


def remove(ToDo):
    rmve = int(input("Please let me know which line you want to remove"))
    val = ToDo.pop(rmve-1)
    add(ToDo)
    return 'successfully removed'


def main():
    print("Welcome to To Do app\nPlease create todays to do tasks")
    Lists = input("Enter tasks with ';' seperated for each  : ")
    ToDo_List = [i.strip() for i in Lists.split(';')]
    add(ToDo_List)
    while True:
        user_prompt = input("Please enter 'view','add','remove','exit' to do necessary action : ")
        if user_prompt.lower() == 'view':

            view()
        elif user_prompt.lower() == 'add':
            add_todo = input("Enter tasks with ';' seperated for each  : ")
            add_todos = [i.strip() for i in add_todo.split(';')]
            ToDo_List.extend(add_todos)
            print(add(ToDo_List))
        elif user_prompt.lower() == 'remove':
            print(remove(ToDo_List))
        elif user_prompt.lower() == 'exit':
            break


if __name__ == "__main__":
    main()
