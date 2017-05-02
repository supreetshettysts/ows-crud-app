"""Logic for Hello.

Hello World is one of the most complex operations in the world. It requires all
the robots and nanotechnology from Terminator to define whether or not our
future will survive an apocalypse.

In other words: always make sure that whenever you add a description it's
something meaningful that you will enjoy reading days, months, or years later.
One more thing: you will automatically be associated with those, and some of us
really enjoy "git blame".
"""

from oto import response
from crud_app.models import crudmodel


def say_hello(name=None):
    """
    Args:
        name (str): the name to display alongside the Hello.

    Returns:
        Response: the hello message.
    """
    if not name or isinstance(name, str) and not name.strip():
        return response.Response('Hello')

    return response.Response('Hello {}!'.format(name))

def hello_nodes_logic():
    """
    Returns:
        Response: All Nodes in a list.
    """
    res = crudmodel.get_nodes_all()
    if res:
        return res

def hello_nodeid(nodeid):
    """
    Args:
    	nodeid (int): Node ID to display
    Returns:
        Response: Node for the nodeid that's passed as arg
    """
    res = crudmodel.get_node_for(nodeid)
    if res:
    	return res

