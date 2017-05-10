"""Model for CRUD app"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from oto import response

from crud_app.connectors import mysql



class Node(mysql.BaseModel):
    """Test Model.

    Node is the first model created by Supreet

    """

    __tablename__ = 'supreet_node'

    id = Column(
        'id', Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    surname = Column(String)

    def to_dict(self):
        """to_dict Method.

        Represents to_dict method to convert object into dictionary.

        """
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }


def get_nodes_all():
    """Get all nodes

    Args:

    Returns:
        response.Response: All the nodes from the table
    """
    with mysql.db_session() as session:
            result_set = session.query(Node).all()

            if not result_set:
                return response.Response(message=response.create_not_found_response('No nodes found'))

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
            response_message = response.Response(message=result_set.to_dict())
        else:
            response_message = response.create_not_found_response('No Node exists for given nodeid')
            

    return response_message


def delete_node(nodeid):
    """Delete node for passed node id

    Args:
        nodeid (int): the id of the node.

    Returns:
        response.Response: the node data for the said nodeid.
    """
    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        if result_set:
            session.delete(result_set)
            response_message = response.Response(message='Node deleted successfully')
        else:
            response_message = response.create_not_found_response('No node found to delete')

    return response_message


def update_node(nodeid,paramdict):
    """Update node for passed node

    Args:
        nodeid: Node ID to update for new column values as passed
        paramdict: Dictionary of column:columnvalue

    Returns:
        response.Response: the node data for the said nodeid.
    """
    print(type(paramdict))
    if nodeid is None:
        return response.create_error_response('Node ID is mandatory')  

    with mysql.db_session() as session:
        result_set = session.query(Node).get(nodeid)
        if result_set:
            for colname, colval in paramdict.items():
                setattr(result_set, colname, colval)
            session.merge(result_set)

            response_message = response.Response(message=result_set.to_dict())
        else:
            response_message = response.create_not_found_response('No such node found to update')

    return response_message


def create_node(paramdict):
    """Update node for passed node id

    Args:
            paramdict: Dictionary column value pairs to be added as a row
    Returns:
        response.Response: the node
    """

    if paramdict is None or 'name' not in paramdict \
                                    or 'surname' not in paramdict:
        return response.create_error_response(message='Name and surname is mandatory',code=500)
    
    with mysql.db_session() as session:
        new_node = Node(name=paramdict.get('name'),surname=paramdict.get('surname'))
        session.add(new_node)
        response_message = response.Response(message=paramdict)
        

    return response_message
