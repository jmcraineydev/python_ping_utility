from flask import Flask
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from flask_login import LoginManager

load_dotenv()

cluster = MongoClient(os.getenv("MONGO_DB_CONNECTION"))
db = cluster["PingUtil"]
userCollection = db["user"]


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        return userCollection.find_one({"email": email})

    return app
