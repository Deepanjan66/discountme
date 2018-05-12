from flask import Flask
from DAO import csvDAO
import facebook
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = "a"

dao = csvDAO(app.root_path)
UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
graph = facebook.GraphAPI(access_token=config.fb_key, version="3.0")

