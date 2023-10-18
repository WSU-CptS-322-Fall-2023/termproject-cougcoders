from app import db
from flask_login import current_user
from datetime import datetime
from config import Config
from app import create_app
from app.Model.models import User, ResearchPosition, Student, Faculty

app = create_app(Config)


@app.before_request
def initDB(*args, **kwargs):
    db.create_all()


# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
