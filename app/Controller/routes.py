from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db

from flask_login import current_user, login_required
from config import Config
from app.Model.models import ResearchPosition, Student, Faculty, User, Application
from app.Controller.forms import PositionForm, ApplicationForm

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATES_FOLDER


@routes_blueprint.route("/", methods=["GET"])
@routes_blueprint.route("/index", methods=["GET"])
def index():
    positions = ResearchPosition.query.all()
    return render_template("index.html", positions=positions)


@routes_blueprint.route("/createposition", methods=["GET", "POST"])
def createposition():
    form = PositionForm()
    if form.validate_on_submit():
        position = ResearchPosition(
            title=form.title.data,
            description=form.description.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            time_commitment=form.time_commitment.data,
            additional_requirements=form.additional_requirements.data,
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
def apply(positionid):
    position = ResearchPosition.query.filter_by(id=positionid).first()
    if position is None:
        flash("Position does not exist!")
        return redirect(url_for("routes.index"))
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(
            reason=form.reason.data,
            refrence_name=form.refrence_name.data,
            refrence_email=form.refrence_email.data,
            status="Pending",
            # student=current_user,
            research_position=position,
        )
        db.session.add(application)
        db.session.commit()
        flash("Application submitted!")
        return redirect(url_for("routes.index"))
    return render_template(
        "application.html", title="Apply", form=form, position=position
    )
