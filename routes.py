from flask import *
import csv
from server import app
from utils import *

@app.route('/')
def discount_feed():
    return render_template("index.html")

@app.route('/feed')
def feed():
    post_list = PostManager.get_all_posts()
    return render_template("feed.html", posts=post_list)

@app.route('/dashboard')
def dashboard():
    categories = []
    return render_template("dashboard.html", categories=categories)

@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        PostManager.add_post(request.form.to_dict())
        return redirect(url_for('feed'))
    return render_template('post.html')

'''
Serve static files
'''
@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)
