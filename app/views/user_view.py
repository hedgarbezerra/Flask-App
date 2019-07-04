import os
from werkzeug.utils import secure_filename
from app import app, db
from flask import request, render_template, redirect, flash, make_response, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.models.user_img import UserImg
from app.models_forms.password_change_form import passwordForm
from app.models_forms.update_user_form import update_userForm
from app.models_forms.user_form import userForm
from app.models_forms.img_form import Profile_imgForm
from app.models_forms.login_form import loginForm
import datetime


@app.route('/photo', methods=['GET', 'POST'])
def create():
    form = Profile_imgForm()

    if request.method == 'POST' and form.validate_on_submit():

        user = User.query.get(1)
        data = form.photo.data
        filename = secure_filename(data.filename)
        filename = user.username+'_profile_img'+filename[-4:]
        path = os.path.join(app.root_path, 'photos', filename)

        try:
            data.save(path)
            print('ok')
        except:
            print('Já existe')

        img = UserImg(user_id=1, path=path, user=user)

        try:
            db.session.add(img)
            db.session.commit()
            print("succs")
            return redirect('/index')
        except:
            print('deu ruim')
            return render_template('users/profile_img.html', form=form)

    return render_template('users/profile_img.html', form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if is_logged():
        return redirect('/index')

    form = userForm()

    if form.validate_on_submit():
        username = form.username.data
        passwd = generate_password_hash(form.password.data)
        born_on = form.born_on.data
        name = form.name.data
        email = form.email.data
        gender = form.gender.data

        user = User(name=name, username=username, email=email, password=passwd, gender=gender, born_on=born_on)

        try:
            db.session.add(user)
            db.session.commit()
            flash('Sucessfully signed up!')
            return redirect('/login')
        except:
            flash('Something went wrong, please try again.')
            return render_template('users/signup.html', form=form)

    return render_template('users/signup.html', form=form)


@app.route('/settings', methods=['GET', 'POST'])
def update():
    if is_logged():
        user = current_user()
        update_form = update_userForm()

        if update_form.validate_on_submit():
            name = update_form.name.data
            gender = update_form.gender.data
            email = update_form.email.data
            born_on = update_form.born_on.data

            try:
                user.name = name
                user.email = email
                user.gender = gender
                user.born_on = born_on
                db.session.commit()
                flash('User updated successfully.')
            except:
                flash('Oops, something went wrong.')

        return render_template('users/settings.html', user=user, update_form=update_form)

    return redirect('/login')


@app.route('/password', methods=['GET', 'POST'])
def password():
    if is_logged():
        user = current_user()
        passwd_form = passwordForm()

        if passwd_form.validate_on_submit():
            passwd = generate_password_hash(passwd_form.password.data)
            try:
                user.password = passwd
                db.session.commit()
                flash('Password updated')
            except:
                flash('Oops, something went wrong.')

        return render_template('users/password_change.html', user=user, passwd_form=passwd_form)

    return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if is_logged():
        return redirect('/index')

    form = loginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = username_exists(username)

        if not user:
            flash('Username is not registered.')
            return render_template('users/login.html', form=form)

        if user and not check_password_hash(user.password, password):
            flash('Password is invalid.')
            return render_template('users/login.html', form=form)

        if user and check_password_hash(user.password, password):
            flash('Sucessfully logged in!')
            response = make_response(redirect('/index'))

            if remember:
                response.set_cookie('username', username,
                                    expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                session['username'] = username

            return response

    return render_template('users/login.html', form=form)


@app.route('/logout', methods=['GET', 'DELETE'])
def logout():
    response = make_response(redirect('/login'))
    session.pop('username', None)
    response.delete_cookie('username')

    flash('Successfully logged out')
    return response


def username_exists(username):
    try:
        return User.query.filter(User.username == username).one()
    except:
        return None


def email_exists(email):
    try:
        return User.query.filter(User.email == email).one()
    except:
        return None


def current_user():
    if 'username' in session:
        return username_exists(session['username'])
    if request.cookies.get('username'):
        return username_exists(request.cookies.get('username'))


def is_logged():
    if 'username' in session:
        return True
    if request.cookies.get('username'):
        return True
    return False