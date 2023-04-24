# Import the necessary libraries
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database engine
# SQLAlchemy will create a SQLite database file named 'mydatabase.db' in the same directory as your Python file
engine = create_engine('sqlite:///mydatabase.db')

# Define a database model for the 'users' table
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    link = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

# Add a new user to the database
session = Session()
Shahzeb = User(name='Shahzeb', age=16, link="something")
Zaryab = User(name='Zaryab', age=17, link="I don't know")
Hira = User(name='Hira', age=21, link="She is Shahzeb's Love")
session.add(Shahzeb)
session.add(Zaryab)
session.add(Hira)
session.commit()

# Retrieve users from the database
users = session.query(User).all()

# Print out the user data
print('The users in the database are:')
for user in users:
    print(f'{user.name} is {user.age} years old and their link is {user.link}')

print('Yay, the database is working!')
