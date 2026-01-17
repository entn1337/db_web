# импорт рабочей бд и библиотеки пскл
from config import POSTGRES_APP
import psycopg2


# функция подключения
def get_connection():
    connect = psycopg2.connect(**POSTGRES_APP)
    return connect


# функция получения списка пользователей
def get_users():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT id, name, hui, email, created_at FROM users ORDER BY id")
    users = [{"id": row[0], "name": row[1], "hui": row[2], "email": row[3], "created_at": row[4]}
        for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return users


# функция добавления пользователя
def add_user(name, hui, email):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute( "INSERT INTO users (name, hui, email) VALUES (%s, %s, %s)",(name, hui, email))
    connect.commit()
    cursor.close()
    connect.close()


add_user("Andrew", 12, "@ok")
add_user("Mary", 0, "mail@ru")
add_user("John", 1, "@jh.yndxru")
users = get_users()

print(users)
