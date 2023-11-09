from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db

from flask_login import current_user, login_required
from config import Config
from app.Model.models import (
    ResearchPosition,
    Student,
    Faculty,
    User,
    Application,
)
from app.Controller.forms import (
    PositionForm,
    ApplicationForm,
    ChangeStatusForm,
    EditStudentProfile,
)

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATES_FOLDER


@routes_blueprint.route("/", methods=["GET"])
@routes_blueprint.route("/index", methods=["GET"])
@login_required
def index():
    if current_user.user_type == "Faculty":
        positions = ResearchPosition.query.filter_by(faculty_id=current_user.id).all()
    else:
        positions = ResearchPosition.query.all()
    applications = Application.query.filter_by(student_id=current_user.id).all()
    return render_template("index.html", positions=positions, applications=applications)


@routes_blueprint.route("/createposition", methods=["GET", "POST"])
@login_required
def createposition():
    if current_user.user_type != "Faculty":
        flash("You must be a faculty member to create positions!")
        return redirect(url_for("routes.index"))
    form = PositionForm()
    if form.validate_on_submit():
        position = ResearchPosition(
            title=form.title.data,
            description=form.description.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            time_commitment=form.time_commitment.data,
            additional_requirements=form.additional_requirements.data,
            faculty_id=current_user.id,
        )
        for lang in form.languages.data:
            position.languages_required.append(lang)
        for field in form.research_fields.data:
            position.research_fields.append(field)
        db.session.add(position)
        db.session.commit()
        flash(f"Position '{form.title.data}' created!")
        return redirect(url_for("routes.index"))
    return render_template("createposition.html", title="Create Position", form=form)


@routes_blueprint.route("/apply/<positionid>", methods=["GET", "POST"])
@login_required
def apply(positionid):
    position = ResearchPosition.query.filter_by(id=positionid).first()
    if position is None:
        flash("Position does not exist!")
        return redirect(url_for("routes.index"))
    prev_app = Application.query.filter_by(
        student_id=current_user.id, research_position_id=positionid
    ).first()
    if prev_app is not None:
        flash("You have already applied to that position!")
        return redirect(url_for("routes.index"))
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(
            reason=form.reason.data,
            refrence_name=form.refrence_name.data,
            refrence_email=form.refrence_email.data,
            student_id=current_user.id,
            research_position=position,
            status="Pending",
        )
        db.session.add(application)
        db.session.commit()
        flash("Application submitted!")
        return redirect(url_for("routes.index"))
    return render_template(
        "application.html", title="Apply", form=form, position=position
    )


@routes_blueprint.route("/viewapplications/<positionid>", methods=["GET"])
@login_required
def viewapplications(positionid):
    position = ResearchPosition.query.filter_by(id=positionid).first()
    form = ChangeStatusForm()
    if position is None:
        flash("Position does not exist!")
        return redirect(url_for("routes.index"))
    if current_user.user_type != "Faculty":
        flash("You must be a faculty member to view applications!")
        return redirect(url_for("routes.index"))
    applications = Application.query.filter_by(research_position_id=positionid).all()
    return render_template(
        "viewapplications.html",
        title="View Applications",
        applications=applications,
        position=position,
        form=form,
    )


@routes_blueprint.route("/changestatus/<applicationid>", methods=["GET", "POST"])
@login_required
def changestatus(applicationid):
    form = ChangeStatusForm()
    application = Application.query.filter_by(id=applicationid).first()
    if form.validate_on_submit:
        application.status = form.status.data
        db.session.commit()
    return render_template(
        "viewapplications.html",
        title="View Applications",
        form=form,
        position=Application.query.filter_by(id=applicationid)
        .first()
        .research_position,
        applications=Application.query.filter_by(
            research_position_id=Application.query.filter_by(id=applicationid)
            .first()
            .research_position.id
        ).all(),
    )


@routes_blueprint.route("/editStudentProfile", methods=["GET", "POST"])
@login_required
def editStudentProfile():
    form = EditStudentProfile()
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    form.major.data = current_user.major
    form.gpa.data = current_user.gpa
    form.graduation_date.data = current_user.graduation_date
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        current_user.major = form.major.data
        current_user.gpa = form.gpa.data
        current_user.graduation_date = form.graduation_date.data
        db.session.commit()
        flash("Changes saved!")
        return redirect(url_for("routes.index"))
    return render_template("editStudentProfile.html", title="Edit Profile", form=form)
