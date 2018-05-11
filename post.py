from flask import render_template, redirect
from routes import *
from server import app
id = 0
def get_unique_id():
    id += 1
    return id

class discount_post():
    def __init__(name, original, discount, location, category, _id):
        self._name = name
        self._id = _id
        self._original = original
        self._discount = discount
        self._location = location
        self._category = category
    self get_name():
        return self._name
    self get_original():
        return self._original
    self get_discount():
        return self._discount
    self get_location():
        return self._location
    self get_category():
        return self._category
    self get_id():
        return get_unique_id()
    