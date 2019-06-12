from test.base import BaseTestCase
from unittest.mock import patch, MagicMock


from app.views.auth import GetTokenView


@patch('app.views.auth.make_response')
class GetTokenViewTest(BaseTestCase):
    def setUp(self):
        self._request_mock = self._patch_lib('app.views.auth.request')
        self._auth_view = GetTokenView()

    @patch('app.views.auth.create_access_token')
    def test_post_should_return_with_auth_token(self, create_access_token_mock, response_mock):
        self._mock_post_body({
            'user_id': 1,
        })

        create_access_token_mock.return_value = b'testtoken'

        self._auth_view.post()

        response_mock.assert_called_once_with(
            b'testtoken',
            200
        )

    @patch('app.views.auth.create_access_token')
    def test_post_should_call_create_access_token(self, create_access_token_mock, response_mock):
        self._mock_post_body({
            'user_id': 1,
        })

        self._auth_view.post()

        create_access_token_mock.assert_called_once_with(identity=1)

    def _mock_post_body(self, data):
        self._request_mock.get_json.return_value = data

    def _patch_lib(self, path):
        patcher = patch(path)
        self.addCleanup(patcher.stop)
        return patcher.start()
