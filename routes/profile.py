from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint

import json
import requests, boto3, botocore
from . import routes


@routes.route('/profile', methods = ['GET', 'POST'])
def profile():

    if request.method == 'POST':
        mobile_num_para = request.form['mobile']
        username_para = request.form['username']
        email_para = session['email']
        password_para = request.form['password']

        request_query = "https://8jcresx6l2.execute-api.us-east-1.amazonaws.com/default/update"

        result = requests.post(request_query, headers={'Content-Type':'application/json'}, data = json.dumps({
        'email': email_para,
        'mobile_num': mobile_num_para,
        'username': username_para,
        'password': password_para
        }))
        return redirect(url_for('routes.profile'))

    else:
        request_query = "https://ntz3p089j3.execute-api.us-east-1.amazonaws.com/default/profile?email={email}".format(email = session['email'])
        watchlist_query = "https://dh5ajdz1q0.execute-api.us-east-1.amazonaws.com/default/watchlist?email={email}".format(email = session['email'])
        result = requests.get(url = request_query)
        result_watchlist = requests.get(url = watchlist_query)

        if result.status_code == requests.codes.ok:
            response = json.loads(result.text)
            response_watchlist = json.loads(result_watchlist.text)
            return render_template('profile.html', username=response['username'], profile_pic=response['profile_pic'], mobile=response['mobile_num'], watchlist=response_watchlist)

        else:
            return 


    
        


