import os
import pytest
from flask import Blueprint, render_template, flash, redirect, url_for
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
        
    test_student = Student(username='CB', email='c.b@wsu.edu', password_hash='1234', first_name='Chance', last_name='Bradford', phone_number='1234',
                     wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
    # test_student.set_password('1234')
    db.session.add(test_student)
    db.session.commit()

    test_faculty = Faculty(username='SAA', email='S.AA@wsu.edu', password_hash='1111', first_name='Sakire', last_name='Arslan Ay',
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
                          data=dict(username='c.b@wsu.edu', firstname='c', lastname='b', phoneNum='1234', WSU_id='1234', gpa='4.0', major='Cpts',
                                    graduation_date='2023-12-06', password='1234', password2='1234'),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(Student.username=='c.b@wsu.edu')
    assert s.first().first_name == 'c'
    assert s.count() == 1
    #check contents of rendered html page
    # assert b"You are now a registered student member!" in response.data 
    # assert b'Please log in to access this page.' in response.data


# tests the '/faculty_registration' form (POST) request response
def test_faculty_registration(request, test_client, init_database):
    response = test_client.post('/faculty_register', 
                          data=dict(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
                                    phone_number='1234', wsu_id='1111', user_type="Faculty"),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(User).filter(Faculty.first_name=='Sakire')
    assert s.first().wsu_id == '1111'
    assert s.count() == 1
    assert b"Faculty Registration" in response.data  #check contents of rendered html page


# tests the '/login' form (POST) with wrong submitted credentials THEN check that the response is valid and login is refused 
def test_invalid_login(test_client, init_database):
    response = test_client.post('/login', 
                          data=dict(username='CB', password='123',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Successful Student User Login!" not in response.data 
    # assert b"Invalid username or password" in response.data 


# tests the student '/login' and '/logout' form (POST) with correct credentials THEN check that the response is valid and login is accepted
def test_student_login_logout(request, test_client, init_database):
    response = test_client.post('/login', 
                          data=dict(username='Cb', password='1234',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Student App" in response.data  # You are now a registered student member!

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"Please log in to access this page." in response.data


# tests the faculty '/login' and '/logout' form (POST) with correct credentials THEN check that the response is valid and login is accepted
def test_faculty_login_logout(request, test_client,init_database):
    response = test_client.post('/login', 
                          data=dict(username='Sakire', password='1111',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Student App" in response.data  

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"Please log in to access this page." in response.data


# tests the '/createposition' page is requested (GET)  AND /PositionForm' form is submitted (POST)
# checks that response is valid and the class is successfully created in the database
def test_createposition(test_client,init_database):
    response = test_client.post('/login', 
                          data=dict(username='Sakire', password='1111',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Student App" in response.data 

    #test the "PositionForm" form 
    response = test_client.get('/createposition')
    # assert response.status_code == 200  
    # assert b"Create new Research Position" in response.data





# tests the '/deleteposition' page form is submitted (POST)
# checks that response is valid and the class is successfully deleted in the database
def test_deleteposition(test_client,init_database):
    # f_test = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
    #                 phone_number='1234', wsu_id='1111', user_type="Faculty")
    # db.session.add(f_test)
    # db.session.commit()
    pass

def test_apply(request, test_client,init_database):
    pass
    

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
   

def test_changestatus(request, test_client,init_database):
    pass
    

def test_editStudentProfile(request, test_client,init_database):
    pass

def test_editFacultyProfile(request, test_client,init_database):
    pass