from app import db
from enum import unique
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

# from app import login


# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


studentApplicants = db.Table(
    "studentApplicants",
    db.Column("student_id", db.Integer, db.ForeignKey("user.id")),
    db.Column(
        "research_position_id", db.Integer, db.ForeignKey("research_position.id")
    ),
)

languages = db.Table(
    "languages",
    db.Column(
        "programming_language_id", db.Integer, db.ForeignKey("programming_language.id")
    ),
    db.Column(
        "research_position_id", db.Integer, db.ForeignKey("research_position.id")
    ),
)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    phone_number = db.Column(db.String(64), nullable=True)
    wsu_id = db.Column(db.String(64), nullable=True)
    user_type = db.Column(db.String(64))

    __mapper_args__ = {
        "polymorphic_identity": "User",
        "polymorphic_on": user_type,
    }

    # __table_args__ = {"extend_existing": True}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Student(User):
    __tablename__ = "student"
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)
    major = db.Column(db.String(64), nullable=True)
    gpa = db.Column(db.Float, nullable=True)
    graduation_date = db.Column(db.DateTime, nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "Student",
    }

    def __repr__(self):
        return "<ID: {}, Username: {}, Email: {}>".format(
            self.id, self.username, self.email
        )


class Faculty(User):
    __tablename__ = "faculty"
    id = db.Column(db.ForeignKey("user.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "Faculty",
    }

    def __repr__(self):
        return "<ID: {}, Username: {}, Email: {}>".format(
            self.id, self.username, self.email
        )


class ResearchPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    time_commitment = db.Column(db.String(64), nullable=False)
    research_fields = db.Column(db.String(128), nullable=False)
    languages_required = db.relationship(
        "ProgrammingLanguage",
        secondary=languages,
        backref=db.backref("research_positions", lazy="dynamic"),
    )
    additional_requirements = db.Column(db.String(1024), nullable=True)
    # faculty_id = db.Column(db.Integer, db.ForeignKey("faculty.id"))
    # students = db.relationship(
    #     "Student", secondary=studentApplicants, backref="research_positions"
    # )

    def get_students(self):
        return self.students


class ProgrammingLanguage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
