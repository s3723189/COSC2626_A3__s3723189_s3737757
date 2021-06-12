from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint

import requests
from . import routes

@routes.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email_para = request.form['email']
        password_para = request.form['password']
        request_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
        "default/helloworld?email={email}&password={password}&action=login".format(email = email_para, password = password_para)
        result = requests.get(url = request_query)
        data = result.json()
        
        if len(data) == 0:

            return render_template('login.html')

        
        data = data[0]
        success = log_in_user(data[2], data[3], data[1], data[0])

        if not success:
            return render_template('login.html')

        return redirect(url_for('root'))


    else:
        return render_template('login.html')



def log_in_user(name, password, email, primary_key):
    query =f"https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default/redis?action=check&token={email}"
    result = requests.get(url = query)
    result = result.json()
    if result == "b'true'":
        print('Already Logged in ')

        #### DO EMAIL STUFF HERE


        return False

    session['username'] = name
    session['password'] = password
    session['email'] = email
    session['primary_key'] = primary_key
    
    request_query = "https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default"\
        "/redis?action={action}&token={email1}".format(action = "login", email1 = email)
    result = requests.get(url = request_query)
    data = result.json()

    


    return True

