from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', title = '404'),404

@main.app_errorhandler(500)
def internal_error(e):
    return render_template('error/500.html', title = '500'),500