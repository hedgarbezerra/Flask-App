from app import app
from flask import request, render_template


@app.route('/', methods=['GET'])
def index():
    return render_template("general/index.html")
