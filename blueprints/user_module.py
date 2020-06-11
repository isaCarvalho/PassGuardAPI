from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_module = Blueprint('User', __name__)
user_controller = UserController()

@user_module.route('/user', methods=['GET'])
def index():
    data = request.json

    id = 0
    if (data != None):
        id = data.get('id')

    return jsonify(user_controller.list(id))

@user_module.route('/user', methods=['POST'])
def save():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    return jsonify(user_controller.save(name, email, password))

@user_module.route('/user', methods=['PUT'])
def update():
    data = request.json

    id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    return jsonify(user_controller.update(id, name, email, password))

@user_module.route('/user', methods=['DELETE'])
def delete():
    id = request.json.get('id')

    return jsonify(user_controller.delete(id))
