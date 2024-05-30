from flask import render_template, Blueprint
from utils.devtools import launch  # TEST CODE

main = Blueprint('main', __name__, static_url_path='/main/static', template_folder='templates', static_folder='static')


@main.route('/')
def index():
    launch()  # TEST CODE
    return render_template('content/index.html', pagekey="Index", left_aside=True)


@main.route('/about')
def about():
    launch()  # TEST CODE
    return render_template('content/about.html', pagekey="About")
