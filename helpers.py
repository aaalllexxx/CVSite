from models.User import User


def get_user(cookie):
    sid = cookie.get("session_id")
    user: User = User.query.filter_by(session_id=sid).first()
    return user or False


def get_user_by_id(id):
    user: User = User.query.filter_by(id=id).first()
    return user or False


def has_priv(cookie, privilegies):
    user = get_user(cookie)
    if user:
        if user.role >= privilegies:
            return True
        return False
    return -1
