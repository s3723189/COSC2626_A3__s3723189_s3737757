from flask import Flask, render_template, redirect, url_for, request, session, flash
import requests
import json

from routes import *
application = Flask(__name__)
application.register_blueprint(routes)

application.secret_key = 'SECRET_KEY'
@application.route('/')
def root():

    return render_template("login.html")


@application.route('/logout')
def logout():
    
    query =f"https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default/redis?action=logout&token={session['email']}"
    requests.get(url = query)
    session.clear()
    return redirect(url_for('routes.login'))





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
    application.debug = True
    application.run()