"""db.py.

Database level utility class for testing against the artist_info schema.
"""

from functools import wraps
import sys

from crud_app import config
from crud_app.connectors.mysql import db_session


CREATE_TABLE_TEST_DATA = """
CREATE TABLE `supreet_node` (
  `id` int(11) PRIMARY KEY,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL
);
"""


DROP_TABLE_TEST_DATA = """
DROP TABLE IF EXISTS supreet_node;
"""


INSERT_TEST_DATA = """
    INSERT INTO `supreet_node`(`id`, `name`,`surname`)
    VALUES (1,'Joffrey','Baratheon'),(2,'Cersei','Lannister');
"""


INSERT_TEST_ALL_DATA = """
    INSERT INTO `supreet_node`(`id`, `name`,`surname`)
    VALUES (1,'Joffrey','Baratheon'),(2,'Cersei','Lannister');
"""


def _exit_if_not_test_environment(session):
    """For safety, only run tests in test environment pointed to sqlite.

    Exit immediately if not in test environment or not pointed to sqlite.
    """
    if config.ENVIRONMENT != config.TEST_ENVIRONMENT:
        sys.exit('Environment must be set to {}.'.format(
            config.TEST_ENVIRONMENT))
    if 'sqlite' not in session.bind.url.drivername:
        sys.exit('Tests must point to sqlite database.')


def test_schema(function):
    """Create and tear down the test DB schema around a function call.

    This just creates the schema and does not seed data. Indvidual test cases
    can use factories to seed data as needed.

    Args:
        function (func): the function to be called after creating the test
        schema.

    Returns:
        Function: The decorated function.
    """
    @wraps(function)
    def call_function_within_db_context(*args, **kwargs):
        # create_itunes_languages()
        create_test_data()

        try:
            function_return = function(*args, **kwargs)
        finally:
            # drop_itunes_languages()
            drop_test_data()

        return function_return
    return call_function_within_db_context


def seed_models(models):
    """Save the given model(s) to the DB."""
    if not hasattr(models, '__iter__'):
        models = [models]

    with db_session() as session:
        _exit_if_not_test_environment(session)
        for model in models:
            session.merge(model)
        session.commit()

""" All Custom functions start here.."""


'''def insert_itunes_languages():
    """Insert data into itunes_languages table."""
    with db_session() as session:
        session.execute(INSERT_ITUNES_LANGUAGES)


def insert_itunes_alllanguages():
    """Insert data into itunes_languages table."""
    with db_session() as session:
        session.execute(INSERT_ITUNES_ALLLANGUAGES)


def create_itunes_languages():
    """Create the `itunes_languages` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        drop_itunes_languages()
        session.execute(CREATE_TABLE_ITUNES_LANGUAGES)


def drop_itunes_languages():
    """Drop the `itunes_languages` table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        session.execute(DROP_TABLE_ITUNES_LANGUAGES)'''


def insert_test_data():
    """Insert data into supreet_node table."""
    with db_session() as session:
        session.execute(INSERT_TEST_DATA)


def insert_test_alldata():
    """Insert data into supreet_node table."""
    with db_session() as session:
        session.execute(INSERT_TEST_ALL_DATA)


def create_test_data():
    """Create the supreet_node table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        drop_test_data()
        session.execute(CREATE_TABLE_TEST_DATA)


def drop_test_data():
    """Drop the supreet_node table."""
    with db_session() as session:
        _exit_if_not_test_environment(session)
        session.execute(DROP_TABLE_TEST_DATA)
