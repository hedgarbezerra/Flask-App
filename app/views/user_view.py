from flask_sqlalchemy import SQLAlchemy
from app import app, db
from flask import request, render_template, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
from app.models.user_img import UserImg
from app.models_forms.user_form import UserForm


@app.route('/create', methods=['POST'])
def create():
    request_file = request.files['img']
    file = UserImg(user_id=1, name=request_file.filename, data=request_file.read())
    db.session.add(file)
    db.session.commit()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        passwd = form.password.data
        passwd_hash = generate_password_hash(passwd)
        born_on = form.born_on.data
        name = form.name.data
        email = form.email.data
        gender = form.gender.data

        user = User(name=name, username=username, email=email, password=passwd_hash, gender=gender, born_on=born_on)

        try:
            db.session.add(user)
            db.session.commit()
            flash('Sucessfully signed up!')
            return redirect('/index')
        except:
            flash('Something went wrong, try again.')
            return render_template('users/signup.html', form=form)

    return render_template('users/signup.html', form=form)


@app.route('/ct', methods=['POST', 'GET'])
def ct():
    user = User(name='hed', username='hed', email='hed',
                password='hed', gender='M', born_on='1993-01-12')

    try:
        db.session.add(user)
        db.session.commit()
    except:
        print('erro')
