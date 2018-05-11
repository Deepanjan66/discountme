from flask import render_template, redirect
from routes import *
from server import app
id = 0
def get_unique_id():
    id += 1
    return id

class discount_post():
    def __init__(self, name, original, discount, location, category, _id):
        self._name = name
        self._id = _id
        self._original = original
        self._discount = discount
        self._location = location
        self._category = category

    def get_name(self):
        return self._name

    def get_original(self):
        return self._original

    def self get_discount(self):
        return self._discount

    def self get_location(self):
        return self._location

    def self get_category(self):
        return self._category

    def self get_id(self):
        return get_unique_id()
    
