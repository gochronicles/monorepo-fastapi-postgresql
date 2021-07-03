from api import database_manager
from contextlib import contextmanager


@contextmanager
def session():
    try:
        current_session = database_manager.SessionMaker()
        yield current_session
    finally:
        current_session.close()
