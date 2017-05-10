"""Logic for crud app"""
from oto import response

from crud_app.models import crudmodel


def read_all_nodes():
    """
    Returns:
        Response: All Nodes in a list.
    """
    res = crudmodel.get_nodes_all()
    return res


def read_nodeid(nodeid):
    """
    Args:
        nodeid (int): Node ID to display
    Returns:
        Response: Node for the nodeid that's passed as arg
    """
    res = crudmodel.get_node_for(nodeid)
    return res


def remove_nodeid(nodeid):
    """
    Args:
        nodeid (int): Node ID to delete
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.delete_node(nodeid)
    return res


def update_nodeid(nodeid,paramdict):
    """
    Args:
        nodeid (int): Node ID to update for new column values as passed
        paramdict (dict): Column names and their new values to be
        used for replacement
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.update_node(nodeid,paramdict)
    return res


def add_node(paramdict):
    """
    Args:
        paramdict (dict): Column names and their values
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.create_node(paramdict)
    return res
