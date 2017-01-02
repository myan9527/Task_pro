from flask import Flask,render_template
from flask_script import Manager
from flask import request
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
#     user_agent = request.headers.get('User-Agent')
    content = ""
    for k,v in request.headers:
        content += k +":"+ v +"<br>"
    return render_template("index.html") 

@app.route('/make')
def make():
    response = make_response('<h1>This response carries a cookie.</h1>')
    response.set_cookie('name','Michael Yan')
    return response

@app.route('/abort')
def red():
    abort(503)
#     return redirect('http://www.baidu.com')

@app.route('/user/<name>')
def user(name):
    return render_template('index.html',name = name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'),404
@app.errorhandler(500)
def internal_error(e):
    return render_template('error/500.html'),500

if __name__ == '__main__':
    manager.run()   