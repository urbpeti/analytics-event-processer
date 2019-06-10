from test.base import BaseTestCase

from app import app, dynamodb
from app.repositories.event import EventRepository
from boto3.dynamodb.conditions import Key, Attr


class EventRepositoryTest(BaseTestCase):
    def setUp(self):
        self._repository = EventRepository(dynamodb)
        self._table = self._empty_table(EventRepository.TABLE_SCHEMA)

    def test_put_event_should_return_with_inserted_element(self):
        self._repository.put_event({
            'uid': 1,
            'timestamp': 1
        })

        response = self._table.query(
            KeyConditionExpression=Key('uid').eq(1)
        )
        item = response['Items'][0]

        self.assertEqual(1, item['uid'])
        self.assertEqual(1, item['timestamp'])

    def test_get_events_by_id_should_return_with_elements_with_the_correct_uid(self):
        self._table.put_item(Item={
            'uid': 1,
            'timestamp': 2
        })

        items = self._repository.get_events_by_id(1)
        item = items[0]

        self.assertEquals(1, len(items))
        self.assertEquals(1, item['uid'])
        self.assertEquals(2, item['timestamp'])

    def _empty_table(self, table_schema):
        self._delete_table(table_schema.get('TableName'))
        return self._create_table(table_schema)

    def _delete_table(self, table_name):
        dynamodb.Table(table_name).delete()

    def _create_table(self, table_schema):
        return dynamodb.create_table(**table_schema)
