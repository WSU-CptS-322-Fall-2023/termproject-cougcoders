from flask import Blueprint, render_template, flash, redirect, url_for
from app import db
from flask_login import login_user, current_user, logout_user, login_required
from config import Config
from app.Model.models import User, Student, Faculty
from app.Controller.auth_forms import FacultyRegForm, StudentRegForm, LoginForm


auth_blueprint = Blueprint("auth", __name__)
auth_blueprint.template_folder = Config.TEMPLATES_FOLDER


@auth_blueprint.route('/faculty_register', methods=['GET', 'POST'])
def faculty_registration():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index')) # need to config faculty index page
    rform = FacultyRegForm()
    if rform.validate_on_submit():
        faculty = Faculty(username=rform.username.data,
                          first_name=rform.firstname.data,
                          last_name=rform.lastname.data,
                          phone_number=rform.phoneNum.data,
                          wsu_id=rform.WSU_id.data,
                          user_type="Faculty") 
        faculty.set_password(rform.password.data)
        db.session.add(faculty)
        db.session.commit()
        flash('you are now a registered Faculty Member!')
        return redirect(url_for('routes.index')) #need to route to faculty_index when we create seperate user index pages
    return render_template('faculty_registration.html', form=rform) # need to route to sperate registration html


@auth_blueprint.route('/student_register', methods=['GET', 'POST'])
def student_registration():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index')) # need to create student index page
    sform = StudentRegForm()
    if sform.validate_on_submit():
        student = Student(username=sform.username.data,
                          first_name=sform.firstname.data,
                          last_name=sform.lastname.data,
                          phone_number=sform.phoneNum.data,
                          wsu_id=sform.WSU_id.data,
                          user_type="Student") 
        student.set_password(sform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('you are now a registered student member!')
        return redirect(url_for('routes.index')) # need to route to student index page
    return render_template('student_registration.html', title='Registration', form=sform) # need to route to sperate registration html


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.user_type=="Student":
            return redirect(url_for('routes.index')) #needs to be redirected to student_index
        else:
            return redirect(url_for('routes.index')) #needs to be redirected to faculty_index
    lform = LoginForm()
    if lform.validate_on_submit():
        user = User.query_filter_by(username = lform.username.data).first()
        if(User is None) or (user.check_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember = lform.remember_me.data)
        if current_user.user_type == "Student":
            return redirect(url_for('routes.index')) #needs to be redirected to student_index
        else:
            return redirect(url_for('routes.index')) #needs to be redirected to faculty_index
    return render_template('login.html', title = 'Sign In', form=lform)


@auth_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))