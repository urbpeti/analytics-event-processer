from flask.views import MethodView
from flask import request, make_response, current_app
from flask_jwt_extended import create_access_token


from datetime import datetime


class GetTokenView(MethodView):
    def post(self):
        try:
            current_app.logger.info('GetToken')
            json_data = request.get_json()
            user_id = json_data['user_id']
            token = create_access_token(identity=user_id)
            return make_response(token, 200)
        except Exception as e:
            current_app.logger.error(e)
            return make_response('Error occured', 500)
