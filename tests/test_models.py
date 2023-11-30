import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import User, Student, Faculty, ResearchPosition, Application, ProgrammingLanguage, Field
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+basedir


class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    #---------------------------------------
    #------------- Model Tests -------------
    
    def test_User_student(self):
        # s = Student(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
        #              wsu_id='1234', major='Cpts', gpa='4.0', graduation_date='5/10/2025', user_type="Student")
        pass

    def test_User_faculty(self):
        # f = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay', phone_number='1234',
        #             wsu_id='1234', user_type="Faculty")
        pass

    # tests for correct password hashing of User class model
    def test_password_hashing(self):
        s = User(username='AE', email='A.E@wsu.edu', first_name='Andrew', last_name='Edson',
                  phone_number='1234', wsu_id='1234')
        s.set_password('testpswrd')
        self.assertFalse(s.check_password('1234'))
        self.assertTrue(s.check_password('testpswrd'))

    def test_enroll_student(self):
        pass
        # to-do iteration3

    def test_enroll_faculty(self):
        pass
        # to-do iteration3

    def test_unenroll_student(self):
        pass
        # to-do iteration3

    def test_unenroll_faculty(self):
        pass
        # to-do iteration3

    def test_ResearchPosition1(self):
        pass
        # to-do iteration3

    def test_ResearchPosition2(self):
        pass
        # to-do iteration3

    def test_Application1(self):
        pass
        # to-do iteration3
    
    def test_Application2(self):
        pass
        # to-do iteration3

    def test_ProgrammingLanguage(self):
        pass
        # to-do iteration3

    def test_Field(self):
        pass
        # to-do iteration3


if __name__ == '__main__':
    unittest.main(verbosity=2)