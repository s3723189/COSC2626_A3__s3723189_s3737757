from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
import requests
import json
from . import routes

@routes.route('/register', methods = ['GET', 'POST'])
def register():

    if request.method == 'POST':
        mobile_num_para = request.form['mobile']
        username_para = request.form['username']
        email_para = request.form['email']
        password_para = request.form['password']

        request_query = "https://w8js23acze.execute-api.us-east-1.amazonaws.com/default/register"

        result = requests.post(request_query, headers={'Content-Type':'application/json'}, data = json.dumps({
        'mobile_num': mobile_num_para,
        'username': username_para,
        'email': email_para,
        'password': password_para
        }))

        if result.status_code == requests.codes.ok:
            #Register Success
            return redirect(url_for('routes.login'))
        else:
            #Register Fail
            return render_template('register.html')

    else:
        return render_template('register.html')
