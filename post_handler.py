from post import discount_post
from routes import *
import csv

def add_post(name, original, discount, location):
    post = discount_post(name, original, discount, location, category)
    csv.write(post)
    pass

def remove_post(post):
    with open('something.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = "?")
        for row in reader:
            if row[5] == post.get_id():
                writer.writerow(row)
    pass

def name_search(name):
    postList = []
    with open('something.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter = "?")
        for row in reader:
            if row[0] == name:
                postList.append(??)
    return postList

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
    return postList
