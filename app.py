from user import User

# user = User.load_from_db_with_email(email="mymail@mail.com")
user = User('ann@a.com', 'Ann', 'Smith', None)
user.save_to_db()
