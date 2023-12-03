import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime
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
    
    # tests for succesful student user insertion into sql database
    def test_User_student(self):
        test_student = Student(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
                     wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
        db.session.add(test_student)
        db.session.commit()
        self.assertEqual(User.query.filter_by(id=1).first().id , 1) 
        self.assertTrue(len(User.query.all()) == 1)

    # tests for succesful faculty user insertion into sql database
    def test_User_faculty(self):
        test_faculty = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
                            phone_number='1234', wsu_id='1111', user_type="Faculty")
        db.session.add(test_faculty)
        db.session.commit()
        self.assertEqual(User.query.filter_by(id=1).first().first_name , 'Sakire') 
        self.assertTrue(User.query.all() != None)    

    # tests for succesful faculty and student user insertions into sql database
    def test_student_faculty(self):
        test_faculty = Faculty(username='SAA', email='S.AA@wsu.edu', first_name='Sakire', last_name='Arslan Ay',
                            phone_number='1234', wsu_id='1111', user_type="Faculty")
        db.session.add(test_faculty)
        db.session.commit()
        test_student = Student(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
                            wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
        db.session.add(test_student)
        db.session.commit()
        self.assertEqual(User.query.filter_by(id=1).first().username , 'SAA') 
        self.assertEqual(User.query.filter_by(id=2).first().user_type , 'Student') 
        self.assertTrue(len(User.query.all()) == 2)  

    # tests for correct password hashing of User class model
    def test_password_hashing(self):
        s = User(username='AE', email='A.E@wsu.edu', first_name='Andrew', last_name='Edson',
                  phone_number='1234', wsu_id='1234')
        s.set_password('testpswrd')
        self.assertFalse(s.check_password('1234'))
        self.assertTrue(s.check_password('testpswrd'))

    # tests for successful insertion of Research Position into sql database
    def test_ResearchPosition1(self):
        test_position = ResearchPosition(
            title='Research Position 1',
            description='Test Research Position',
            start_date=datetime.utcnow(),
            end_date=datetime.utcnow(),
            time_commitment='1hr/week',
            additional_requirements=None,
            faculty_id=1,
        )
        db.session.add(test_position)
        db.session.commit()
        self.assertEqual(ResearchPosition.query.filter_by(id=1).first().title, 'Research Position 1')
        self.assertTrue(ResearchPosition.query.all() != None)

    # tests for successful insertion of Research Position with language and field properties into database
    def test_ResearchPosition2(self):
        test_position = ResearchPosition(
            title='Research Position 2',
            description='Test Research Position',
            start_date=datetime.utcnow(),
            end_date=datetime.utcnow(),
            time_commitment='1hr/week',
            additional_requirements=None,
            faculty_id=1,
        )

        langauges = ["C++", "Python", "Java", "C", "Binary"]
        for lang in langauges:
            if ProgrammingLanguage.query.filter_by(name=lang).first() is None:
                db.session.add(ProgrammingLanguage(name=lang))
        fields = ["Cybersecurity", "Artificial Intelligence", "Cloud", "Machine Learning"]
        for field in fields:
            if Field.query.filter_by(name=field).first() is None:
                db.session.add(Field(name=field))
        db.session.add(test_position)
        db.session.commit()

        test_position.languages_required.append(ProgrammingLanguage.query.first())
        test_position.research_fields.append(Field.query.first())

        db.session.commit()
        self.assertTrue(ProgrammingLanguage.query.first() in ResearchPosition.query.filter_by(id=1).first().languages_required)
        self.assertTrue(Field.query.first() in ResearchPosition.query.filter_by(id=1).first().research_fields)

    # tests for successful insertion of application into sql database
    def test_Application1(self):
        test_student = Student(username='CB', email='c.b@wsu.edu', first_name='Chance', last_name='Bradford', phone_number='1234',
                        wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
        db.session.add(test_student)
        db.session.commit()
        test_app = Application(reason='for money', refrence_name='Sakire', refrence_email='S.AA@wsu.edu',
                               status='Pending', student_id=User.query.filter_by().first().id)
        db.session.add(test_app)
        db.session.commit()
        self.assertEqual(Application.query.filter_by(id=1).first().student_id, 1)
        self.assertEqual(Application.query.filter_by(id=1).first().reason, 'for money')
        self.assertTrue(len(Application.query.all()), 1)
    
    # tests for successful insertion of two applications for one user into sql database (many-to-one)
    def test_Application2(self):
        test_student = Student(username='AE', email='A.E@wsu.edu', first_name='Andrew', last_name='Edson', phone_number='1234', 
                         wsu_id='1234', major='Cpts', gpa='4.0', graduation_date=datetime.utcnow(), user_type="Student")
        db.session.add(test_student)
        db.session.commit()
        test_app1 = Application(reason='seems interesting', refrence_name='Andy Ofallon', refrence_email='A.O@wsu.edu',
                               status='Pending', student_id=User.query.filter_by().first().id)
        db.session.add(test_app1)
        db.session.commit()
        test_app2 = Application(reason='testing application', refrence_name='Sakire', refrence_email='S.AA@wsu.edu',
                               status='Pending', student_id=User.query.filter_by().first().id)
        db.session.add(test_app2)
        db.session.commit()
        self.assertEqual(Application.query.filter_by(id=1).first().student_id, 1)
        self.assertEqual(Application.query.filter_by(id=1).first().student_id, Application.query.filter_by(id=2).first().student_id)
        self.assertTrue(len(Application.query.all()), 2)

    # tests for successful insertion of Programming Language list into sql database
    def test_ProgrammingLanguage(self):
        test_languages = ["C++", "Python", "Java", "C", "Binary"]
        for language in test_languages:
            db.session.add(ProgrammingLanguage(name=language))
        db.session.commit()
        self.assertEqual(ProgrammingLanguage.query.first().name, "C++")
        self.assertTrue("Java" in x.name for x in ProgrammingLanguage.query.all())

    # tests for successful insertion of Cpts Field list into sql database
    def test_Field(self):
        test_fields = ["Cybersecurity", "Artificial Intelligence", "Cloud", "Machine Learning"]
        for field in test_fields:
            db.session.add(Field(name=field))
        db.session.commit()
        self.assertEqual(Field.query.first().name, "Cybersecurity")
        self.assertTrue("Cloud" in x.name for x in Field.query.all())


if __name__ == '__main__':
    unittest.main(verbosity=2)