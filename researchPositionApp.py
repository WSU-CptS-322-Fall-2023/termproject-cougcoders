from app import db
from flask_login import current_user
from datetime import datetime
from config import Config
from app import create_app
from app.Model.models import (
    User,
    ResearchPosition,
    Student,
    Faculty,
    ProgrammingLanguage,
    Field,
)

app = create_app(Config)


@app.before_request
def initDB(*args, **kwargs):
    db.create_all()
    langauges = ["C++", "Python", "Java", "C", "Binary"]
    for lang in langauges:
        if ProgrammingLanguage.query.filter_by(name=lang).first() is None:
            db.session.add(ProgrammingLanguage(name=lang))
    fields = ["Cybersecurity", "Artificial Intelligence", "Cloud", "Machine Learning"]
    for field in fields:
        if Field.query.filter_by(name=field).first() is None:
            db.session.add(Field(name=field))
    db.session.commit()


# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
