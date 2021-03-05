from database import connection_pool


class User:

    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"

    def save_to_db(self):
        # connect to the database and automatically close the connection
        with connection_pool.getconn() as conn:
            # cursor: used to insert/retrieve data
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO public.users (first_name, last_name, email)"
                               "VALUES (%s, %s, %s)",
                               (self.first_name, self.last_name, self.email))
        print("Data saved successfully")

    @classmethod
    def load_from_db_with_email(cls, email):
        try:
            with connection_pool.getconn() as conn:  # connect to the database and automatically close the connection
                with conn.cursor() as cursor:  # cursor: used to insert/retrieve data
                    try:
                        cursor.execute("SELECT * FROM public.users "
                                       "WHERE email=%s", (email,))
                        user_data = cursor.fetchone()  # get the first row
                        # print(user_data) return (cls(id=user_data[0], first_name=user_data[1], last_name=user_data[
                        # 2], email=user_data[3]))
                        print(cls(id=user_data[0], first_name=user_data[1], last_name=user_data[2], email=user_data[3]))
                    except TypeError:
                        print(f"User with email '{email}' doesn't exist in the database")
                    except:
                        print(f"Please check the format of your input - '{email}'")
        except AttributeError:
            print(f"Please check your connection settings.")


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
