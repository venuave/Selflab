from .models import Cookie, Article
from flask import Blueprint, render_template


#remove
cookies_data = {
  'chocolate-chip' : {'name': 'Chocolate Chip', 'price': '$1.50'},
  'oatmeal-raisin' : {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  'sugar' : {'name': 'Sugar', 'price': '$0.75'},
  'peanut-butter' : {'name': 'Peanut Butter', 'price': '$0.50'},
  'oatmeal' : {'name': 'Oatmeal', 'price': '$0.25'},
  'salted-caramel' : {'name': 'Salted Caramel', 'price': '$1.00'},
}

articles_data = {
  'article-one' : {'name': 'How to be happy', 'read time': '7min'},
  'article-two' : {'name': 'How to be balanced', 'read time': '6min'},
  'article-three' : {'name': 'How to be independent', 'read time': '4min'},
}

blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies')
def cookies():
  return render_template('cookies/cookies.html')

@blueprint.route('/articles')
def articles():
  return '''<h1>Latest articles</h1> <a href="/articles/article-one">How to be happy</a> <br> <br> <a href="/articles/article-two">How to be balanced</a> <br> <br> <a href="/articles/article-three">How to be independent</a>'''

@blueprint.route('/articles/<slug>')
def article(slug):
  if slug in articles_data:
    return '<h1>' + articles_data[slug]['name'] + '</h1><p>' + articles_data[slug]['read time'] + '</p>'
  else:
    return 'Sorry we could not find that article.' 
