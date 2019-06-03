from app import app, db
from flask import request, render_template
from app.models.user_img import UserImg


@app.route('/x')
def hello_world():
    return 'Hello!'


@app.route('/create', methods=['POST'])
def create():
    request_file = request.files['img']
    file = UserImg(user_id=1, name=request_file.filename, data=request_file.read())
    db.session.add(file)
    db.session.commit()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('users/signup.html')

    elif request.method == 'POST':
        pass

    else:
        return render_template('errors.html')
