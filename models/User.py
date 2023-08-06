from aengine_flask.global_storage import GlobalStorage

gs = GlobalStorage()
db = gs.db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(512))
    image = db.Column(db.String(512))
    role = db.Column(db.Integer)
    session_id = db.Column(db.String(512))
    points = db.Column(db.Integer, default=0)
    password = db.Column(db.String(512))
    bg_image = db.Column(db.String(512))
    Hav = db.Column(db.Integer, default=0)
    Vav = db.Column(db.Integer, default=0)
    Sav = db.Column(db.Integer, default=1)
    Hbg = db.Column(db.Integer, default=0)
    Vbg = db.Column(db.Integer, default=0)
