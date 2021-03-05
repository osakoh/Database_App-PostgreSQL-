from user import User

user = User(id=None, first_name='Pao', last_name='Tim', email='p@t.com')
user.save_to_db()
# print(User.load_from_db_with_email("ann@a.com"))
# print(User.load_from_db_with_email("tim@a.com"))
# print(User.load_from_db_with_email("pru@s.com"))
