from flask import Blueprint, render_template, request, redirect
from .db import db
from .models import Url
import re

new_app = Blueprint('new_app', __name__)

@new_app.route('/<short_url>')
def redirect_to_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first()
    
    return redirect(url.original_url)

@new_app.route('/')
def add_index():
    return render_template('index.html')

@new_app.route('/add_url', methods=['POST'])
def add_url():
    
    org_url =request.form['original_url']
    original = re.compile(r'https?://(www\.)?')
    original_url = original.sub('', org_url).strip().strip('/')

    url = Url.query.filter_by(original_url=original_url).first()
    if url:
        url.visits = url.visits + 1
    else:
        url = Url(original_url=original_url)
    
        db.session.add(url)
    db.session.commit()
    return render_template('url_added.html' , new_url = url.short_url, original_url = url.original_url)
    
@new_app.route('/visits', methods = ['POST'])
def visits():
    url = Url.query.all()
    return render_template('visit.html', urls=url)


