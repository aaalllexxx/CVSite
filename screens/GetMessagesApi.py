import json

from flask import render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from aengine_flask.global_storage import GlobalStorage
from aengine_flask.screen import Screen
from helpers import get_user, get_user_by_id
from models.Messsge import Message
from models.Response import Response

gs = GlobalStorage()
db: SQLAlchemy = gs.db


class GetMessagesApi(Screen):
    options = {
        "methods": ["GET"]
    }

    def main(self):
        messages = Message.query.all()
        resp = []
        for message in messages:
            user = get_user_by_id(message.user_id)
            resp.append({
                "name": user.name,
                "message": message.message,
                "image": user.image
            })
        return json.dumps(resp, indent=4)


