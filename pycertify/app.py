from flask import Flask
#from pycertify.ext import configuration
from pycertify.blueprints import restapi
from pycertify.ext import views

#inicia o app em Flask
app = Flask(__name__)

#chama a modulos api e as páginas
restapi.init_app(app)
views.init_app(app)
#configuration.load_extentions(app)



