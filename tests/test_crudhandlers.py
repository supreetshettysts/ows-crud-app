"""Tests for Handlers."""

import json
from unittest.mock import MagicMock
from unittest.mock import patch
from pytest_mock import mocker

import application
from oto import response

from crud_app import handlers
from crud_app.logic import crud_logic


@patch('crud_app.handlers.g')
def test_exception_handler(mock_g):
    """Verify exception_Handler returns 500 status code and json payload."""
    message = (
        'The server encountered an internal error '
        'and was unable to complete your request.')
    mock_error = MagicMock()
    server_response = handlers.exception_handler(mock_error)
    mock_g.log.exception.assert_called_with(mock_error)

    # assert status code is 500
    assert server_response.status_code == 500

    # assert json payload
    response_message = json.loads(server_response.data.decode())
    assert response_message['message'] == message
    assert response_message['code'] == response.error.ERROR_CODE_INTERNAL_ERROR


def test_get_node(test_node_id, mocker):
    """Test get node data by node id."""
    expected_response = '{"id": 1,"name": "Joffrey","surname": "Baratheon"}'
    mocker.patch.object(
        crud_logic, 'read_nodeid',
        return_value=response.Response(message=expected_response))

    with application.app.test_request_context():
        handler_response = handlers.read_a_node(test_node_id)
        assert handler_response.status_code == 200
        crud_logic.read_nodeid.assert_called_with(test_node_id)


def test_get_node_not_found(test_node_id, mocker):
    """Test get node data with not found error."""
    mocker.patch.object(
        crud_logic, 'read_nodeid',
        return_value=response.create_not_found_response('No Node\
                                             exists for given nodeid'))

    with application.app.test_request_context():
        handler_response = handlers.read_a_node(test_node_id)
        assert handler_response.status_code == 404
        crud_logic.read_nodeid.assert_called_with(test_node_id)


def test_create_node(test_create_single_node, mocker):
    """Test create node."""
    mocker.patch.object(
        crud_logic, 'add_node',
        return_value=response.Response(message='Successfully added'))

    with application.app.test_request_context(
            data=json.dumps(test_create_single_node),
            content_type='application/json'):
        handler_response = handlers.add_node()
        assert handler_response.status_code == 200
        crud_logic.add_node.assert_called_with(test_create_single_node)


def test_update_node(test_node_id, test_create_single_node, mocker):
    """Test update node."""
    mocker.patch.object(
        crud_logic, 'update_nodeid',
        return_value=response.Response(message=test_create_single_node))

    with application.app.test_request_context(
            data=json.dumps(test_create_single_node),
            content_type='application/json'):
        handler_response = handlers.update_node(test_node_id)

        assert handler_response.status_code == 200
        crud_logic.update_nodeid.assert_called_with(test_node_id,
                                                    test_create_single_node)


def test_delete_node(test_node_id, mocker):
    """Test delete node."""
    mocker.patch.object(
        crud_logic, 'remove_nodeid',
        return_value=response.Response(message='Node deleted successfully'))

    with application.app.test_request_context():
        handler_response = handlers.remove_node(test_node_id)

        assert handler_response.status_code == 200
        crud_logic.remove_nodeid.assert_called_with(test_node_id)
