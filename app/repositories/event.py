from boto3.dynamodb.conditions import Key, Attr


class EventRepository:
    def __init__(self, dynamodb):
        self._dynamodb = dynamodb

    def put_event(self, event):
        table = self._dynamodb.Table('AnalyticEvents')

        return table.put_item(
            Item=event
        )

    def get_events_by_id(self, id):
        table = self._dynamodb.Table('AnalyticEvents')

        response = table.query(
            KeyConditionExpression=Key('id').eq(id)
        )

        return response['Items']
