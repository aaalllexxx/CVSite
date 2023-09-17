from flask import render_template

from aengine_flask.screen import Screen


class HomeScreen(Screen):
    def main(self):
        return render_template("index.html")
