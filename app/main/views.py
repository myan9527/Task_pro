from . import main
from flask import render_template, url_for, redirect
from flask_login import current_user

@main.route('/', methods = ['GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
    return render_template("index.html", title='Index')