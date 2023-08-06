from flask import render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from aengine_flask.global_storage import GlobalStorage
from aengine_flask.screen import Screen
from helpers import get_user
from models.Response import Response

gs = GlobalStorage()
db: SQLAlchemy = gs.db


class EditScreen(Screen):
    options = {
        "methods": ["GET", "POST"]
    }

    def main(self):
        user = get_user(request.cookies)
        if not user:
            return redirect("/user/login")
        if request.method == "POST":
            form = request.form
            if form:
                Hav = form.get("Hav")
                Vav = form.get("Vav")
                Sav = form.get("Sav")
                Hbg = form.get("Hbg")
                Vbg = form.get("Vbg")
                name = form.get("name")
                user.Hav = Hav or 0
                user.Vav = Vav or 0
                user.Sav = Sav or 0
                user.Hbg = Hbg or 0
                user.Vbg = Vbg or 0
                user.name = name
                db.session.commit()
            files = request.files
            if files:
                profile = files["profile_image"]
                bg = files["bg_image"]
                if profile:
                    profile.save(gs.base_dir + f"/static/imgs/downloaded/{user.id}_pf.{profile.filename.split('.')[-1]}")
                    user.image = f"/static/imgs/downloaded/{user.id}_pf.{profile.filename.split('.')[-1]}"
                if bg:
                    bg.save(gs.base_dir + f"/static/imgs/downloaded/{user.id}_bg.{bg.filename.split('.')[-1]}")
                    user.bg_image = f"/static/imgs/downloaded/{user.id}_bg.{bg.filename.split('.')[-1]}"
                db.session.commit()
        return render_template("micro_sites/users/edit.html", user=user)
