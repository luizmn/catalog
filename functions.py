# This file contains functions used in the catalog
from flask import session as login_session

# BEGIN - User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'],  # NOQA
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# END - User Helper Functions
