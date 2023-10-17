from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db

from flask_login import current_user, login_required
from config import Config
from app.Model.models import ResearchPosition, Student, Faculty, User
from app.Controller.forms import PositionForm

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATES_FOLDER


@routes_blueprint.route("/", methods=["GET"])
@routes_blueprint.route("/index", methods=["GET"])
def index():
    positions = ResearchPosition.query.all()
    return render_template("index.html", positions=positions)

@routes_blueprint.route('/createposition', methods=['GET', 'POST'])
def createposition():
    form = PositionForm()
    if form.validate_on_submit():
        position = ResearchPosition(
            title=form.title.data,
            description=form.description.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            time_commitment=form.time_commitment.data,
            research_fields=form.research_fields.data,
            languages=form.languages.data,
            additional_requirements=form.additional_requirements.data
        )
        db.session.add(position)
        db.session.commit()
        flash(f"Position '{form.title.data}' created!")
        return redirect(url_for('routes.index'))
    return render_template('createposition.html', title='Create Position', form=form)
