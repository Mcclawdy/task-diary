# Файл - манифест
# в этом модуле нужно вызвать функцию setup() , из специального пакета setuptools

from setuptools import setup
# setup(
#     name = Имя пакета
#     version =             Версия пакета 3 число - патч , 2 число - добавили функционал , 1 число - версия(мажорная)
#     description =         Краткое описание пакета
#     url =                 URL адрес пакета / офф сайт
#     license =             Лицензия
#     author =              Автор(ник из гита)
#     author_email =        email адресс для связи
#     packages =            Пакеты, которые нужно скопировать при установке(без рекурсии)
#     py_modules =          Модули, которые нужно скопировать при установке
#     scripts =             Запускаемые из консоли команды
#     install_requires =    Прямые зависимости проекта
#     entry_points =        Входные точки
# )
setup(
    name = 'task-diary', 
    version = '0.0.0',
    description = 'Console diary',
    license = 'Apache License 2.0',
    author = 'nikitos_nikitos',
    author_email = 'mcclawdy@gmail.com',
    packages = ['task_diary', ],
    entry_points = {
        'console_scripts' : [
            'diary = task_diary:main'  #команда = путь до модуля : выполняемая функция 
        ],
        },
    install_requires = [
        'appdirs',
        'prettytable'
    ],
    package_data = {
        'task_diary' : ['resources/*'], #в списке указываем какие ресурсы нужно скопировать 
    }
)

# 