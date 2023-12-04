from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
    PasswordField,
    SelectField,
    BooleanField,
    SelectMultipleField,
)
from wtforms.fields.html5 import DateField, DecimalField
from wtforms.validators import ValidationError, Length, DataRequired, Email, EqualTo, NumberRange
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from flask_login import current_user
from app.Model.models import ResearchPosition, ProgrammingLanguage, Field, User
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


class ChangeStatusForm(FlaskForm):
    status = SelectField(
        "Status",
        choices=[("Pending"), ("Hired"), ("Approved for Interview"), ("Not Hired")],
    )
    submit = SubmitField("Change Status")


class EditStudentProfile(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=64)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=64)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    graduation_date = DateField("Graduation Date", validators=[DataRequired()])
    major = StringField("Major", validators=[DataRequired()])
    gpa = DecimalField("GPA", places=2, validators=[DataRequired(), NumberRange(min=0.0, max=4.0)])
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
    submit = SubmitField("Save Changes")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError(
                    "Email already exists! Please use a different email address."
                )


class FilterPositions(FlaskForm):
    research_fields = QuerySelectMultipleField(
        "Research Fields",
        query_factory=lambda: Field.query.all(),
        get_label=lambda x: x.name,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    programming_languages = QuerySelectMultipleField(
        "Languages",
        query_factory=lambda: ProgrammingLanguage.query.all(),
        get_label=lambda x: x.name,
        widget=ListWidget(prefix_label=False),
        option_widget=CheckboxInput(),
    )
    recommended = BooleanField("Recommended")
    submit = SubmitField("Filter")


class EditFacultyProfile(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=64)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=64)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Save Changes")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError(
                    "Email already exists! Please use a different email address."
                )
