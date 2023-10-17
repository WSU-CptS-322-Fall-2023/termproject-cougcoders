from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import current_user
from app.Model.models import ResearchPosition

class PositionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=64)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=1024)])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    time_commitment = StringField('Time Commitment', validators=[DataRequired()])
    research_fields = StringField('Research Fields', validators=[DataRequired()])
    languages = StringField('Programming Languages')
    additional_requirements = StringField('Additional Requirements')
    submit = SubmitField('Create')
