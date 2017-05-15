"""Tests for exception handler."""

from unittest.mock import patch

import pytest

from crud_app import api
from crud_app import handlers  # noqa (handlers are imported for test client)


@pytest.fixture
def fixture_client():
    """Create an api test client fixture."""
    return api.app.test_client()


@patch('crud_app.handlers.jsonify', side_effect=Exception())
def test_exception_handler(mock_jsonify, fixture_client):
    """Test an uncaught Exception results in a 500 status code."""
    result = fixture_client.get('/hello/')
    assert result.status_code == 500
