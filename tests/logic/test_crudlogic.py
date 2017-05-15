"""Tests for logic."""
from oto import response

from crud_app.models import crudmodel
from crud_app.logic import crud_logic


def test_get_node_by_nodeid_success(test_node_id, mocker):
    """Test response contents upon success."""
    mocker.patch.object(
        crudmodel, 'get_node_for',
        return_value=response.Response(message=test_node_id))

    result = crud_logic.read_nodeid(test_node_id)
    assert result
    assert result.message == test_node_id


def test_create_new_node_success(test_create_single_node, mocker):
    """Test response contents upon success."""
    mocker.patch.object(
        crudmodel, 'create_node',
        return_value=response.Response(message=test_create_single_node))

    result = crud_logic.add_node(test_create_single_node)
    assert result
    assert result.message == test_create_single_node


def test_update_the_node_success(test_node_id, test_create_single_node,
                                                                    mocker):
    """Test response contents upon success."""
    mocker.patch.object(
        crudmodel, 'update_node',
        return_value=response.Response(message=test_create_single_node))

    result = crud_logic.update_nodeid(test_node_id, test_create_single_node)
    assert result
    assert result.message == test_create_single_node


def test_delete_the_node_success(test_node_id, mocker):
    """Test response contents upon success."""
    mocker.patch.object(
        crudmodel, 'delete_node',
        return_value=response.Response('Node deleted successfully'))

    result = crud_logic.remove_nodeid(test_node_id)
    assert result
    assert result.message == 'Node deleted successfully'
