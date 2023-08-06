import os
from aengine_flask.app import App
from aengine_flask.global_storage import GlobalStorage
from flask_sqlalchemy import SQLAlchemy

GlobalStorage().debug = True
base_dir = os.path.dirname(os.path.realpath(__file__))


class MyApp(App):
    def __init__(self):
        super().__init__()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"


app = MyApp()
gs = GlobalStorage()
db = SQLAlchemy(gs.app)
gs.db = db
gs.base_dir = base_dir
app.app.secret_key = os.urandom(12).hex()
if __name__ == "__main__":
    from models.User import User
    from models.Response import Response

    app.set_root_folder(base_dir)
    with app.app.app_context():
        db.create_all()
        user = User.query.filter_by(id=1).first()
        if not user:
            admin = User(name="Alex Abdelnur", image="", points=999999999)
            db.session.add(admin)
            db.session.commit()
    app.load_config(base_dir + "/config.json")
    app.run("0.0.0.0", 80, debug=True)
