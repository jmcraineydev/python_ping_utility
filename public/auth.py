from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", text="test text")


@auth.route("/logout")
def logout():
    return "<p>LOGOUT</p>"


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email does not appear to be long enough", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater that 1 character", category="error")
        elif password1 != password2:
            flash(
                "Your password and password confrimation do not match", category="error"
            )
        elif password1 < 7:
            flash("Your password must be at least 7 characters", category="error")
        else:
            flash("Account created!", category="success")
            # add user to DB

    return render_template("signup.html")
