from .db import db
import string
from random import choices
from .db import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200), unique=True)
    short_url = db.Column(db.String(16))
    visits = db.Column(db.Integer, default=0)



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()
    
    def generate_short_url(self):
        characters =  string.digits + string.ascii_letters
        path = ''.join(choices(characters, k = 3))
        short_url = "{domain}{path} ".format(domain='wrlc.shrt', path = path)
        
        url = self.query.filter_by(short_url=short_url).first()
        
        if url:
            return self.generate_short_url()

        return short_url

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(200))
    visits = db.Column(db.Integer, default=0)

   