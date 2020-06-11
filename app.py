import flask
from flask_cors import CORS
from flask import jsonify, render_template
from blueprints.password_module import password_module
from blueprints.user_module import user_module

app = flask.Flask(__name__)
app.register_blueprint(password_module, url_prefix='/')
app.register_blueprint(user_module, url_prefix='/')

app.config["DEBUG"] = True

CORS(app, resources = {r"/*" : {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify('This page was not found'), 404

if __name__ == '__main__':
    app.run()