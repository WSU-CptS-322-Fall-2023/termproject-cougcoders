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

        db.init_app(flask_app)
        testing_client = flask_app.test_client()
    
        # Establish an application context before running the tests.
        ctx = flask_app.app_context()
        ctx.push()
    
        yield  testing_client     
        ctx.pop()

    #---------------------------------------
    #------------- Route Tests -------------

    def init_database():
        # Create the database and the database table
        pass
        # to-do iteration3

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
        pass
        # to-do iteration3

    def test_apply(request, test_client,init_database):
        pass
        # to-do iteration3

    def test_withdraw_application(request, test_client,init_database):
        pass
        # to-do iteration3
    
    def test_viewapplications(request, test_client,init_database):
        pass
        # to-do iteration3

    def test_changestatus(request, test_client,init_database):
        pass
        # to-do iteration3

    def test_editStudentProfile(request, test_client,init_database):
        pass
        # to-do iteration3
