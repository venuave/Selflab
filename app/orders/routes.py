from flask import Blueprint, render_template
from app.cookies.models import Cookie

blueprint = Blueprint('orders', __name__)
  
@blueprint.get('/checkout')
def get_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)