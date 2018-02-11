from flask import Flask
from flask_bootstrap import Bootstrap


footedia = Flask(__name__)
Bootstrap(footedia)

from footedia import routes
