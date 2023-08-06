from hashlib import sha256


def get_user(cookie):
    from models.User import User
    sid = cookie.get("session_id")
    user: User = User.query.filter_by(session_id=sid).first()
    return user or False


def get_user_by_id(id):
    from models.User import User
    user: User = User.query.filter_by(id=id).first()
    return user or False


def get_user_by_kw(**kwargs):
    from models.User import User
    user: User = User.query.filter_by(**kwargs).first()
    return user or False


def has_priv(cookie, privilegies):
    user = get_user(cookie)
    if user:
        if user.role >= privilegies:
            return True
        return False
    return -1


def encrypt_pass(passw):
    return sha256(passw.encode("utf-8")).hexdigest()
