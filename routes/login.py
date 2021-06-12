from flask import render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint

import json
import boto3
import requests
from botocore.exceptions import ClientError
from . import routes

@routes.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        email_para = request.form['email']
        password_para = request.form['password']
        request_query = "https://5aegj1tt7i.execute-api.us-east-1.amazonaws.com/"\
        "default/helloworld?email={email}&password={password}&action=login".format(email = email_para, password = password_para)
        result = requests.get(url = request_query)
        data = result.json()
        
        if len(data) == 0:

            return render_template('login.html')

        
        data = data[0]
        success = log_in_user(data[2], data[3], data[1], data[0])

        if not success:
            return render_template('login.html')

        return redirect(url_for('root'))


    else:
        return render_template('login.html')



def log_in_user(name, password, email, primary_key):
    query =f"https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default/redis?action=check&token={email}"
    result = requests.get(url = query)
    result = result.json()
    if result == "b'true'":
        print('Already Logged in ')

        SENDER = "muhammadgiorady@yahoo.com"
        RECIPIENT = email
        AWS_REGION = "us-east-1"
        SUBJECT = "Multiple Login Warning"
        BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                    "This email was sent with Amazon SES using the "
                    "AWS SDK for Python (Boto)."
                    )
                    
        # The HTML body of the email.
        BODY_HTML = """<html>
        <head>Warning</head>
        <body>
        <h1></h1>
        <p>Your account has been logged in from another location / browser</p>
        </body>
        </html>
                    """            

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
        return False

    session['username'] = name
    session['password'] = password
    session['email'] = email
    session['primary_key'] = primary_key
    
    request_query = "https://tqxdruy9ka.execute-api.us-east-1.amazonaws.com/default"\
        "/redis?action={action}&token={email1}".format(action = "login", email1 = email)
    result = requests.get(url = request_query)
    data = result.json()

    


    return True

