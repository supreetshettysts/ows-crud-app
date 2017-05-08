"""Test Cases for Test model."""
from crud_app.models import crudmodel
from tests.testutils import db


@db.test_schema
def test_get_by_id():
    """Test for the specified test_id is returned."""
    expected_response = {
        'id': 1, 'name': 'Joffrey', 'surname': 'Baratheon'}

    db.insert_test_data()
    response = crudmodel.get_node_for(1)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_get_by_id_not_found():
    """Test for the specified test_id not found."""
    response = crudmodel.get_node_for(3)
    assert response.message == 'No Node exists for given nodeid'


@db.test_schema
def test_get_all_tests():
    """Test get_all_tests."""
    expected_response = [
        {'id': 1, 'name': 'Joffrey', 'surname': 'Baratheon'},
        {'id': 2, 'name': 'Cersei', 'surname': 'Lannister'}
        ]

    db.insert_test_alldata()
    response = crudmodel.get_nodes_all()

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_get_all_nodes_not_found():
    """Test get all tests not found."""
    response = crudmodel.get_nodes_all()
    assert response.message == 'No nodes found'


@db.test_schema
def test_add_test_data():
    """Test add_test_data."""
    expected_response = 'Successfully added'

    data = {'id': '', 'name': 'Ned', 'surname': 'Stark'}
    response = crudmodel.create_node(data)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_add_valid_data():
    """Test get all tests not found."""
    data = {}
    response = crudmodel.create_node(data)
    assert response.message == 'Blank Node cannot be created'


@db.test_schema
def test_update_test_data():
    """Test update_test_data."""
    expected_response = 'Updated node successfully'

    data = {
        'id': 1, 'name': 'Joffrey', 'surname': 'Lannister'}
    db.insert_test_data()
    response = crudmodel.update_node(data)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_update_with_valid_data():
    """Test for valid data not found."""
    data = {}
    response = crudmodel.update_node(data)
    assert response.message == 'Update parameters cannot be blank'


@db.test_schema
def test_update_test_data_not_found():
    """Test for specified test_id not found."""
    data = {'id': 2, 'name': 'Cersei'}
    response = crudmodel.update_node(data)
    assert response.message == 'No such node found to update'


@db.test_schema
def test_delete_test_data():
    """Test delete_test_data."""
    expected_response = 'Node deleted successfully'

    db.insert_test_data()
    response = crudmodel.delete_node(2)

    assert response.status == 200
    assert response.message == expected_response


@db.test_schema
def test_delete_test_data_not_found():
    """Test for the specified test_id not found."""
    response = crudmodel.delete_node(3)
    assert response.message == 'No node found to delete'
