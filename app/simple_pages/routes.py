from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/about')
def about():
  return render_template('about.html')

@blueprint.route('/registration')
def registration():
  return render_template('registration.html')

@blueprint.route('/')
def index():
  name = 'Sam'
  fake_number = 342
  return render_template('simple_pages/index.html', name=name, visitor_number=fake_number)

@blueprint.route('/blog')
def blog():
  return render_template ('blog.html')

@blueprint.route('/legal')
def legal():
  return send_file('static/downloads/legal.txt', as_attachment=True)