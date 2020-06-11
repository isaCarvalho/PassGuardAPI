from flask import Blueprint, request, jsonify
from controllers.register_controller import RegisterController

register_module = Blueprint('Register', __name__)
register_controller = RegisterController()

@register_module.route('/register', methods=['GET'])
def index():
    data = request.json
    id = 0
    
    if (data != None):
        id = data.get('id')

    return jsonify(register_controller.list(id))

@register_module.route('/register/user', methods=["GET"])
def getByUser():
    data = request.json
    id_user = 0
    
    if (data != None):
        id_user = data.get('id_user')

    return jsonify(register_controller.getRegisterByUser(id_user))

@register_module.route('/register', methods=['POST'])
def save():
    data = request.json

    passwordDescription = data.get('passwordDescription')
    passwordContent = data.get('passwordContent')
    id_user = data.get('id_user')

    return jsonify(register_controller.save(passwordDescription, passwordContent, id_user))

@register_module.route('/register', methods=['PUT'])
def update():
    data = request.json

    id = data.get('id')
    passwordDescription = data.get('passwordDescription')
    passwordContent = data.get('passwordContent')
    id_user = data.get('id_user')

    return jsonify(register_controller.update(passwordDescription, passwordContent, id_user, id))

@register_module.route('/register', methods=['DELETE'])
def delete():
    id = request.json.get('id')

    return jsonify(register_controller.delete(id))