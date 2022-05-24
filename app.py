from flask import Flask, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

articles_data = {
  'article-one' : {'name': 'How to be happy', 'read time': '7min'},
  'article-two' : {'name': 'How to be balanced', 'read time': '6min'},
  'article-three' : {'name': 'How to be independent', 'read time': '4min'},
}

@app.route('/')
def index():
  return '''<h1>This is Selflab blog!</h1> <a href="/about">About Blog</a> <br> <br> <a href="/articles">Articles</a>'''

@app.route('/about')
def about():
  return 'We like articles'

@app.route('/about-me')
def about_me():
  return redirect(url_for('about'))

@app.route('/articles')
def articles():
  return '''<h1>Latest articles</h1> <a href="/articles/article-one">How to be happy</a> <br> <br> <a href="/articles/article-two">How to be balanced</a> <br> <br> <a href="/articles/article-three">How to be independent</a>'''

@app.route('/articles/<slug>')
def article(slug):
  if slug in articles_data:
    return '<h1>' + articles_data[slug]['name'] + '</h1><p>' + articles_data[slug]['read time'] + '</p>'
  else:
    return 'Sorry we could not find that article.' 


if __name__ == '__main__':
  app.run()

