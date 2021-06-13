from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
import json
from . import routes

import requests
@routes.route('/trending', methods = ['GET'])
def trending():
    if not session.get('username'):
        flash(f'Error: Please login')
        return redirect(url_for('routes.login'))
    request_query = "https://552vpnxh6b.execute-api.us-east-1.amazonaws.com/default/TrendingFunction"
    result = requests.get(url = request_query)
    data = result.json()
    
    
    return render_template('trending.html', mov = data, profile_pic=session['profile_pic'])



#https://r254gmirsg.execute-api.us-east-1.amazonaws.com/default/ExploreFunction?email=s3737757@gmail.com