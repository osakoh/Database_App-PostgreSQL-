from database import CursorFromConnectionFromPool


class User:
    def __init__(self, id, first_name, last_name, email):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"

    def save_to_db(self):
        """
        saves a user to the database and returns a message on success
        """
        with CursorFromConnectionFromPool() as cursor:  # cursor: used to insert/retrieve data
            cursor.execute("INSERT INTO public.users (first_name, last_name, email)"
                           "VALUES (%s, %s, %s)",
                           (self.first_name, self.last_name, self.email))
            # connection_pool.putconn(conn)  # return the connection back to the pool
        print("Data saved successfully")

    @classmethod
    def load_from_db_with_email(cls, email):
        """
        :param email: used to retrieve data from the database
        :return: the name of the user if it exist in the database, else an error message is shown
        """
        # connect to the database and automatically close the connection cursor: used to insert/retrieve data
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute("SELECT * FROM public.users "
                           "WHERE email=%s", (email,))
            user_data = cursor.fetchone()  # get the first row
            return cls(id=user_data[0], first_name=user_data[1], last_name=user_data[2], email=user_data[3])


"""
        # connect to db
        conn = psycopg2.connect(user='postgres', password='0000', database='learning', host='localhost')
        # cursor: used to insert/retrieve data
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.users (first_name, last_name, email)"
                           "VALUES (%s, %s, %s)",
                           (self.first_name, self.last_name, self.email))
        conn.commit()
        conn.close()
        print("Success")
"""
