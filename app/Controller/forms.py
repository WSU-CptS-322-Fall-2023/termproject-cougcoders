from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user
