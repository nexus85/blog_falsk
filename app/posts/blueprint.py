# кyсок изолированной информации - blueprintd
from flask import render_template
from flask import Blueprint
posts = Blueprint('posts', __name__, template_folder='templates')  #posts это имя под которым зарегин blueprint

@posts.route('/')
def index():

    return render_template('posts/index.html')