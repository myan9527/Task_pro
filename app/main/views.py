from . import main
from flask import render_template, request, abort, make_response

@main.route('/')
def index():
#     user_agent = request.headers.get('User-Agent')
    content = ""
    for k, v in request.headers:
        content += k +":"+ v +"<br>"
    return render_template("index.html", title='Index')

@main.route('/make')
def make():
    response = make_response('<h1>This response carries a cookie.</h1>')
    response.set_cookie('name', 'Michael Yan')
    return response

@main.route('/abort')
def red():
    abort(503)
#     return redirect('http://www.baidu.com')

@main.route('/user/<name>')
def user(name):
    return render_template('index.html',name = name)