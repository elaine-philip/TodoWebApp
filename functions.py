FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    todos items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    # you don't need to do close file with this
    # reads existing task from file and stores in list
    return todos_local

def write_todos(todos_args, filepath=FILEPATH):
    """
       Writes the todo items list in the text file.
       """
    with open(filepath, 'w') as file:
        file.writelines(todos_args)
    # writes all tasks into list

