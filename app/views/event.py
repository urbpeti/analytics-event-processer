from flask.views import MethodView
from flask import request, make_response, current_app

from app.lib.encoders import DecimalEncoder
from botocore.exceptions import ClientError

import json
from datetime import datetime


class EventView(MethodView):
    def __init__(self, event_repository):
        self._event_repository = event_repository

    def post(self):
        json_data = request.get_json()
        self._set_timestamp(json_data)

        current_app.logger.info('EventView post')

        try:
            item = self._event_repository.put_event(json_data)
            current_app.logger.info('EventView event stored in db')

            return make_response(json.dumps(item, indent=4, cls=DecimalEncoder), 200)
        except ClientError as e:
            current_app.logger.error(e.response['Error']['Message'])

            return make_response('Error occured', 500)

    def get(self):
        current_app.logger.info('List analytic events')
        items = self._event_repository.get_events_by_id(1)
        return make_response(json.dumps(items, indent=4, cls=DecimalEncoder), 200)

    def _set_timestamp(self, data):
        data['timestamp'] = datetime.now().timestamp()
