from config import POSTGRES_SYS, POSTGRES_APP
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# 1. ПРОВЕРКА + создание БД только если НЕТ
conn_sys = psycopg2.connect(**POSTGRES_SYS)
conn_sys.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn_sys.cursor()

# Проверяем существование БД
cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'users_db'")
exists = cursor.fetchone()

if not exists:
    cursor.execute("CREATE DATABASE users_db OWNER postgres")
    print("✅ БД users_db создана")
else:
    print("ℹ️ БД users_db уже существует")

cursor.close()
conn_sys.close()

# 2. Создание таблицы ТОЛЬКО если НЕТ
conn_app = psycopg2.connect(**POSTGRES_APP)
cursor = conn_app.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        years INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    )
""")
conn_app.commit()
print(" Таблица users готова")

cursor.close()
conn_app.close()

