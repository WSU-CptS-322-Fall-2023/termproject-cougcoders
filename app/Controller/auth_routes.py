from flask import Blueprint, render_template, flash, redirect, url_for
from app import db
from flask_login import login_user, current_user, logout_user, login_required
from config import Config

auth_blueprint = Blueprint("auth", __name__)
auth_blueprint.template_folder = Config.TEMPLATES_FOLDER
