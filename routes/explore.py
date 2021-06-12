from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
import json
from . import routes

import requests
@routes.route('/explore', methods = ['GET'])
def explore():
    print(session['username'])

    data_1 = get_genre('Romance')
    data_2 = get_genre('Sci-Fi')
    data_3 = get_genre('Action')
    data_4 = get_genre('Adventure')
    data_5 = get_genre('Horror')
    data_6 = get_genre('Thriller')
    data_7 = get_genre('Korean')
    data_8 = get_genre('Japanese')
    data_9 = get_genre('Anime')
  
    print(data_9)

    return render_template('explore.html', mov_rom = data_1, 
        mov_sf = data_2, 
        mov_act = data_3, 
        mov_adv = data_4,
        mov_hor = data_5,
        mov_thr = data_6,
        mov_kor = data_7,
        mov_jp = data_8,
        mov_ani = data_9,
    )


def get_genre(genre):
    request_query = "https://r254gmirsg.execute-api.us-east-1.amazonaws.com/"\
    "default/ExploreFunction?email={email}&genre={gen}".format(email = session['email'], gen = genre)
    result = requests.get(url = request_query)
    return result.json()

#https://r254gmirsg.execute-api.us-east-1.amazonaws.com/default/ExploreFunction?email=s3737757@gmail.com