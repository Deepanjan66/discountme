from post import Discount_post
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
    """
    def category_search(category):
        postList = []
        with open('something.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter = "?")
            for row in reader:
                if row[4] == category:
                    postList.append(??)
        return postList
    def get_all_posts():
        postList = []
        with open('something.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter ="?")
            for row in reader:
                postList.append(??)
        return postList"""


