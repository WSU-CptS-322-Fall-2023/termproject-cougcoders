# add students and faculty and create a post
from datetime import datetime, timedelta
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
    title="Position Title",
    description="This is the research position description!",
    time_commitment="24 hours per day",
    start_date = datetime.now() - timedelta(days=5),
    end_date = datetime.now() + timedelta(days=2),
    research_fields = "Some research fields"
)

db.session.add(r)
db.session.commit()

r2 = ResearchPosition(
    title="Research 2",
    description="This is another research position description!",
    time_commitment="25 hours per day",
    start_date = datetime.now() - timedelta(days=554),
    end_date = datetime.now() + timedelta(days=28),
    research_fields = "Cybersecurity, DevOps, Cloud",
    languages = "Rust, Haskell, TypeScript"
)

db.session.add(r2)
db.session.commit()
