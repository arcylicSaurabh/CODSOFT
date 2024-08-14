import os

TODO_FILE = 'todos.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return file.read().splitlines()

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        file.write('\n'.join(tasks))

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: {task}')

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
    else:
        print('Your tasks:')
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def remove_task(index):
    """Remove a task by index."""
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print('Invalid task number.')
        return
    removed_task = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f'Task removed: {removed_task}')

def main():
    """Main function to handle user input."""
    while True:
        print('\nTo-Do List App')
        print('1. View tasks')
        print('2. Add task')
        print('3. Remove task')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input('Enter the task: ')
            add_task(task)
        elif choice == '3':
            view_tasks()
            try:
                index = int(input('Enter the task number to remove: '))
                remove_task(index)
            except ValueError:
                print('Please enter a valid number.')
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()
