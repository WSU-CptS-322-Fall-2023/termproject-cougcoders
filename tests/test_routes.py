import os
import pytest
from app import create_app, db
from app.Model.models import User, Student, Faculty, ResearchPosition, Application, ProgrammingLanguage, Field
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True

@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield  testing_client
    # this is where the testing happens!     
    ctx.pop()

# helper function to create users
def new_user(uname, uemail,pswd):
    user = User(username=uname, email=uemail)
    user.set_password(pswd)
    return user

# Creates database and user and inserts the user into database
@pytest.fixture
def init_database():
    
    db.create_all()
        
    test_user = new_user(uname='Cb', uemail='c.b@wsu.edu',pswd='1234')
    
    db.session.add(test_user)
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

#---------------------------------------
#------------- Route Tests -------------

def test_register_page(test_client):
    pass
    # to-do iteration3

def test_student_registration(test_client,init_database):
    pass
    # to-do iteration3

def test_faculty_registration(test_client,init_database):
    pass
    # to-do iteration3

def test_invalid_login(test_client,init_database):
    pass
    # to-do iteration3

def test_student_loginlogout(request, test_client,init_database):
    pass
    # to-do iteration3

def test_faculty_loginlogout(request, test_client,init_database):
    pass
    # to-do iteration3

def test_createposition(request, test_client,init_database):
    pass
    # to-do iteration3

def test_deleteposition(request, test_client,init_database):
    # f_test = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
    #                 phone_number='1234', wsu_id='1111', user_type="Faculty")
    # db.session.add(f_test)
    # db.session.commit()
    pass

def test_apply(request, test_client,init_database):
    pass
    # to-do iteration3

def test_withdraw_application(request, test_client,init_database):
    # s_test = Student(username='MB', email='M.B@wsu.edu', first_name='Matthew', last_name='Bruggeman', phone_number='1234',
    #                 wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
    # db.session.add(s_test)
    # db.session.commit()

    # test_delete = Application(reason='testing application', refrence_name='Sakire', refrence_email='S.AA@wsu.edu',
    #                        status='Pending', student_id=User.query.filter_by().first().id)
    # db.session.add(test_delete)
    # db.session.commit()
    # # withdraw_application(User.query.filter_by(id=1).first())
    # self.assertEqual(len(Application.query.all()), 1)
    # db.session.delete(test_delete)
    # db.session.commit()
    # self.assertEqual(Application.query.all(), [])
    pass

def test_viewapplications(request, test_client,init_database):
    pass
    # to-do iteration3

def test_changestatus(request, test_client,init_database):
    pass
    # to-do iteration3

def test_editStudentProfile(request, test_client,init_database):
    pass
