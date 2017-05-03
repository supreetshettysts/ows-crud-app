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
    surname = Column(String)

    def to_dict(self):
        """to_dict Method.

        Represents to_dict method to convert object into dictionary.

        """
        return {
            'id': self.test_id,
            'name': self.name,
            'surname':self.surname
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
    """Get node for passed node id

    Args:
        nodeid (int): the id of the node.

    Returns:
        response.Response: the node data for the said nodeid.
    """
    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        if result_set:
            node_name = result_set.name
            node_sname = result_set.surname
            nodejson = result_set.to_dict()
        else:
            nodejson = {"message":"No Node exists for given nodeid"}

    return response.Response(message=nodejson)

def delete_node(nodeid):
    """Delete node for passed node id

    Args:
        nodeid (int): the id of the node.

    Returns:
        response.Response: the node data for the said nodeid.
    """
    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        node_name = result_set.name
        nodejson = result_set.to_dict()
        session.delete(result_set)

    return response.Response(message=("Deleted node {}").format(nodejson))

def update_node(nodeid,paramdict):
    """Update node for passed node id

    Args:
        nodeid (int): the id of the node.

    Returns:
        response.Response: the node data for the said nodeid.
    """
    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        # keyvalue_tuples = param_imdict[0]
        # paramdict = keyvalue_tuples # Convert immutable paramter tuples into a key value dictionary
        # paramdict = {t[0]:t[1] for t in keyvalue_tuples} # Convert immutable paramter tuples into a key value dictionary
        node_name = result_set.name
        nodejson = result_set.to_dict()
        for colname,colval in paramdict.items():
            setattr(result_set,colname,colval)
        session.merge(result_set)

    return response.Response(message=("Updated node {} with {}").format(nodejson,paramdict))


