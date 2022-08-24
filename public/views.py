from flask import Blueprint, render_template, session, redirect, url_for, session

views = Blueprint("views", __name__)


@views.route("/")
def home():
    if session.get("user") == None:
        return redirect(url_for("auth.login"))
    return render_template("home.html", session=session)
