import os


class BaseConfig:
    """Base configuration."""
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = 'dummy'
    AWS_SECRET_KEY = 'dummy'
    DYNAMODB_ENDPOINT = 'http://localstack:4569'


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTIN = True
    DEBUG = True
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = 'dummy'
    AWS_SECRET_KEY = 'dummy'
    DYNAMODB_ENDPOINT = 'http://localstack-test:4569'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'dummy')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'dummy')
    DYNAMODB_ENDPOINT = 'http://localhost:4569'
