from flask import render_template, redirect, request
import csv
from server import app
from utils import *

@app.route('/')
def discount_feed():
    return render_template("all.html")

@app.route('/discount_post')
def discount_post():
    if request.method == 'POST':
        PostManager.add_post(dict(request.form))
        return redirect(url_for('dashboard.html'))
    return render_template("discount_post.html")

@app.route('/feed')
def feed():
    post_list = PostManager.get_all_posts()
    print(post_list)
    return render_template("index.html", posts=post_list)

@app.route('/dashboard')
def dashboard():
    categories = []
    return render_template("dashboard.html", categories=categories)



