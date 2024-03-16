tasks = {
    'Отставание': ['Задача 1', 'Задача 2', 'задача 3'],
    'В процессе': [],
    'Сделано': []
}


def display_tasks():
    print('Отставание:')
    for task in tasks['Отставание']:
        print(task)
    print('В процессе:')
    for task in tasks['В процессе']:
        print(task)
    print('Сделано:')
    for task in tasks['Сделано']:
        print(task)


def add_task(task_name):
    tasks['Отставание'].append(task_name)


def remove_task(task_name, column):
    if task_name in tasks[column]:
        tasks[column].remove(task_name)
    else:
        print('Задача не найдена в указанном столбце.')


def move_task(task_name, current_column, new_column):
    if task_name in tasks[current_column]:
        tasks[current_column].remove(task_name)
        tasks[new_column].append(task_name)
    else:
        print('Задача не найдена в указанном столбце.')


def task_list() -> object:
    while True:
        display_tasks()
        print('Меню:')
        print('1. Добавить задачу')
        print('2. Удалить задачу')
        print('3. Отметьте задачу как выполненную')
        print('4. Задача перемещения')
        print('5. Выход')
        choice = input('Введите свой выбор: ')

        if choice == '1':
            task_name = input('название задачи: ')
            add_task(task_name)
        elif choice == '2':
            task_name = input('Введите название задачи для удаления: ')
            column = input('Введите имя столбца): ')
            remove_task(task_name, column)
        elif choice == '3':
            task_name = input('Введите название задачи, чтобы отметить ее как выполненную: ')
            move_task(task_name, 'Отставание', 'Сделано')
        elif choice == '4':
            task_name = input('Введите название задачи для перемещения: ')
            current_column = input('Введите название текущего столбца: ')
            new_column = input('Введите новое имя столбца: ')
            move_task(task_name, current_column, new_column)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == '__task_list__':
    task_list()
