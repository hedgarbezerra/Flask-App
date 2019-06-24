from app import app
from flask import request, render_template, redirect, url_for


@app.route('/index', methods=['GET'])
def index():
    return render_template("general/index.html")


@app.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('index')), 301

