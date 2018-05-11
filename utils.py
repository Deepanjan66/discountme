from src.User import User
from server import dao

class UserManager:
    def add_user(user_form):
        # count curr user number
        uid = len(dao.read(USERS)) + 1
        user_form['id'] = uid
        dao.write(USERS, [user_form])

    def get_user_by_id(self, id):
        user_dict = next(filter(lambda u:u['id'] == id, dao.read(USERS)))
        return User(user_dict)
