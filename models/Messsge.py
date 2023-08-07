from aengine_flask.global_storage import GlobalStorage

gs = GlobalStorage()
db = gs.db


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    message = db.Column(db.String(256), nullable=False)
