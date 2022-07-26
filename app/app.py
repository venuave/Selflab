from flask import Flask

from .simple_pages.__init__ import routes
from . import cookies, simple_pages, orders, api, users
from app.extensions.database import db, migrate
from app.extensions.authentication import login_manager

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')
  
  register_extensions(app)
  register_blueprints(app)

  return app

# Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)
  app.register_blueprint(api.routes.blueprint)
  app.register_blueprint(users.routes.blueprint)



def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)
