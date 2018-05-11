from flask import render_template, redirect

from server import app

@app.route('/')
def discount_feed():
    return render_template("index.html")
