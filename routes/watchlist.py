from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from . import routes

import requests
@routes.route('/watchlist/<int:movie_name>')
def watchlist(movie_name):

    print(movie_name)

    wl_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/default"\
    "/helloworld?action=wladd&id={id}&mov={mov}"\
    "".format(id = session["primary_key"], mov = movie_name)

    result = requests.get(url = wl_query)
    
    data = result.json()

    

    
    return redirect(url_for('routes.home'))

    