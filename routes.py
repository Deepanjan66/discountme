from flask import render_template, redirect, request
import csv
from server import app
from utils import *

@app.route('/')
def discount_feed():
    return render_template("index.html")

@app.route('/discount_post')
def discount_post():
    if request.method == 'POST':
        name = request.form["name"]
        original = request.form["original_price"]
        discount = request.form["discount_price"]
        location = reuqest.form["location"]
        category = request.form["category"]
        PostManager.add_post(dict(request.form))
        return redirect(url_for('dashboard.html'))
    return render_template("discount_post.html")

@app.route('/feed')
def feed():
    postList = get_all_posts()
    return render_template("feed.html")



