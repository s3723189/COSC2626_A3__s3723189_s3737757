import os

S3_BUCKET                 = "s3737757-s3723189-a3"
S3_KEY                    = "AKIA6QWQLLEFA7HQ3S5O"
S3_SECRET                 = "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"
#S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
S3_LOCATION                = "https://d1jphzkpp95em7.cloudfront.net/"

SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000