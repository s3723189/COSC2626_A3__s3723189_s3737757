from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from . import routes

import requests
@routes.route('/movie/<movie_name>', methods = ['GET', 'POST'])
def movie(movie_name):

    request_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
    "default/helloworld?action=movie&id={id}".format(id = movie_name)
    result = requests.get(url = request_query)

    request_query_cast = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
    "default/helloworld?action=staff&type=cast&id={id}".format(id = movie_name)

    request_query_director = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
    "default/helloworld?action=staff&type=director&id={id}".format(id = movie_name)

    request_query_genre = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
    "default/helloworld?action=genre&id={id}".format(id = movie_name)

    result_cast = requests.get(url = request_query_cast)
    result_director = requests.get(url = request_query_director)
    result_genre = requests.get(url = request_query_genre)
    
    data = result.json()
    data_cast = result_cast.json()
    data_director = result_director.json()
    data_genre = result_genre.json()
    data = data[0]

    return render_template('movie.html', movie = data,  cast = data_cast, director = data_director, genres = data_genre)

    


