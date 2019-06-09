import os

from flask import Flask

from app.views.baseview import BaseView

app = Flask(__name__)

app.add_url_rule('/base', view_func=BaseView.as_view('base'))
