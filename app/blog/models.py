from flask_login import UserMixin
from app.extensions.database import db, CRUDMixin

class BlogPost(db.Model, CRUDMixin, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(128), index = True, unique = True)
  body = db.Column(db.String(400))