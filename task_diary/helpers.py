from datetime import datetime
import appdirs
import os
# Переменная __all__ контролирует что импортировать , если используется *

__all__ = (
    'prompt',
    'input_date',
    'input_datetime',
    'print_table',
    'print_task',
)

def prompt(msg , default = None, type_cast = None):
    while 1:
        value = input(f'{msg}: ')
        if not value:
            return default

        if type_cast is None:
            return value
        
        try:
            return type_cast(value)
        except ValueError as err:
            print(err)


def input_int(msg = 'Введите число', default = None):
    return prompt(msg, default, int)


def input_float(msg = 'Введите сумму', default = None):
    return prompt(msg, default, float)


def input_datetime(msg = 'Введите дату', default = None, ftm = '%Y-%m-%d %H:%M:%S'):   
    # def to_datetime(value):
    #     return datetime.strptime(value, ftm)
    # return prompt(msg, default, type_cast = to_datetime)
    return prompt(msg, default, lambda v: datetime.strptime(v, ftm))

def input_date(msg = 'Введите дату', default = None, ftm = '%Y-%m-%d'):
    value = input_datetime(msg, default, ftm)

    # @fixme: скорее всго упадем в date
    if vars is None:
        return default

    return value.date()


def print_task():
    pass


def print_table():
    pass


def make_dirs_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path, 0o755) # для создания передаем путь и права доступа
    return path


user_config_dir = make_dirs_if_not_exists(appdirs.user_config_dir(__package__))
user_data_dir = make_dirs_if_not_exists(appdirs.user_data_dir(__package__))


# __name__ - содержит имя модуля , если это главный модуль то выведет __main__
if __name__ == '__main__':
    
    # number = prompt('Введи цену', 0, float)
    # print(number, type(number))

    # dt = input_datetime()
    # print(dt, type(dt))
    pass



