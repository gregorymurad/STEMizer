from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from STEMizer.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        #check if there is already a username with the same username, if exists
        # then throw a validation error from wtforms, if not, this if does not hold
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self,email):
        user = User.query.filter_by(username=email.data).first()
        #check if there is already a username with the same username, if exists
        # then throw a validation error from wtforms, if not, this if does not hold
        if user:
            raise ValidationError('There is an account with that email already. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')