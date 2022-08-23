from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import userCollection
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = userCollection.find_one({"email": email})
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                # session["user"] = user
                flash("Logged in successfully!", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash(
                "Email does not exist, please check your email or make a new account",
                category="error",
            )

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = userCollection.find_one({"email": email})

        if user:
            flash("Email is already registered", category="error")
        elif len(email) < 4:
            flash("Email does not appear to be long enough", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater that 1 character", category="error")
        elif password1 != password2:
            flash(
                "Your password and password confrimation do not match", category="error"
            )
        elif len(password1) < 7:
            flash("Your password must be at least 7 characters", category="error")
        else:
            hashedPw = generate_password_hash(password1, method="sha256")
            new_user = {"email": email, "first_name": firstName, "password": hashedPw}
            userCollection.insert_one(new_user)
            login_user(new_user, remember=True)
            # session["user"] = new_user
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)
