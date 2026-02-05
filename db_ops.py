from config import POSTGRES_APP  # ← ДОБАВИТЬ
import psycopg2

def get_connection():
    return psycopg2.connect(**POSTGRES_APP)

def get_users():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT id, name, years, email, created_at FROM users ORDER BY id")
    users = [{"id": row[0], "name": row[1], "years": row[2], "email": row[3], "created_at": row[4]}
        for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return users

def add_user(name, hui, email):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (name, years, email) VALUES (%s, %s, %s)", 
                   (name, int(hui), email))  # ← int(hui)
    connect.commit()
    cursor.close()
    connect.close()

# Тестовые данные ТОЛЬКО если пусто
connect = get_connection()
cursor = connect.cursor()
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    add_user("Testin", 12, "@example.com")
cursor.close()
connect.close()
