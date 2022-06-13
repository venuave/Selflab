from flask import Flask, redirect, url_for, render_template, send_file
app = Flask(__name__)
app.config.from_object('config')

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

#@app.route('/')
# def index():
#return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/registration')
def registration():
  return render_template('registration.html')

@app.route('/cookies')
def cookies():
  return render_template('cookies.html')

@app.route('/')
def index():
  name = 'Sam'
  fake_number = 342
  return render_template('index.html', name=name, visitor_number=fake_number)

# @app.route('/about')
# def about():
  #return 'We like articles'

@app.route('/about-me')
def about_me():
  return render_template ('about.html')

@app.route('/blog')
def blog():
  return render_template ('blog.html')

@app.route('/articles')
def articles():
  return '''<h1>Latest articles</h1> <a href="/articles/article-one">How to be happy</a> <br> <br> <a href="/articles/article-two">How to be balanced</a> <br> <br> <a href="/articles/article-three">How to be independent</a>'''

@app.route('/articles/<slug>')
def article(slug):
  if slug in articles_data:
    return '<h1>' + articles_data[slug]['name'] + '</h1><p>' + articles_data[slug]['read time'] + '</p>'
  else:
    return 'Sorry we could not find that article.' 

@app.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)

if __name__ == '__main__':
  app.run()

