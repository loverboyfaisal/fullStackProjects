# Import bluebrint
from flask import Blueprint,render_template,request
from flask_login import login_required,current_user
# Create bluebrint instance
views = Blueprint("views",__name__)


@views.route("/home")
@views.route("/")
@login_required
def home():
    from src.models import fetch_post
    posts = fetch_post()
    return render_template('home.html',posts=posts)

# @views.route('/fetchposts')
# def fetchposts():
#     from src.models import fetch_post
#     posts = fetch_post()
#     return posts


@views.route('/createpost',methods=["GET","POST"])
# uncomment it after finish
# @login_required
def create_post():
    if request.method == "GET":
        return render_template('createpost.html')
    if request.method == "POST":
        post_content = request.values.get("user_input_post_content")
        from src.models import create_post
        create_post(current_user.id,post_content)
    return render_template('createpost.html')

