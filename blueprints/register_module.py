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

@register_module.route('/register', methods=['POST'])
def save():
    data = request.json

    registerDescription = data.get('registerDescription')
    registerContent = data.get('registerContent')

    return jsonify(register_controller.save(registerDescription, registerContent))

@register_module.route('/register', methods=['PUT'])
def update():
    data = request.json

    id = data.get('id')
    registerDescription = data.get('registerDescription')
    registerContent = data.get('registerContent')

    return jsonify(register_controller.update(id, registerDescription, registerContent))

@register_module.route('/register', methods=['DELETE'])
def delete():
    id = request.json.get('id')

    return jsonify(register_controller.delete(id))
