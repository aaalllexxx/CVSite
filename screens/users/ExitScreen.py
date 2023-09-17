from flask import render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from aengine_flask.global_storage import GlobalStorage
from aengine_flask.screen import Screen
from helpers import get_user
from models.Response import Response

gs = GlobalStorage()
db: SQLAlchemy = gs.db


class ExitScreen(Screen):
    options = {
        "methods": ["GET", "POST"]
    }

    def main(self):
        user = get_user(request.cookies)
        if not user:
            return redirect("/user/login")
        user.session_id = ""
        db.session.commit()
        return redirect("/user/login")
