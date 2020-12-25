# По этому файлу пайтон понимает что это не просто папка,
# а пакет и будет импортировать отсюда файлы
import pkg_resources
from textwrap import dedent
from datetime import datetime , timedelta
import sys

from . import helpers as h 
from . import storage
from .services import make_connection

def input_task_data(task = None):
    """Ввод данных о задаче"""
    task = dict(task) if task is not None else {}
    data = {}

    data['title'] = h.prompt('Название' , default = task.get('title'))
    
    data['planned'] = h.prompt('Запланированно', default = task.get(
        'planned', datetime.now() + timedelta(days = 1)))

    data['description'] = h.prompt('Описание', default = task.get('description', ''))
    return data

def input_task():
    task_id = h.input_int('Введите id задачи')
    with  make_connection() as conn:
        task = storage.get_task(conn, task_id)
    
        if task is None:
            print(f'Задачи с ID {task_id} нет')
        
        return task
def action_list_task():
    """Вывести список задач"""


def action_show_task():
    """Просмотреть задачу"""


def action_add_task():
    """Добавить задачу"""
    data = input_task_data()
    with make_connection() as conn:
        storage.create_task(conn, **data)
    print(f'''Задача "{data['title']}" создана.''')
    

def action_edit_task():
    """Отредактировать задачу"""
    task = input_task()

    if task is not None:
        data = input_task_data(task)

        with make_connection() as conn:
            storage.update_task(conn, task['id'], **data)

        print(f'Задача "{task["title"]}" успешно отредактирована')


def action_done_task():
    """Завершить задачу"""


def action_reopen_task():
    """Начать хадачу заново"""


def action_show_menu():
    """Показаь меню"""
    print(dedent(
        """
            1.  Вывести список задач
            2.  Просмотреть задачу
            3.  Добавить задачу
            4.  Отредактировать задачу
            5.  Завершить задачу
            6.  Начать задачу заново
            m.  Показать меню
            q.  Выйти
        """
    ))


def action_exit():
    """Выйти"""
    sys.exit(0)

#0 - завершение программы без ошибок


actions = {
    '1' : action_list_task,
    '2' : action_show_task,
    '3' : action_add_task,
    '4' : action_edit_task,
    '5' : action_done_task,
    '6' : action_reopen_task,
    'm' : action_show_menu,
    'q' : action_exit,
}

def main():
    with make_connection() as conn:
        shema_path = pkg_resources.resource_filename(
            __package__,
            'resources/sheme.sql'
        )
        storage.initialize(conn, shema_path)

    action_show_menu()

    while 1:
        cmd = input('\nВведите команду: ').strip()
        action = actions.get(cmd)

        if action:
            action()
        else:
            print(f'Команды {cmd} не существует')