from flask import Flask
from DAO import csvDAO

app = Flask(__name__)
app.config['SECRET_KEY'] = "a"

dao = csvDAO(app.root_path)
