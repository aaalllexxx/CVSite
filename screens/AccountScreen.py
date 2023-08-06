from flask import render_template, request, redirect
from helpers import get_user, get_user_by_id
from aengine_flask.screen import Screen


class AccountScreen(Screen):
    def main(self):
        user = get_user(request.cookies)
        if not user:
            return redirect("/user/login")
        return render_template("micro_sites/users/account.html", user=user)
