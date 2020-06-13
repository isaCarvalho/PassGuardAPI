import flask
from flask_cors import CORS
from flask import jsonify, render_template
from blueprints.register_module import register_module
from blueprints.user_module import user_module
from blueprints.login_module import login_module

app = flask.Flask(__name__)
app.register_blueprint(register_module, url_prefix='/api/v1')
app.register_blueprint(user_module, url_prefix='/api/v1')
app.register_blueprint(login_module, url_prefix='/api/v1')

app.config["DEBUG"] = True

CORS(app, resources = {r"/*" : {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/createAccount', methods=['GET'])
def createAccount():
    return render_template('createAccount.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run()