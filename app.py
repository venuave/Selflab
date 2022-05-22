from flask import Flask, redirect, url_for
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
  return 'Hello World!'

@app.route('/about')
def about():
  return 'I like cookies'

if __name__ == '__main__':
  app.run()

