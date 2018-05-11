from flask import render_template, redirect
from routes import *
from server import app

#def get_id():
   # return curr_id + 1

class discount_post():
    def __init__(name, original, discount, location):
        self._name = name
        self._id = get_id()
        self._original = original
        self._discount = discount
        self._location = location
    self get_name():
        return self._name
    self get_original():
        return self._original
    self get_discount():
        return self._discount
    self get_location():
        return self._location
    