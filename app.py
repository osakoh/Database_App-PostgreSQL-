from database import Database
from user import User
from custom_settings import Configure

c = Configure()

Database.initialise(user=c.usr, password=c.pwd, database=c.db, host=c.host)

print(User.load_from_db_with_email("p@t.com"))

user = User(None, 'Pet', 'Jones', 'email@m.com')
user.save_to_db()
