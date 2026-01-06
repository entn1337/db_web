import psycopg2

# системное соединение
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="pswd"
)

conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

print("автосохранение работает")

cursor = conn.cursor()

print("курсор для SQL-команд создан")

cursor.execute("DROP DATABASE IF EXISTS users_db;")  # удалить бд если существует по имени users_db
cursor.execute("CREATE DATABASE users_db;")  # создать бд по имени users_db 

print("база данных создана")

conn.close()

print("закрыто системное соединение")

conn = psycopg2.connect(host="localhost", dbname="users_db", user="postgres", password="pswd")

print("подключился к рабочей бд")

# создание таблицы users
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        hui INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    )
""")

conn.close()

print("таблица user создана")
