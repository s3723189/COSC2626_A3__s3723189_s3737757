import os

S3_BUCKET                 = "XXX"
S3_KEY                    = "XXX"
S3_SECRET                 = "XXX"
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000