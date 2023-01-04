from flask import Flask
from pycertify.ext import configuration

def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app)
    return app

def create_app():
    app = minimal_app()
    configuration.load_extentions(app)
    return app


