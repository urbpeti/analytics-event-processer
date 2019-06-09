
from flask_script import Manager

from app import app, dynamodb

manager = Manager(app)


def createEventTableSchema():
    _create_dynamodb_table(
        TableName='AnalyticEvents',
        KeySchema=[
            {
                'AttributeName': 'uid',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'timestamp',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'uid',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'timestamp',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 5
        }
    )


def _create_dynamodb_table(*args, **kwargs):
    table = dynamodb.create_table(*args, **kwargs)
    print('{} table status: {}'.format(
        kwargs['TableName'],
        table.table_status)
    )

    kwargs['TableName'] = '{}Test'.format(kwargs['TableName'])
    testtable = dynamodb.create_table(*args, **kwargs)
    print('{} table status: {}'.format(
        kwargs['TableName'],
        testtable.table_status)
    )


@manager.command
def provisiondb():
    createEventTableSchema()


if __name__ == "__main__":
    manager.run()
