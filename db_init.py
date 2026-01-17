# импорты
from config import POSTGRES_SYS, POSTGRES_APP
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# системное подключение
conn_sys = psycopg2.connect(**POSTGRES_SYS)


# автокоммит + курсор
conn_sys.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn_sys.cursor()


# создание рабочей бд
cursor.execute("CREATE DATABASE users_db")


# закрытие курсора и системного соединения
cursor.close()
conn_sys.close()


# подключение к рабочей бд + создание таблицы
conn_app = psycopg2.connect(**POSTGRES_APP)  # переменная = подключение к рабочей бд
cursor = conn_app.cursor()  # ручка запросов к бд
cursor.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        hui INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT NOW()
    )
""")

# коммит + закрытие курсора и линка с рабочей бд
conn_app.commit()
cursor.close()
conn_app.close()

print('все прошло успешно')