#этот модуль работать с БАЗОЙ ДАННЫХ
from datetime import timedelta


SQL_CREATE_NEW_TASK = 'INSERT INTO diary (title, planned, description) VALUES (?, ?, ?)'

SQL_UPDATE_TASK = 'UPDATE diary SET title=?, planned=? description=? WHERE id=?'

SQL_UPDATE_TASK_STATUS = 'UPDATE diary SET status=? WHERE id=?'

SQL_SELECT_ALL_TASKS =  'SELECT id, title, planned, description, status, created FROM diary'

SQL_SELECT_TASK_BY_PK = f'{SQL_SELECT_ALL_TASKS} WHERE id=?'

SQL_SELECT_TASKS_PER_DATE = f'{SQL_SELECT_ALL_TASKS} WHERE planned BETWEEN ? AND ?'


def initialize(conn, creation_sheme):
    with open(creation_sheme) as f:
        conn.executescript(f.read())


def create_task(conn, title, planned, description = ''):
    conn.execute(SQL_CREATE_NEW_TASK, (title, planned, description))

def update_task(conn, pk, title, planned, description):
    conn.execute(SQL_UPDATE_TASK, (title, planned, description, pk))


def update_task_status(conn, pk, status):
    conn.execute(SQL_UPDATE_TASK_STATUS, (status, pk))


def get_task(conn, pk):
    cursor = conn.execute(SQL_SELECT_TASK_BY_PK, (pk,))
    return cursor.fetchone()


def get_tasks_per_date(conn, date):
    date_end = date + timedelta(hours=23, minutes=59, seconds=59)
    cursor = conn.execute(SQL_SELECT_TASKS_PER_DATE, (date, date_end))
    return cursor.fetchall()


def get_all_tasks(conn):
    return conn.execute(SQL_SELECT_ALL_TASKS).fetchall()

