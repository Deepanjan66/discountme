from models import Discount_post
from server import dao
from config import *
import csv

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


