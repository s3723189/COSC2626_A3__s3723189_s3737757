from flask import Flask, render_template, redirect, url_for, request, session, flash
import requests
import json

from routes import *
app = Flask(__name__)
app.register_blueprint(routes)

app.secret_key = 'SECRET_KEY'
@app.route('/')
def root():

    return render_template("index.html")


@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')





def is_logged_in():
    exists = False
    if "username" in session:
        exists = True
    return exists


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
