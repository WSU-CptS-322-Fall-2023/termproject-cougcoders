from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from flask_login import current_user
from app.Model.models import ResearchPosition, ProgrammingLanguage, Field
from wtforms.widgets import ListWidget, CheckboxInput


class PositionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=64)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=1024)]
    )
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    time_commitment = StringField("Time Commitment", validators=[DataRequired()])
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
    additional_requirements = StringField("Additional Requirements")
    submit = SubmitField("Create")


class ApplicationForm(FlaskForm):
    reason = TextAreaField(
        "Reason for Applying", validators=[DataRequired(), Length(max=1024)]
    )
    refrence_name = StringField("Faculty Refrence Name", validators=[DataRequired()])
    refrence_email = StringField(
        "Faculty Refrence Email", validators=[DataRequired(), Email()]
    )
    submit = SubmitField("Apply")
