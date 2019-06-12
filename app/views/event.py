from flask.views import MethodView
from flask import request, make_response, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.lib.encoders import DecimalEncoder
from app.lib.auth import Auth
from botocore.exceptions import ClientError

import json
from datetime import datetime


class EventView(MethodView):
    def __init__(self, event_repository):
        self._event_repository = event_repository

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        self._handle_post(current_user)

    def _handle_post(self, current_user):
        try:
            json_data = request.get_json()
            self._set_timestamp(json_data)
            self._set_uid(json_data, current_user)

            current_app.logger.info(
                'EventView post user_id: ' + str(current_user)
            )

            item = self._event_repository.put_event(json_data)
            current_app.logger.info('EventView event stored in db')

            return make_response(json.dumps(item, indent=4, cls=DecimalEncoder), 200)

        except ClientError as e:
            current_app.logger.error(e.response['Error']['Message'])
            return make_response('Error occured', 500)
        except Exception as e:
            current_app.logger.error(e)
            return make_response('Error occured', 500)

    def _set_timestamp(self, data):
        data['timestamp'] = int(datetime.now().timestamp())

    def _set_uid(self, data, uid):
        data['uid'] = int(uid)
