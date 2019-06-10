from boto3.dynamodb.conditions import Key, Attr


class EventRepository:
    TABLE_NAME = 'AnalyticEvents'
    TABLE_SCHEMA = {
        'TableName': 'AnalyticEvents',
        'KeySchema': [
            {
                'AttributeName': 'uid',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'timestamp',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        'AttributeDefinitions': [
            {
                'AttributeName': 'uid',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'N'
            }
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 5
        }
    }

    def __init__(self, dynamodb):
        self._dynamodb = dynamodb

    def put_event(self, event):
        table = self._dynamodb.Table(EventRepository.TABLE_NAME)

        return table.put_item(
            Item=event
        )

    def get_events_by_id(self, id):
        table = self._dynamodb.Table(EventRepository.TABLE_NAME)

        response = table.query(
            KeyConditionExpression=Key('uid').eq(id)
        )

        return response['Items']
