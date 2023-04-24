import os
import openai
import GPT_Key
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

