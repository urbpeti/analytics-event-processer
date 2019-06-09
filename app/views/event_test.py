from test.base import BaseTestCase
from unittest.mock import patch, MagicMock
from botocore.exceptions import ClientError
import decimal


from app.views.event import EventView


@patch('app.views.event.make_response')
class EventViewTest(BaseTestCase):
    def setUp(self):
        self._request_mock = self._patch_lib('app.views.event.request')
        self._event_repository = MagicMock()
        self._event_view = EventView(self._event_repository)

    @patch('app.views.event.json')
    def test_post_should_store_event_with_timestamp(self, json_mock, _):
        self._mock_timestamp(123.0)
        self._mock_post_body({
            'uid': 1,
            'event_type': 'play_sound'
        })
        json_mock.dumps.return_value = '{}'

        self._event_view.post()

        self._event_repository.put_event.assert_called_once_with({
            'uid': 1,
            'timestamp': 123.0,
            'event_type': 'play_sound'
        })

    def test_post_should_return_with_http_ok(self, make_response_mock):
        self._mock_timestamp(123.0)
        self._event_repository.put_event.return_value = {
            'uid': decimal.Decimal(1),
            'timestamp': decimal.Decimal(123.0)
        }

        self._event_view.post()

        make_response_mock.assert_called_once_with(
            '{\n    "uid": 1,\n    "timestamp": 123\n}', 200
        )

    def test_post_should_return_internal_server_error_when_repositry_throw_exception(self, make_response_mock):
        self._mock_timestamp(123.0)
        self._event_repository.put_event.side_effect = ClientError(
            error_response={"Error": {"Message": ''}}, operation_name='insert'
        )

        self._event_view.post()

        make_response_mock.assert_called_once_with(
            'Error occured', 500
        )

    def _mock_post_body(self, data):
        self._request_mock.get_json.return_value = data

    def _mock_timestamp(self, ts):
        dt = self._patch_lib('app.views.event.datetime')
        dt.now.return_value.timestamp.return_value = ts
        return dt

    def _patch_lib(self, path):
        patcher = patch(path)
        self.addCleanup(patcher.stop)
        return patcher.start()
