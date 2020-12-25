#Этот модуль предоставляет доступ к внешним ресусом 
from configparser import ConfigParser
import os
import pkg_resources
import shutil
import sqlite3
from .helpers import user_config_dir, user_data_dir
# import os
# assert os.path.exists('/home/nikitos/python/task-diary/')

def make_config(*config_files):
    config = ConfigParser()
    config.read(config_files)   #чтение конфигурационного файла
    return config

def make_default_config():
    filename = os.path.join(user_config_dir, 'config.ini') #Принимает любое количество аргументов и склеивает их нужным слешом для конкретной ОС
    if not os.path.exists(filename):
        default = pkg_resources.resource_filename(__name__, 'resources/config.ini')
        shutil.copyfile(default , filename)
    return make_config(filename)

    
config = make_default_config()

def make_connection(name='db'):
    db_name = os.path.join(user_data_dir, config.get(name, 'db_name'))
    conn = sqlite3.connect(db_name, detect_types = sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn


