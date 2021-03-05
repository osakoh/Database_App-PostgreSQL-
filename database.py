from psycopg2 import pool

from custom_settings import Configure

c = Configure()

# def connect():
#     return psycopg2.connect(user=c.usr,
#                             password=c.pwd,
#                             database=c.db,
#                             host=c.host)


connection_pool = pool.SimpleConnectionPool(minconn=1, maxconn=10, user=c.usr,
                                            password=c.pwd, database=c.db, host=c.host
                                            )
