import os
from flask import Flask
from .database import init_app
from .commands import init_app

app = Flask(__name__)

# for production
# app.config.from_object(os.environ['APP_SETTINGS'])

# for development
app.config.from_object('config.Development')

# Database
database.init_app(app)
# commands
commands.init_app(app)

from wall import routes