import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname = {self.fullname}, nickname = {self.nickname})>"


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

user1 = User(name="Marcin", fullname="Marcin Albiniak", nickname="albim")
session.add(user1)

user2 = User(name="Olga", fullname="Olga Kot", nickname="kotek")
session.add(user2)

user3 = User(name="Tomasz", fullname="Kłos", nickname="tomus")
session.add(user3)

session.commit()

print("____wszyscy użtkownicy_____")
for s in session.query(User).all():
    print(s.fullname)

nick = input("Podaj nick name użytkownika: ")
print(f"____użtkownicy o nickname: {nick}_____")
for s in session.query(User).filter(User.nickname == nick):
    print(s.fullname)



