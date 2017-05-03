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

from oto import response
from oto.adaptors.flask import flaskify

from crud_app import config
from crud_app.api import app
from crud_app.logic import hello


@app.route('/', methods=['GET'])
def hello_world():
    """Hello World with an optional GET param "name"."""    
    name = request.args.get('name', '')
    # name = request.args.post('name', '')
    return flaskify(hello.say_hello(name))


@app.route('/<username>', methods=['GET'])
def hello_world_username(username):
    """Hello World on /<username>.

    Args:
        username (str): the user's username.
    """
    return flaskify(hello.say_hello(username))


@app.route('/nodes', methods=['GET'])
def hello_nodes():
    """Hello World on /<username>.

    Args:
        username (str): the user's username.
    """
    return flaskify(hello.hello_nodes_logic())

@app.route('/node/<nodeid>', methods=['GET'])
def hello_node(nodeid):
    """Hello World on /<username>.

    Args:
        username (str): the user's username.
    """
    return flaskify(hello.hello_nodeid(nodeid))

@app.route('/delete/node/<nodeid>', methods=['GET'])
def remove_node(nodeid):
    """
    Args:
        nodeid (int): Node ID 
    """
    return flaskify(hello.remove_nodeid(nodeid))


@app.route('/update/node/<nodeid>/', methods=['GET'])
def update_node(nodeid):
    """Update <nodeid> with param values for right keys

    Args:
        nodeid (int): Node ID 
    """
    paramdict = request.args
    if len(paramdict):
        keyvalue_tuples = dict(paramdict)
        # paramdict = keyvalue_tuples # Convert immutable paramter tuples into a key value dictionary

        paramdict = {k:v[0] for k,v in keyvalue_tuples.items()} # Convertinto a key value dictionary
    else:
        paramdict = {}
    # print(paramdict)
    return flaskify(hello.update_nodeid(nodeid,paramdict))


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
