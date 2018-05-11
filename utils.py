from models import *
from server import dao
from config import *
import requests

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
        print(data)
        return data

    def get_post_by_id(id):
        post_dict = next(filter(lambda u:int(u['id']) == id, dao.read(POSTS)))
        return Discount_post(post_dict)

    def get_posts_by_user(id):
        user_posts = dao.read(USER_POST)
        post_ids = [int(row['post_id']) for row in user_posts if int(row['uid']) == id]
        post_objs = list(map(PostManager.get_post_by_id, post_ids))
        return post_objs 

class LocationManager:
    def get_latitudes(locs):
        all_lats = []

        for loc in locs:
            response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=\"'\
            +loc+'\"&key=AIzaSyDg02uDO1ClnNq6h8nqx6Fx_nX8WPUog_s')

            resp_json_payload = response.json()
            try:
                response = resp_json_payload['results'][0]['geometry']['location']
                if response is None:
                    all_lats.append(None)
                    continue
            except:
                all_lats.append(None)
                continue
            all_lats.append(response)
            
        return all_lats

class CategoryManager:
    def get_categories_by_id(id):
        pass

