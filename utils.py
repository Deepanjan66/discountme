from models import *
from server import dao
from config import *

class UserManager:
    def add_user(user_form):
        # count curr user number
        uid = len(dao.read(USERS)) + 1
        user_form['id'] = uid
        dao.write(USERS, [user_form])

    def get_user_by_id(id):
        user_dict = next(filter(lambda u:int(u['id']) == id, dao.read(USERS)))
        return User(user_dict)

    def get_users():
        return [ User(user_dict) for user_dict in dao.read(USERS) ]


class PostManager:
    def add_post(data_dict):
        all_posts = dao.read(POSTS)
        data_dict['id'] = len(all_posts)
        dao.write(POSTS, [data_dict], mode="a")


    def remove_post(post):
        data = dao.read(POSTS)
        data = [row for row in data if int(row['id']) != post.id ]
        dao.write(POSTS, data, mode="w")

    def name_search(name):
        data = dao.read(POSTS)
        data = [row for row in data if name in row['name']]
        data = [Discount_post(row) for row in data]
        return data

    def category_search(category):
        data = dao.read(POSTS)
        data = [row for row in data if name in row['category']]
        data = [Discount_post(row) for row in data]
        return data

    def get_all_posts():
        data = dao.read(POSTS)
        data = [Discount_post(row) for row in data]
        return data


