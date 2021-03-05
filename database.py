import psycopg2

from custom_settings import Configure

c = Configure()


def connect():
    return psycopg2.connect(user=c.usr,
                            password=c.pwd,
                            database=c.db,
                            host=c.host)
