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
        pass
        # to-do iteration3

    def test_User_faculty(self):
        pass
        # to-do iteration3

    def test_password_hashing(self):
        pass
        # to-do iteration3

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