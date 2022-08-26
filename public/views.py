from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    session,
    request,
)
import schedule
import time

from public.tracking import (
    addUrlToTracking,
    getUserTrackedUrl,
    updateUserURLStatus,
    updateAllURLStatus,
)


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    if session.get("user") == None:
        return redirect(url_for("auth.login"))
    if request.method == "POST":
        url = request.form.get("url")
        addUrlToTracking(url)
    userUrls = getUserTrackedUrl()
    updateUserURLStatus(userUrls)
    userUrls = getUserTrackedUrl()
    return render_template("home.html", session=session, userUrls=userUrls)


# schedule.every(30).seconds.do(updateAllURLStatus)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
