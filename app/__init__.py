from config import Config
import csv
from flask_httpauth import HTTPBasicAuth
from flask import Flask


app = Flask(__name__)
save_webhook_output_file = 'webhook_output.csv'

app.config['BASIC_AUTH_USERNAME'] = Config.WEBHOOK_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = Config.WEBHOOK_PASSWORD

# If true, then site wide authentication is needed
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = HTTPBasicAuth(app)


@basic_auth.verify_password
def verify_password(username, password):
    # Check username and password here
    return username == app.config['BASIC_AUTH_USERNAME'] \
            and password == app.config['BASIC_AUTH_PASSWORD']


from app import routes
from app.models import *
