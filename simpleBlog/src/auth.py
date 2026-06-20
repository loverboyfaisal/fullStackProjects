# Import bluebrint
from flask import Blueprint,render_template
# Create bluebrint instance
auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    return render_template('login.html')


@auth.route('/sign_up')
def sign_up():
    return "sign up"


@auth.route('/logout')
def logout():
    return "logout"