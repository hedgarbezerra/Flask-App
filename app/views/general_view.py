from app import app
from flask import render_template, redirect, url_for
from .user_view import current_user, is_logged

@app.route('/index', methods=['GET'])
def index():
    if is_logged():
        user = current_user()
    else:
        user = None
    return render_template("general/index.html", user=user)


@app.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('index')), 301

