from model import db
from model.models import User


def db_check_if_not_insert_to_db_and_get_user_id(email, name, provider, unique_id):
    user = User.query.filter_by(uid=unique_id).first()
    if not user:
        user = User(name=name, email=email, uid=unique_id, oauth=provider)
        db.session.add(user)
        db.session.commit()
        return user.id
    return user.id

def guset_insert_to_db(email, name, provider, unique_id):
    user = User(name=name, email=email, uid=unique_id, oauth=provider)
    db.session.add(user)
    db.session.commit()