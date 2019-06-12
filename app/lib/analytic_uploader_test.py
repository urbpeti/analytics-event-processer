from app.lib.analytic_uploader import AnalyticUploader, SimpleHTTPHandler
from unittest import TestCase
from unittest.mock import MagicMock, mock_open, patch


class AnalyticUploaderTest(TestCase):
    def setUp(self):
        self._handler = MagicMock()
        self._uploader = AnalyticUploader([self._handler])

    def test_uploader_should_call_transform_with_event(self):
        event = {'k1': 'v1'}

        self._uploader.upload(event)

        self._handler.transform.assert_called_once_with(event)

    def test_uploader_should_call_uploader_with_transformed_event(self):
        event = {'k1': 'v1'}
        self._handler.transform.return_value = event

        self._uploader.upload(event)

        self._handler.upload.assert_called_once_with(event)


class SimpleHttpHandlerTest(TestCase):
    def test_transform_should_replace_values_form_old_event(self):
        handler = SimpleHTTPHandler('path/to/conf', 'serviceurl')
        old_event = {
            'key1': {
                'key2': 'value'
            }
        }
        config = '{"newkey": "key1.key2"}'
        with patch('app.lib.analytic_uploader.open', mock_open(read_data=config)):
            transformed_event = handler.transform(old_event)

            self.assertEqual({'newkey': 'value'}, transformed_event)

    @patch('app.lib.analytic_uploader.requests')
    def test_upload_should_send_post_request_to_service_with_event(self, requests_mock):
        handler = SimpleHTTPHandler('path/to/conf', 'serviceurl')
        event = {'key': 'value'}

        handler.upload(event)

        requests_mock.post.assert_called_once_with('serviceurl', json=event)
