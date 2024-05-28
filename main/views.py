from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('content/index.html', pagekey="Index")


@main.route('/about')
def about():
    return render_template('content/about.html', pagekey="About")
