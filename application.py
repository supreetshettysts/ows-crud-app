"""Application."""

from raven.contrib import flask

from crud_app import api
from crud_app import config
from crud_app import handlers  # noqa


if config.SENTRY:
    api.app.config['SENTRY_DSN'] = config.SENTRY
    flask.Sentry(api.app)

app = api.app
