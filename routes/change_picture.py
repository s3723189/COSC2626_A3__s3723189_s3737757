from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from werkzeug.utils import secure_filename

import json
import requests
from . import routes
import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET, S3_LOCATION

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

@routes.route('/change-picture', methods = ['GET'])
def change_picture():
    return render_template('change_picture.html', profile_pic=session['profile_pic'])


@routes.route('/change-picture', methods = ['POST'])
def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file    = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """

	# C.
    if file.filename == "":
        return "Please select a file"

	# D.
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        img_url   	  = upload_file_to_s3(file, S3_BUCKET)
        email_para = session['email']

        request_query = " https://80ro3foidl.execute-api.us-east-1.amazonaws.com/default/update"

        result = requests.post(request_query, headers={'Content-Type':'application/json'}, data = json.dumps({
        'email': email_para,
        'profile_pic': img_url
        }))

        session['profile_pic'] = img_url
        
        return redirect(url_for('routes.profile'))

    else:
        return redirect("/")


    
        
def upload_file_to_s3(file, bucket_name, acl="public-read"):

    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    print(file.filename)
    print(file.content_type)
    print(file.content_length)
    print(file.mimetype)
    print(bucket_name)
    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            'profile-pic/{}'.format(file.filename),
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    img_url = "{}{}".format(S3_LOCATION, 'profile-pic/{}'.format(file.filename))

    return img_url


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS