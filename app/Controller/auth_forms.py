from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo
from app.Model.models import User, Student, Faculty, Field, ProgrammingLanguage
from wtforms.widgets import ListWidget, CheckboxInput

class FacultyRegForm(FlaskForm):
    username = StringField('WSU Email', validators=[DataRequired(), Email(), Length(min=0, max=64)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=0, max=64)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=0, max=64)])
    phoneNum = StringField("Phone Number", validators=[DataRequired(), Length(min=0, max=64)])
    WSU_id = StringField("WSU Id", validators=[DataRequired(), Length(min=0, max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=128)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(min=0, max=128)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists! Please use a different username.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists! Please use a different email address.')
        
class StudentRegForm(FlaskForm):
    username = StringField('WSU Email', validators=[DataRequired(), Email(), Length(min=0, max=64)])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=0, max=64)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=0, max=64)])
    phoneNum = StringField("Phone Number", validators=[DataRequired(), Length(min=0, max=64)])
    WSU_id = StringField("WSU Id", validators=[DataRequired(), Length(min=0, max=64)])
    research_fields = QuerySelectMultipleField(
        "Research Fields",
        query_factory=lambda: Field.query.all(),
        get_label=lambda x: x.name,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    languages = QuerySelectMultipleField(
        "Languages",
        query_factory=lambda: ProgrammingLanguage.query.all(),
        get_label=lambda x: x.name,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=128)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(min=0, max=128)])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists! Please use a different username.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists! Please use a different email address.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=0, max=64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=0, max=128)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
