from flask import render_template, url_for,redirect
# from flask_login import login_required
from . import main
from flask_login import current_user
from .. import db
from ..request import get_competitions


# @main.route('/')
# def index():
#
#     return render_template('index.html')
@main.route('/standings',methods=['GET','POST'])
def standings():
    matches=get_competitions()
    return render_template('standings.html',matches=matches)
