"""Defining fixtures for testing handlers."""

import pytest
# import pytest_mock


@pytest.fixture
def test_node_id():
    """Return a track unique id for testing."""
    return 1


@pytest.fixture
def test_create_single_node():
    return {'id': 3, 'name': 'Ned', 'surname': 'Stark'}
