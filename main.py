from flask import Flask, request, jsonify
from config import POSTGRES_APP
from db_ops import get_users, add_user



app = Flask(__name__)


@app.route('/users', methods=["GET"])
def get_us():
    users = get_users() 
    return jsonify(users)



@app.route('/users', methods=['POST'])
def add_us():
    data = request.json
    add_user(data['name'], int(data['years']), data['email'])
    return jsonify({'status': 'ok'})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
