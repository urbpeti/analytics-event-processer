import os


class BaseConfig:
    """Base configuration."""
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = 'dummy'
    AWS_SECRET_KEY = 'dummy'
    JWT_SECRET_KEY = 'secret'
    DYNAMODB_ENDPOINT = 'http://localstack:4569'


class TestingConfig(BaseConfig):
    """Testing configuration."""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTIN = True
    DEBUG = True
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = 'dummy'
    AWS_SECRET_KEY = 'dummy'
    JWT_SECRET_KEY = 'test_secret'
    DYNAMODB_ENDPOINT = 'http://localstack-test:4569'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    REGION = 'eu-central-1'
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY', 'dummy')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY', 'dummy')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'test_secret')
    DYNAMODB_ENDPOINT = 'http://localhost:4569'
