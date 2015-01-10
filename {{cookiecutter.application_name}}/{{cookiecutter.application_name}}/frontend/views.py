from flask import (
    Blueprint,
    render_template
)

# we can get to the registry/registries configured using:
# from {{cookiecutter.application_name}} import app
# then use : app.register ... to get/put etc.

frontend = Blueprint('frontend', __name__, template_folder='templates')

@frontend.route('/')
def index():
    return render_template('index.html')
