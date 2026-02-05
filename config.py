POSTGRES_SYS = {
    'host': '192.168.1.41',     # Системный сервер PostgreSQL
    'port': 5432,              # Стандартный порт
    'user': 'postgres',        # Суперпользователь
    'password': 'pswd',        # Пароль
    'database': 'postgres'     # Служебная БД для админских операций
}



POSTGRES_APP = {
    'host': '192.168.1.41',     # Тот же сервер
    'port': 5432,
    'user': 'postgres',
    'password': 'pswd',
    'dbname': 'users_db'        # НОВЫЙ ключ для рабочей БД!
}
