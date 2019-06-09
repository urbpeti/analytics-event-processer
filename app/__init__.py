import os

from flask import Flask
from flask_cors import CORS

from app.views.baseview import BaseView

app = Flask(__name__)
CORS(app)

app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)

app.config.from_object(app_settings)

app.add_url_rule('/base', view_func=BaseView.as_view('base'))
