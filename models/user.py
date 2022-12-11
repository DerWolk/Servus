import uuid

USERS = [
    {
        'id': uuid.uuid4().hex,
        'username': 'wolk',
        'password': 'zyx'
    }
]


def authenticate(username, password):
    user = get_user_by(username, 'username')
    if user['password'] == password:
        return user
    return None


def add_user(username, password):
    user = {
        'id': uuid.uuid4().hex,
        'username': username,
        'password': password,
    }
    USERS.append(user)
    return user


def get_user_by(username, by):
    for user_item in USERS:
        if user_item[by] == username:
            return user_item
    return None
