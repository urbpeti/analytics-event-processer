import os
import boto3

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

dynamodb = boto3.resource(
    'dynamodb',
    region_name=app.config.get('REGION'),
    endpoint_url=app.config.get('DYNAMODB_ENDPOINT'),
    aws_access_key_id=app.config.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=app.config.get('AWS_SECRET_KEY'),
    aws_session_token=''
)

app.add_url_rule('/base', view_func=BaseView.as_view('base'))
