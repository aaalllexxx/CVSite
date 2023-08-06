import uuid
from hashlib import sha256

from flask import render_template, request, flash, redirect
from helpers import get_user, get_user_by_id, get_user_by_kw
from aengine_flask.screen import Screen
from aengine_flask.global_storage import GlobalStorage

gs = GlobalStorage()
db = gs.db

class LoginScreen(Screen):
    options = {
        "methods": ["GET", "POST"]
    }

    def main(self):
        if request.method == "POST":
            form = request.form
            if form:
                user = get_user_by_kw(name=form.get("login"))
                if user and user.password == sha256(form.get("password").encode("utf-8")).hexdigest():
                    uid = uuid.uuid4().hex
                    user.session_id = uid
                    db.session.commit()
                    resp = redirect("/user/account")
                    resp.set_cookie("session_id", uid, 1*60*60*10)
                    return resp
            flash("Неверные данные для входа.")

        return render_template("micro_sites/users/login.html")
