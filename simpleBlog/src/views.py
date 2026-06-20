# Import bluebrint
from flask import Blueprint,render_template
# Create bluebrint instance
views = Blueprint("views",__name__)


@views.route("/home")
@views.route("/")
def home():
    return render_template('home.html',name="ahmed")