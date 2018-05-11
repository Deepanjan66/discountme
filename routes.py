from flask import render_template, redirect
import csv
from server import app

@app.route('/')
def discount_feed():
    return render_template("index.html")

@app.route('/discount_post')
def discount_post():
    if request.method == 'POST':
        name = request.form["name"]
        original = request.form["original"]
        discount = request.form["discount"]
        location = reuqest.form["location"]
        category = request.form["category"]
        post_handler.add_post(name, original, discount, location, category)
        return redirect(url_for('dashboard.html'))
    return render_template("discount_post.html")

@app.route('/feed')
def feed():
    postList = get_all_posts()
    return render_template("feed.html")



