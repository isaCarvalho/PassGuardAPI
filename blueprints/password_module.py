from flask import Blueprint, request, jsonify
from controllers.password_controller import PasswordController

password_module = Blueprint('Password', __name__)
password_controller = PasswordController()

@password_module.route('/password', methods=['GET'])
def index():
    data = request.json
    id = 0
    
    if (data != None):
        id = data.get('id')

    return jsonify(password_controller.list(id))

@password_module.route('/password', methods=['POST'])
def save():
    data = request.json

    passwordDescription = data.get('passwordDescription')
    passwordContent = data.get('passwordContent')

    return jsonify(password_controller.save(passwordDescription, passwordContent))

@password_module.route('/password', methods=['PUT'])
def update():
    data = request.json

    id = data.get('id')
    passwordDescription = data.get('passwordDescription')
    passwordContent = data.get('passwordContent')

    return jsonify(password_controller.update(id, passwordDescription, passwordContent))

@password_module.route('/password', methods=['DELETE'])
def delete():
    id = request.json.get('id')

    return jsonify(password_controller.delete(id))
