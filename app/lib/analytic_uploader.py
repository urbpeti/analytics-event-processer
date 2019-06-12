import json
import requests

from app.lib.utility import replace_values


class AnalyticUploader:
    def __init__(self, handlers):
        self._handlers = handlers

    def upload(self, event):
        for handler in self._handlers:
            tranformed_event = handler.transform(event)
            handler.upload(tranformed_event)


class SimpleHTTPHandler:
    def __init__(self, conf_path, service_url):
        self._service_url = service_url
        self._conf_path = conf_path

    def transform(self, event):
        conf = {}
        with open(self._conf_path) as config_file:
            conf = json.load(config_file)
        transformatted_event = replace_values(event, conf)

        return transformatted_event

    def upload(self, event):
        requests.post(self._service_url, json=event)
