from flask import render_template, Blueprint

main = Blueprint('main', __name__, static_url_path='/main/static', template_folder='templates', static_folder='static')


@main.route('/')
def index():
    return render_template('content/index.html', pagekey="Index")


@main.route('/about')
def about():
    return render_template('content/about.html', pagekey="About")
