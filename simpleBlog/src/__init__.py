from flask import Flask
from flask_login import LoginManager,UserMixin


def create_app():   
    app = Flask(__name__)
    app.secret_key = "my_sec_key"

    # Connect blueprint to our main app
    from src.views import views
    # url_prifix is the root url which means for example if i wanna to visit /home
    # and url_prefix is /root so i have to go to /root/home
    app.register_blueprint(views, url_prefix='/')

    from src.auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app

