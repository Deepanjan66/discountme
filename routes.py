from flask import *
import csv
from server import app
from utils import *
import requests
import json


@app.route('/discount_post', methods=["POST"])
def discount_post():
    if request.method == 'POST':
        PostManager.add_post(dict(request.form))
        return redirect(url_for('dashboard.html'))
    return render_template("discount_post.html")

@app.route('/')
@app.route('/feed')
def feed():
    post_list = PostManager.get_all_posts()
    print(post_list)
    return render_template("index.html", posts=post_list)

@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        PostManager.add_post(request.form.to_dict())
        return redirect(url_for('feed'))
    return render_template('post.html')

@app.route('/new_user', methods=["POST"])
def new_user():
    if request.method == "POST":
        UserManager.add_user(dict(request.form))
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html")

@app.route('/explore')
@app.route('/map')
def show_map():
    return render_template('map.html')

@app.route('/locs', methods=["POST"])
def locations():
    data = {}
    posts = PostManager.get_all_posts()
    locs = [post.location for post in posts]
    locs = LocationManager.get_latitudes(locs)
    all_details = [(l, p.name) for l, p in zip(locs, posts)]

    for i, loc in enumerate(all_details):
        data[i] = (loc[0]['lat'], loc[0]['lng'], loc[1])

    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    data['curr'] = (j['latitude'], j['longitude'])
    data['size'] = len([key for key in data]) - 1
    print(data)

    return json.dumps(data)

@app.route('/profile/<id>')
def dashboard(id):
    id = int(id)
    posts = PostManager.get_posts_by_user(id)
    return render_template("profile.html",username=UserManager.get_user_by_id(id).name, posts = posts)


'''
Serve static files
'''
@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)
