import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #'sqlite:///db.sqlite3' #

SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME = os.environ.get('USER')
ADMIN_PASSWORD = os.environ.get('PASSWORD')