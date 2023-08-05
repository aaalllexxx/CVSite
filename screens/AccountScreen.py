from flask import render_template, request
from helpers import get_user, get_user_by_id
from aengine_flask.screen import Screen


class AccountScreen(Screen):
    def main(self):
        user = get_user(request.cookies) or get_user_by_id(1)
        return render_template("micro_sites/users/account.html", user=user)
