from unittest import TestCase

from app.lib.utility import replace_values


class TestUtility(TestCase):
    def test_replace_values(self):
        dictionary = {
            'Key1': {
                'Key2': 'old value'
            }
        }

        config = {
            'newkey1': {
                'newkey2': {
                    'newkey3': 'Key1.Key2'
                }
            }
        }

        new_dic = replace_values(dictionary, config)

        self.assertEqual(
            {'newkey1': {'newkey2': {'newkey3': 'old value'}}},
            new_dic
        )
