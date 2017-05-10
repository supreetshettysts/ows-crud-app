"""Application Handlers.

Requests are redirected to handlers, which are responsible for getting
information from the URL and passing it down to the logic layer. The way
each layer talks to each other is through Response objects which defines the
type status of the data and the data itself.

Please note: the Orchard uses the term handlers over views as convention
for clarity

See:
    oto.response for more details.
"""
from flask import g
from flask import jsonify
from flask import request

from oto.adaptors.flask import flaskify
from oto import response

from crud_app.api import app
from crud_app import config
from crud_app.logic import crud_logic


@app.route('/nodes', methods=['GET'])
def read_allnodes():
    """Read all Nodes

    Args:
        No Args
    """
    return flaskify(crud_logic.read_all_nodes())


@app.route('/node/<int:nodeid>', methods=['GET'])
def read_a_node(nodeid):
    """Read only node with node id passed

    Args:
        nodeid (int): Node ID
    """
    return flaskify(crud_logic.read_nodeid(nodeid))


@app.route('/node/<int:nodeid>', methods=['DELETE'])
def remove_node(nodeid):
    """
    Args:
        nodeid (int): Node ID
    """
    return flaskify(crud_logic.remove_nodeid(nodeid))


@app.route('/node', methods=['PUT'])
def update_node():
    """Update <nodeid> with param values for right keys.

    Args:
        nodeid (int): Node ID
    """
    paramdict = request.get_json()
    return flaskify(crud_logic.update_nodeid(paramdict))


@app.route('/node', methods=['POST'])
def add_node():
    """Update <nodeid> with param values for right keys

    Args:
        nodeid (int): Node ID
    """
    # paramdict = request.args
    paramdict = request.get_json()
    return flaskify(crud_logic.add_node(paramdict))


@app.route(config.HEALTH_CHECK, methods=['GET'])
def health():
    """Check the health of the application."""
    return jsonify({'status': 'ok'})


@app.errorhandler(500)
def exception_handler(error):
    """Default handler when uncaught exception is raised.

    Note: Exception will also be sent to Sentry if config.SENTRY is set.

    Returns:
        flask.Response: A 500 response with JSON 'code' & 'message' payload.
    """
    message = (
        'The server encountered an internal error '
        'and was unable to complete your request.')
    g.log.exception(error)
    return flaskify(response.create_fatal_response(message))
