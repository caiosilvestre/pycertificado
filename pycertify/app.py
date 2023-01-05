from flask import Flask
#from pycertify.ext import configuration
from pycertify.blueprints import restapi
from pycertify.blueprints import views

app = Flask(__name__)

restapi.init_app(app)
views.init_app(app)
#configuration.load_extentions(app)



