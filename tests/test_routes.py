import os
import pytest
from app import create_app, db
from app.Model.models import User, Student, Faculty, ResearchPosition, Application, ProgrammingLanguage, Field
from config import Config
from datetime import datetime


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
    # this is where the testing happens    
    ctx.pop()


# Creates database and user and inserts the user into database
@pytest.fixture
def init_database():

    db.create_all()
        
    test_student = Student(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
                     wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
    # test_student.set_password('1234')
    db.session.add(test_student)
    db.session.commit()

    test_faculty = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
                            phone_number='1234', wsu_id='1111', user_type="Faculty")
    # test_student.set_password('1111')
    db.session.add(test_faculty)
    db.session.commit()

    yield 

    db.drop_all()

#---------------------------------------
#------------- Route Tests -------------

# tests the '/student_register' page (GET) request response
def test_student_register_page(test_client, init_database):
    response = test_client.get('/student_register')
    assert response.status_code == 200
    assert b"Register" in response.data


# tests the '/faculty_register' page (GET) request response
def test_faculty_register_page(test_client, init_database):
    response = test_client.get('/faculty_register')
    assert response.status_code == 200
    assert b"Register" in response.data


# tests the '/student_registration' form (POST) request response
def test_student_registration(test_client, init_database):
    response = test_client.post('/student_register', 
                          data=dict(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
                                    wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student"),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(Student.username=='CB')
    assert s.first().email == 'c.b@wsu.edu'
    assert s.count() == 1
    assert b"Student Registration" in response.data   


# tests the '/faculty_registration' form (POST) request response
def test_faculty_registration(test_client, init_database):
    response = test_client.post('/faculty_register', 
                          data=dict(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
                                    phone_number='1234', wsu_id='1111', user_type="Faculty"),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(Faculty.first_name=='Sakire')
    assert s.first().wsu_id == '1111'
    assert s.count() == 1
    assert b"Faculty Registration" in response.data  


def test_invalid_login(test_client, init_database):
    pass
    

def test_student_login(request, test_client, init_database):
    pass


def test_student_logout(request, test_client, init_database):
    pass


def test_faculty_login(request, test_client,init_database):
    pass


def test_faculty_logout(request, test_client,init_database):
    pass 


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
