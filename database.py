from psycopg2 import pool

from custom_settings import Configure

c = Configure()

# def connect():
#     return psycopg2.connect(user=c.usr,
#                             password=c.pwd,
#                             database=c.db,
#                             host=c.host)


# connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, user=c.usr,
#                                             password=c.pwd, database=c.db, host=c.host
#                                             )
connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=1, user=c.usr,
                                            password=c.pwd, database=c.db, host=c.host
                                            )


class ConnectionFromPool:
    def __init__(self):
        """ initialise connection as none each time the ConnectionFromPool class is called """
        self.connection = None

    def __enter__(self):
        """
        __enter__: runs when the with statement is called
        get the connection from the connection_pool
        """
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ __exit__: runs when we exit the exit statement """
        self.connection.commit()  # save the connection else the data would be lost
        connection_pool.putconn(self.connection)  # return the connection back to connection pool
