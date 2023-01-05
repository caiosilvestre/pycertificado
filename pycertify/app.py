from flask import Flask
from pycertify.ext import configuration

app = Flask(__name__)

configuration.load_extentions(app)



