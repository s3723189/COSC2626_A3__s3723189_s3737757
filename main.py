from flask import Flask, render_template, redirect, url_for, request, session, flash
import requests
import json
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
@app.route('/')
def root():

    return render_template("index.html")



@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email_para = request.form['email']
        password_para = request.form['password']
        request_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
        "default/helloworld?email={email}&password={password}".format(email = email_para, password = password_para)
        result = requests.get(url = request_query)
        data = result.json()
        if len(data) == 0:
            return render_template('login.html')
        
        data = data[0]
        log_in_user(data[1], data[2], data[3], data[0])
        return render_template('index.html')


    else:
        return render_template('login.html')




    return "testing"

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')



def log_in_user(name, password, email, primary_key):
    session['username'] = name
    session['password'] = password
    session['email'] = email
    session['primary_key'] = primary_key

    



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

