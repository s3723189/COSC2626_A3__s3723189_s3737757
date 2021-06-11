from boto3 import resource
from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from . import routes

import requests
@routes.route('/home/<search>', methods = ['GET', 'POST'])
@routes.route('/home', methods = ['GET', 'POST'])
def home(search = None):
    return_movies(search)
    
    request_query = "https://552vpnxh6b.execute-api.us-east-1.amazonaws.com/default/TrendingFunction"
    result = requests.get(url = request_query)
    data = result.json()
    data = data[:5]

    

    
    return render_template("home.html", mov = data)


def return_movies(search):
    request_query = "https://td6hnl707c.execute-api.us-east-1.amazonaws.com/default"\
    "/Elasticsearch?action=search&value={value}".format(value = search)
    result = requests.get(url = request_query)
    data_search = result.json()
    results = []
    for row in data_search:
        results.append(row['_source'])
    
    print(results)