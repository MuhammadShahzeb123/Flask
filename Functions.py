from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import hashlib


class RegistrationForm(FlaskForm):
        username = StringField("Username", validators=[DataRequired(),
                                                        Length(min=2, max=29)])
        email = StringField("Email", validators=[DataRequired(),
                                                Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),
                                                                        EqualTo(password)])
        submit = SubmitField("Sign Up")
        remember = BooleanField('Remember Me')

class LoginForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired(), Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        forget_password = BooleanField('Forgot Password?')
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')

class DataBase:
        Engine = create_engine('sqlite:///Database.db') # It is the Instance that is used to create the database
        Base = declarative_base() # This is the Base class in which Table can be Defined
        
        class User(Base):
                __tablename__ = "Database"
                id = Column(Integer, primary_key=True)
                username = Column(String)
                email = Column(String)
                password = Column(String)
        
        Base.metadata.create_all(Engine)
        
        Session = sessionmaker(bind=Engine)
        session = Session()

        def signup(self, username: str, email: str, password: str) -> bool:
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                if User_Data_Query is not None and User_Data_Query.email == email:
                        return False
                else:
                        password = hashlib.sha256(password.encode("UTF-8")).hexdigest()
                        User_Data = self.User(username=username, email=email, password=password)
                        self.session.add(User_Data)
                        self.session.commit()
                        return True

        def login(self, email: str, password: str) -> bool:
                hashed_password = hashlib.sha256(password.encode("UTF-8")).hexdigest()
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first() 
                if User_Data_Query is not None and User_Data_Query.email == email and User_Data_Query.password == hashed_password:
                        return True
                else:
                        return False

