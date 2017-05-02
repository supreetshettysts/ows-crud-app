"""Application configuration."""

import logging
import os
from os.path import dirname, join
from dotenv import load_dotenv

import newrelic.agent


# Service information
from sqlalchemy.pool import NullPool, StaticPool

# to load .env variables for windows
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

SERVICE_NAME = 'ows-crud_app'
SERVICE_VERSION = '1.0.0'

# Production environment
PROD_ENVIRONMENT = 'prod'
DEV_ENVIRONMENT = 'dev'
QA_ENVIRONMENT = 'qa'
TEST_ENVIRONMENT = 'test'
ENVIRONMENT = os.environ.get('Environment', DEV_ENVIRONMENT)

if ENVIRONMENT == PROD_ENVIRONMENT:
    newrelic.agent.initialize('newrelic.ini')

# Errors and loggers
SENTRY = os.environ.get('SENTRY_DSN') or None
LOGGER_DSN = os.environ.get('LOGGER_DSN')
LOGGER_LEVEL = logging.INFO
LOGGER_NAME = 'ows1'

# Generic handlers
HEALTH_CHECK = '/hello/'

# Database credentials
DB_CREDENTIALS = {
    'database': os.environ.get('CMUS_MYSQL_DATABASE'),
    'host': os.environ.get('CMUS_MYSQL_HOST'),
    'password': os.environ.get('CMUS_MYSQL_PASSWORD'),
    'port': os.environ.get('CMUS_MYSQL_PORT'),
    'user': os.environ.get('CMUS_MYSQL_USER')
}


# Database config
if ENVIRONMENT == TEST_ENVIRONMENT:
    DB_URL = 'sqlite://'
    POOL_CLASS = StaticPool
else:
    DB_URL = (
        'mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8'.format(
            user=DB_CREDENTIALS.get('user'),
            password=DB_CREDENTIALS.get('password'),
            host=DB_CREDENTIALS.get('host'),
            db=DB_CREDENTIALS.get('database')))
    POOL_CLASS = NullPool
