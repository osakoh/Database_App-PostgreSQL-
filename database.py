import psycopg2


def connect():
    return psycopg2.connect(user='postgres', password='0000', database='learning', host='localhost')
