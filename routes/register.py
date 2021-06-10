from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
import requests
import json
import boto3
from botocore.exceptions import ClientError
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
            # Replace sender@example.com with your "From" address.
            # This address must be verified with Amazon SES.
            SENDER = "muhammadgiorady@yahoo.com"

            # Replace recipient@example.com with a "To" address. If your account 
            # is still in the sandbox, this address must be verified.
            RECIPIENT = email_para

            # Specify a configuration set. If you do not want to use a configuration
            # set, comment the following variable, and the 
            # ConfigurationSetName=CONFIGURATION_SET argument below.
            # CONFIGURATION_SET = "ConfigSet"

            # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
            AWS_REGION = "us-east-1"

            # The subject line for the email.
            SUBJECT = "Welcome to Whatch"

            # The email body for recipients with non-HTML email clients.
            BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                        "This email was sent with Amazon SES using the "
                        "AWS SDK for Python (Boto)."
                        )
                        
            # The HTML body of the email.
            BODY_HTML = """<html>
            <head></head>
            <body>
            <h1>Registration Success</h1>
            <p>Thank you for registering your account at Whatch. You can now login</p>
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

            return redirect(url_for('routes.login'))
            

        elif result.status_code == 400:
            message = json.loads(result.text)
            flash(message['message'])
            return render_template('register.html')
        else:
            #Register Fail
            return render_template('register.html')

    else:
        return render_template('register.html')
