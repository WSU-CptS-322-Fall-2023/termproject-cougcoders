# add students and faculty and create a post

from app import create_app, db

app = create_app()
app.app_context().push()
db.create_all()
from app.Model.models import Student, Faculty, ResearchPosition

s = Student(username="test2", email="test2")
db.session.add(s)

f = Faculty(username="test1", email="test1")

db.session.add(f)

r = ResearchPosition(
    title="test",
    description="test",
    time_commitment="test",
    additional_requirements="test",
)

db.session.add(r)
db.session.commit()
