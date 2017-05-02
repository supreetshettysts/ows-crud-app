"""Model Sample.

This is just a model sample. It depends on which database you want to use but
basically make sure this file only contains methods and classes that are
related to this model.
"""

from oto import response
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from crud_app.connectors import mysql


class Node(mysql.BaseModel):
    """Test Model.

    Node is the first model created by Supreet

    """

    __tablename__ = 'supreet_node'

    test_id = Column(
        'id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)

    def to_dict(self):
        """to_dict Method.

        Represents to_dict method to convert object into dictionary.

        """
        return {
            'id': self.test_id,
            'name': self.name
        }


def get_by_id(model_id):
    """Get a model by its id.

    Note:
        This is just an example on how to do a request from a microservice
        to another microservice using the owsrequest.request module. The module
        will create the HMAC for the request and will automatically calculate
        the next correlation id.

    Args:
        id (int): the id of the model.

    Returns:
        response.Response: the data of the model.
    """
    model = request.get('ows-microservice', '/resource')
    return response.Response(message=model.json(), status=model.status_code)

def get_nodes_all():
    """Get all nodes

    Args:
        id (int): the id of the model.

    Returns:
        response.Response: the data of the model.
    """
    with mysql.db_session() as session:
            result_set = session.query(Node).all()

            if not result_set:
                return response.Response('test data not available.')

            total_records = [r.to_dict() for r in result_set]
            return response.Response(message=total_records)

def get_node_for(nodeid):
    """Get nodefor passed node id

    Args:
        nodeid (int): the id of the node.

    Returns:
        response.Response: the node data for the said nodeid.
    """
    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        node_name = result_set.name
        nodejson = result_set.to_dict()
    return response.Response(message=nodejson)


