# Import bluebrint
from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from src.models import User,create_user
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_user,logout_user,current_user,login_required
# Create bluebrint instance
auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        usr_input_email = request.values.get("usr_input_email")
        usr_input_password = request.values.get("usr_input_password")
        user_exist = User.get_by_email(usr_input_email)
        if user_exist:
            password_hash = user_exist.user_password
            if check_password_hash(password_hash, usr_input_password):

                login_user(user_exist,remember=True)
                return redirect(url_for("views.home"))
            else:
                return render_template('login.html',msg="Incorrect password")
        else:
            return render_template('login.html',msg="user is not exist")




@auth.route('/sign_up',methods=["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        usr_input_email = request.values.get("usr_input_email")
        usr_input_username = request.values.get("usr_input_username")
        usr_input_password = request.values.get("usr_input_password")
        usr_input_confirm_password = request.values.get("usr_input_confirm_password")
        if usr_input_password != usr_input_confirm_password:
            return render_template('signup.html',error="Password confrim does not mathce password")
        user_exist = User.get_by_email(usr_input_email)
        if user_exist:
            return render_template("signup.html",error="user is already signed up")
        password_hash = generate_password_hash(usr_input_password)
        create_user(usr_input_username,usr_input_email,password_hash)

    return render_template('signup.html',error="User has been created")


@auth.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect("/")