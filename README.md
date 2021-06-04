# CREATING TABLE
python

from url_shortener import create_app

from url_shortener.db import db

from url_shortener.models import Url

db.create_all(app=create_app())

exit()


# TO CHECK TABLES
sqlite3 url_shortener/db.sqlite3

.tables

# DOCKER IMAGE BUILD & RUN

docker build -t docker_flask .

docker run -d --name flask_container -p 5000:5000 docker_flask

can run localhost:5000 and can see the app
