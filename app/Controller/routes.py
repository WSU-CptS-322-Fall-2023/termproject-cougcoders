from flask import Blueprint, render_template, flash, redirect, url_for, request
from app import db

from flask_login import current_user, login_required
from config import Config

routes_blueprint = Blueprint("routes", __name__)
routes_blueprint.template_folder = Config.TEMPLATES_FOLDER


@routes_blueprint.route("/", methods=["GET"])
@routes_blueprint.route("/index", methods=["GET"])
def index():
    return render_template("index.html")
