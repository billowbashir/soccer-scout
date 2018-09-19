from flask import render_template, url_for,redirect
from flask import Flask,render_template, url_for,redirect, abort, request
from . import main
from flask_login import current_user, login_required
from .. import db , photos
from ..models import User
from .forms import UpdateProfile
from ..request import get_competitions,get_fixtures

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort (404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/contact')
def contact():

    return render_template('contact.html')

@main.route('/standings',methods=['GET','POST'])
def standings():
    matches=get_competitions()
    return render_template('standings.html',matches=matches)

@main.route('/fixtures',methods=['GET','POST'])
def fixtures():
    fixtures=get_fixtures()
    return render_template('fixtures.html',fixtures=fixtures)
