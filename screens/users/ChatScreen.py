from flask import render_template, request, flash, redirect
from helpers import get_user, get_user_by_id
from aengine_flask.screen import Screen
from aengine_flask.global_storage import GlobalStorage
from models.Messsge import Message

gs = GlobalStorage()


class ChatScreen(Screen):
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
                message = Message(user_id=user.id, message=form.get("message"))
                gs.db.session.add(message)
                gs.db.session.commit()
                return redirect("/user/chat")
        return render_template("micro_sites/users/chat.html", user=user)
