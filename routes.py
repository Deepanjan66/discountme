from flask import *
import csv
from server import app
from utils import *
import requests
import json

@app.route('/')
@app.route('/feed', defaults={'category': 'all'})
@app.route('/feed/<category>', )
def feed(category='all'):
    post_list = PostManager.category_search(category)
    all_category = [entry.category for entry in PostManager.get_all_posts()]
    all_category = list(set(all_category))
    # print(post_list)

    
    return render_template("feed.html", posts=post_list, 
            all_category=all_category, curr_category=category)

@app.route('/post', methods = ['POST', 'GET'])
def post():
    if request.method == 'POST':
        PostManager.add_post(request.form.to_dict(), request.files['file'])
        rels = UserManager.get_users_categories()
        print("Hello")

        for r_id in rels:
            print(r_id, rels[r_id])
            if r_id not in rels:
                continue
            if request.form['category'] in rels[r_id]:
                print("Hello 3")
                EmailManager.send_email(UserManager.get_user_by_id(r_id).email,\
                        "We found a new discount offer for you. {} is going at {}".format(request.form['name'], request.form['current_price']))
                print("Hello4")

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
    all_details = [(l, p.name, p.current_price) for l, p in zip(locs, posts)]

    for i, loc in enumerate(all_details):
        data[i] = (loc[0]['lat'], loc[0]['lng'], loc[1], loc[2])

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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    filename += ".jpg"
    print(filename)
    print(app.config['UPLOAD_FOLDER'])
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                                           filename)


'''
Serve static files
'''
@app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)
