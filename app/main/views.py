from . import main
from flask import render_template, request, abort, make_response

@main.route('/', methods = ['GET'])
def index():
    return render_template("index.html", title='Index')

@main.route('/login', methods = ['GET'])
def login():
    return render_template("login.html", title='Login')

@main.route('/login', methods = ['POST'])
def pro_login():
    # check user exist or not

    # add to db

    # add to session

    # load basic data

    # return success
    return render_template("dashboard.html", title = '')
@main.route('/abort')
def red():
    abort(503)
#     return redirect('http://www.baidu.com')

@main.route('/user/<name>')
def user(name):
    return render_template('index.html',name = name)