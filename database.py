from psycopg2 import pool

# def connect():
#     return psycopg2.connect(user=c.usr,
#                             password=c.pwd,
#                             database=c.db,
#                             host=c.host)


# connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, user=c.usr,
#                                             password=c.pwd, database=c.db, host=c.host
#                                             )
class Database:
    """
    connection_pool belongs to the class (Database), it's a static property of the class
    """
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        """ initialise connection as none each time the ConnectionFromPool class is called """
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        __enter__: runs when the with statement is called
        get the connection from the connection_pool
        """
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """ __exit__: runs when we exit the exit statement """
        if exception_type is not None:  # if the exception contains a value other than none.e.g TypeError, AttributeError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()  # save the connection else the data would be lost
        Database.return_connection(self.connection)  # return the connection back to connection pool
