from aengine_flask.global_storage import GlobalStorage

gs = GlobalStorage()
db = gs.db


class Response(db.Model):
    __tablename__ = "responses"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    theme = db.Column(db.String(128), nullable=False)
    message = db.Column(db.String(256), nullable=False)
