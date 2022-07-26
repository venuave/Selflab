from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/about') 
def about():
  return render_template('simple_pages/about_me.html')

@blueprint.route('/registration')
def registration():
  return render_template('simple_pages/registration.html')


@blueprint.route('/blog')
def blog():
  return render_template ('simple_pages/blog.html')

@blueprint.route('/base')
def base():
  return render_template ('simple_pages/base.html')



