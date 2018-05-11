from flask import render_template, redirect
from routes import *
from server import app

class Discount_post():
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.id = data_dict['id']
        self.original = data_dict['original_price']
        self.discount = data_dict['current_price']
        self.location = data_dict['location']
        self.category = data_dict['category']

    def get_name(self):
        return self._name

    def get_original(self):
        return self._original

    def get_discount(self):
        return self._discount

    def get_location(self):
        return self._location

    def get_category(self):
        return self._category

    def get_id(self):
        return get_unique_id()
    
