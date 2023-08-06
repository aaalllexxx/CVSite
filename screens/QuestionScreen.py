from flask import render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from aengine_flask.global_storage import GlobalStorage
from aengine_flask.screen import Screen
from helpers import get_user
from models.Response import Response

gs = GlobalStorage()
db: SQLAlchemy = gs.db


class QuestionScreen(Screen):
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
                theme = form.get("theme")
                message = form.get("message")
                if theme and message:
                    response = Response(user_id=user.id, theme=theme, message=message)
                    db.session.add(response)
                    db.session.commit()
                    flash("Успешно", category="success")
                flash("Введите все данные.")
                return redirect("/user/question")
        return render_template("micro_sites/users/question.html", user=user)
