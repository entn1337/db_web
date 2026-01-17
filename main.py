# импорты
from flask import Flask, request, jsonify
from config import POSTGRES_APP
from db_ops import get_users, add_user


# объявление объекта фласк
app = Flask(__name__) 


# роут GET (использует функцию get_user (список пользователей))
@app.route('/users' , methods=["GET"])
def get_us():
    connect = get_users()
    return jsonify(connect)


# роут ADD (использует функцию add_user (добавления пользователя))
@app.route('/users', methods=['POST'])
def add_us():
    data = request.json
    name = data['name']
    hui = data['hui']
    email = data['email']
    add_user(name, hui, email)
    return jsonify({'status': 'ok'})


# запуск
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
