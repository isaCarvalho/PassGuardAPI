from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

login_module = Blueprint('Login', __name__)
user_controller = UserController()

@login_module.route('/login', methods=['GET'])
def index():
    data = request.json
    email = None
    password = None
    encrypt = None

    if (data != None):
        email = data.get('email')
        password = data.get('password')
        encrypt = data.get('encrypt')

    return jsonify(user_controller.authenticate(email, password, encrypt))