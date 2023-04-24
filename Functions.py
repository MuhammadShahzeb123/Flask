import os
import openai
import GPT_Key
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

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

openai.api_key = GPT_Key.key
class ChatGPT: 
        def __init__(self, role) -> None:
                self.Messages =  [
                        {"role": "system", "content": role}       
                ]
                

        def ask(self, Q: str) -> str:
                self.Messages.append({"role": "user", "content": Q})
                
                response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.Messages
                ) 
                self.Messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]}) # type: ignore
                return response["choices"][0]["message"]["content"] # type: ignore
        
        
        def Saving_Messages(self) -> None:
                title = "Please Provide a 3 Worded Title for this conversation. NOTE: Only 3 Words and should described what we talked about."
                Logs = self.ask(title)
                with open(f"{Logs}.log", "a") as log:
                        for Message in self.Messages:
                                log.write(str(f"{Message}\n"))
                                log.write("\n\n\n")
                                log.close()
                os.system("move *.log /logs")

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

        def signup(self, username, email, password) -> None:
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                if User_Data_Query.email == email:
                        return "Already signed up"
                else:
                        User_Data = self.User(username=username, email=email, password=password)
                        self.session.add(User_Data)
                        self.session.commit()
                        return "Signed up"

                
        def login(self, email, password) -> bool:
                User_Data_Query = self.session.query(self.User).filter_by(email=email).first()
                if User_Data_Query.email == email and User_Data_Query.password == password:
                        return True
                else:
                        return False