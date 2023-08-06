from flask import render_template, request, flash, redirect
from helpers import get_user, get_user_by_id
from aengine_flask.screen import Screen
from aengine_flask.global_storage import GlobalStorage

gs = GlobalStorage()


class ShareScreen(Screen):
    options = {
        "methods": ["GET", "POST"]
    }

    def main(self):
        user = get_user(request.cookies) or get_user_by_id(1)
        if request.method == "POST":
            form = request.form
            if form:
                try:
                    identifier = form.get("id")
                    transfer_points = int(form.get("sum"))
                    final_user = get_user_by_id(int(identifier))
                    if final_user:
                        if user.points >= transfer_points > 0:
                            user.points -= transfer_points
                            final_user.points += transfer_points
                            gs.db.session.commit()
                        else:
                            flash("Не достаточно средств.")
                    else:
                        flash("Нет пользователя с таким id.")
                except ValueError:
                    flash("Не все данные введены верно.")
                return redirect("/share")

        return render_template("micro_sites/users/share.html", user=user)
