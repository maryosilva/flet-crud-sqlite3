from .connection import get_db_connection, init_db

init_db()

__all__ = ['get_db_connection']