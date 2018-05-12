from models import *
from server import dao, app
from config import *
import requests
import os
import facebook
import smtplib
from collections import defaultdict

class UserManager:
    def add_user(user_form):
        # count curr user number
        uid = len(dao.read(USERS)) + 1
        user_form['id'] = uid
        dao.write(USERS, [user_form])

    def get_user_by_id(id):
        all_users = dao.read(USERS)
        for user in all_users:
            if user['id'] == str(id):
                return User(user)
        return None

    def get_users():
        return [ User(user_dict) for user_dict in dao.read(USERS) ]

    def get_users_categories():
        data = dao.read(USER_CATEGORIES)
        rels = defaultdict(list)
        for rel in data:
            if rel['category'] not in rel['user_id']:
                rels[rel['user_id']].append(rel['category'])

        return rels



class PostManager:
    def add_post(data_dict, uploaded_file=None):
        all_posts = dao.read(POSTS)
        data_dict['id'] = len(all_posts)
        if uploaded_file is not None:
            filename = str(data_dict['id']) + ".jpg"
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data_dict.pop('file', None)
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
        data = [row for row in data if category == row['category'] or category == 'all']
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

    def get_all_categories():
        all_category = [entry.category for entry in PostManager.get_all_posts()]
        all_category = list(set(all_category))
        return all_category

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

class FacebookManager:
    def get_friends():
        return graph.get_connections(id='me', connection_name='friends')

    def send_message(msg, audience_type):
         graph.put_object(parent_object='me', connection_name=audience_type,
                                   message=msg)
class EmailManager:
    def send_email(recipient, content):
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email, password)

        server.sendmail("z5110198@unsw.edu.au", recipient, content)
        server.quit()






