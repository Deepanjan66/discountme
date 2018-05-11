from flask import *
import csv
from server import app
from utils import *

@app.route('/')
def discount_feed():
    return render_template("index.html")

@app.route('/discount_post')
def discount_post():
    if request.method == 'POST':
        PostManager.add_post(dict(request.form))
        return redirect(url_for('dashboard.html'))
    return render_template("discount_post.html")

@app.route('/feed')
def feed():
    post_list = PostManager.get_all_posts()
    return render_template("feed.html", posts=post_list)

@app.route('/dashboard')
def dashboard():
    categories = []
    return render_template("dashboard.html", categories=categories)
@app.route('/<id>/profile')
def profile(id):
    posts = PostManager.get_post_by_user(id)
    render_template("profile.html",username = get_user_by_id(id),posts = posts)



'''
Serve static files
'''
@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)
