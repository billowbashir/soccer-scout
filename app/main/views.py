from flask import render_template, url_for,redirect
# from flask_login import login_required
from . import main
from flask_login import current_user
from .. import db



@main.route('/')
def index():

    return render_template('index.html')
