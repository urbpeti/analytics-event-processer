from app.views.event import EventView
from app.repositories.event import EventRepository
import os
import boto3

from flask import Flask
from flask_cors import CORS

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


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

app.add_url_rule(
    '/events', view_func=EventView.as_view('events', event_repository=EventRepository(dynamodb))
)
