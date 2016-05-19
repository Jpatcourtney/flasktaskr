
# from datetime import date

from project import db
# from project.models import Task, User

#create the database and table
db.create_all()

# #insert data 
# db.session.add(User('admin', 'ad@min.com', 'admin', 'admin'))

# db.session.add(Task('Finish the tuut', date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1))

# db.session.add(Task('Finish Real Pythont', date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1))

# commit changes to db 
db.session.commit()