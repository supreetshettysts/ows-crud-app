"""Logic for crud app."""

from crud_app.models import crudmodel


def read_all_nodes():
    """Read all nodes.

    Returns:
        Response: All Nodes in a list.
    """
    res = crudmodel.get_nodes_all()
    return res


def read_nodeid(nodeid):
    """Read a node with nodeid.

    Args:
        nodeid (int): Node ID to display
    Returns:
        Response: Node for the nodeid that's passed as arg
    """
    res = crudmodel.get_node_for(nodeid)
    return res


def remove_nodeid(nodeid):
    """Remove a nodeid with nodeid.

    Args:
        nodeid (int): Node ID to delete
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.delete_node(nodeid)
    return res


def update_nodeid(nodeid, paramdict):
    """Update nodeid with nodeid.

    Args:
        nodeid (int): Node ID to update for new column values as passed
        paramdict (dict): Column names and their new values to be
        used for replacement
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.update_node(nodeid, paramdict)
    return res


def add_node(paramdict):
    """Add node for passed json key value pairs.

    Args:
        paramdict (dict): Column names and their values
    Returns:
        Response: Status code for operation
    """
    res = crudmodel.create_node(paramdict)
    return res
