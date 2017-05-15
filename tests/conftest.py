"""Defining fixtures for testing handlers."""

import pytest
# import pytest_mock


@pytest.fixture
def test_node_id():
    """Return a unique node id for testing."""
    return 1


@pytest.fixture
def test_create_single_node():
    """Return a unique node for testing."""
    return {'id': 3, 'name': 'Ned', 'surname': 'Stark'}
