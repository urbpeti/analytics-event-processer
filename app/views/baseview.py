from flask.views import MethodView
from flask import make_response


class BaseView(MethodView):
    def get(self):
        return make_response('Hello world', 200)
