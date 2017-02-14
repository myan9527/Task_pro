from . import main
from flask import render_template, request, abort, make_response

@main.route('/', methods = ['GET'])
def index():
    return render_template("index.html", title='Index')