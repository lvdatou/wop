from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired,EqualTo,Length

class RegisterForm(FlaskForm):
    '''
        Registration Form
    '''

    username = StringField(
        label = 'USERNAME',
        validators = [DataRequired(message = 'the username cannot be blank'),Length(min = 3,
            max = 25,message = 'The username length should be between 3-25 characters!')]
    )

    password = PasswordField(
        label = 'PASSWORD',
        validators = [DataRequired(message = 'The password cannot be blank'),Length(min = 6,
            max = 25,message = 'The password length should be between 3-25 characters!')]
    )

    confirm = PasswordField(
        label = 'PASSWORD CONFIRMATION',
        validators = [EqualTo('password',message = 'The password is inconsistent')]
    )

    submit = SubmitField(label='REGIST')

class NameLoginForm(FlaskForm):
    '''
        username login form
    '''
    username = StringField(
        label='USERNAME',
        validators=[DataRequired(message='The username can not be blank')])
    password = PasswordField(
        label='PASSWORD',
        validators=[DataRequired(message='The password can not be blank')])
    remember = BooleanField(label='Remember Me')
    submit = SubmitField(label='Login')
    pass

class PostForm(FlaskForm):
    '''
        post form
    '''
    title = StringField('Article Title',[DataRequired(),Length(min=6,max=255)])
    abstract = TextAreaField('Article Abstract')
    content = TextAreaField('Article Content',[DataRequired()])
    submit = SubmitField(label = "SUBMIT")