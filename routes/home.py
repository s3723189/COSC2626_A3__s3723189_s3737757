from boto3 import resource
from botocore.utils import datetime2timestamp
from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from . import routes

import requests
@routes.route('/home', methods = ['GET', 'POST'])
def home():
    

    if not check_session():
        flash(f'Error: Please login')
        return redirect(url_for('routes.login'))

    search_data = []
    
    search = request.args.get('search', None)



    request_query = "https://552vpnxh6b.execute-api.us-east-1.amazonaws.com/default/TrendingFunction"
    result = requests.get(url = request_query)
    data = result.json()
    data = data[:4]

    if search is not None:
        search_data = return_movies(search)
        print(search_data)
        return render_template("home.html", mov = data, search_mov = search_data, keyword = search, profile_pic=session['profile_pic'])
    else:
        print('Search none')

    
    return render_template("home.html", mov = data, profile_pic=session['profile_pic'])


def return_movies(search):
    request_query = "https://td6hnl707c.execute-api.us-east-1.amazonaws.com/default"\
    "/Elasticsearch?action=search&value={value}".format(value = search)
    result = requests.get(url = request_query)
    data_search = result.json()
    results = []
    final_result = []
    for row in data_search:
        results.append(row['_source']['movie_id'])
    

    seen = set()
    for row in results:
        request_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
        "default/helloworld?action=movie&id={id}".format(id = row)
        result_query = requests.get(url = request_query)
        data = result_query.json()
        if row not in seen:
            seen.add(row)
            final_result.append(data)
      

    return final_result


def check_session():
    if not session.get('username'):
        return False
    query =f"https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default/redis?action=check&token={session['email']}"
    result = requests.get(url = query)
    result = result.json()
   
    if result != "b'true'":
        session.clear()
        return False
    
    
    return True