from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
import requests
from . import routes

@routes.route('/login', methods = ['GET', 'POST'])
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
