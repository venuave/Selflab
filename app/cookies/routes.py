from .models import Cookie
from flask import Blueprint, render_template, request, current_app
from flask_login import login_required



blueprint = Blueprint('cookies', __name__)


@blueprint.route('/cookies/<slug>')
@login_required
def cookie(slug):
  cookie = Cookie.query.filter_by(slug=slug).first_or_404()
  return render_template('cookies/show.html', cookie=cookie)

@blueprint.route('/cookies')
@login_required
def cookies():
  page_number = request.args.get('page', 1, type=int)
  cookies_pagination = Cookie.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
  return render_template('cookies/cookies.html', cookies_pagination=cookies_pagination)

#@blueprint.route('/articles')
# def articles():
  #return '''<h1>Latest articles</h1> <a href="/articles/article-one">How to be happy</a> <br> <br> <a href="/articles/article-two">How to be balanced</a> <br> <br> <a href="/articles/article-three">How to be independent</a>'''

#@blueprint.route('/articles/<slug>')
# def article(slug):
  #if slug in articles_data:
   # return '<h1>' + articles_data[slug]['name'] + '</h1><p>' + articles_data[slug]['read time'] + '</p>'
  #else:
   # return 'Sorry we could not find that article.' 
