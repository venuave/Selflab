from . import routes, models

from app.extensions.database import db, CRUDMixin

class User(db.Model, CRUDMixin, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(128), index = True, unique = True)
  password = db.Column(db.String(1024))