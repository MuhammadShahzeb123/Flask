from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import hashlib
from GPT_Key import key
import openai

openai.api_key = key


class RegistrationForm(FlaskForm):
        first_name = StringField("First Name", validators=[DataRequired(),Length(min=2, max=15)])
        last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2, max=15)])
        username = StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
        email = StringField("Email", validators=[DataRequired(), Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
        submit = SubmitField("Sign Up")
        remember = BooleanField('Remember Me')

class LoginForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired(), Email()])
        password = PasswordField("Password", validators=[DataRequired()])
        forget_password = BooleanField('Forgot Password?')
        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')

class ChatInput(FlaskForm):
        chat_input = TextAreaField("Input", validators=[DataRequired()], render_kw={"style": "height: 50px; max-height: 150px; resize: none; overflow-y: auto;"})
        submit = SubmitField("Send")

class DataBase:
        Engine = create_engine('sqlite:///Database.db') # It is the Instance that is used to create the database
        Base = declarative_base() # This is the Base class in which Table can be Defined
        
        class User(Base):
                __tablename__ = "users"
                id = Column(Integer, primary_key=True)
                first_name = Column(String)
                last_name = Column(String)
                username = Column(String)
                email = Column(String)
                password = Column(String)
        
        class Conversation(Base):
                __tablename__ = "conversations"
                role = Column(String, primary_key=True)
                user = Column(String)
                assistant = Column(String)
        
        Base.metadata.create_all(Engine)
        
        Session = sessionmaker(bind=Engine)
        session = Session()

        def signup(self, first_name: str, last_name:str, username: str, email: str, password: str) -> bool:
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                if User_Data_Query is not None and User_Data_Query.email == email:
                        return False
                hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                User_Data = self.User(first_name=first_name, last_name=last_name, username=username, email=email, password=hashed_password)
                self.session.add(User_Data)
                self.session.commit()
                return True

        def login(self, email: str, password: str) -> bool:
                hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                return (User_Data_Query is not None and User_Data_Query.email == email and User_Data_Query.password == hashed_password)

        def username_retriever(self, email: str) -> str:
                Username_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                return Username_Data_Query.username
class ChatGPT:
        def __init__(self) -> None:
                self.messages =  [
                        {"role": "system", "content": "Assistive Chatbot that Help people with Their Problems"}       
                ]
        
        def ask(self, Q: str) -> str:
                if Q == "clear":
                        self.messages =  [
                                {"role": "system", "content": "Help people with their Problems and explain them briefly how to solve that with examples"}       
                        ]
                else:
                        self.messages.append({"role": "user", "content": Q})
                        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=self.messages
                        )
                        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
                        return response["choices"][0]["message"]["content"]
