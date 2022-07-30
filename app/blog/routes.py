from app.extensions.database import db
from flask import Blueprint, redirect, url_for,render_template, flash, redirect, request, abort
from flask_login import login_required
from app.blog.models import BlogPost

blueprint = Blueprint('blog', __name__)



@blueprint.route("/blog")
@login_required
def blog():
    posts = BlogPost.query.all()
    return render_template("/blog/blog.html", posts=posts)

@blueprint.get('/create')
@login_required
def get_create():
    return render_template('blog/create.html')


@blueprint.post('/create')
@login_required
def post_create():
    try:
        title = request.form['title']
        body = request.form['body']

        if not title:
            flash('Your title is missing!')
        elif not body:
            flash('Your message is missing!')


        blogpost = BlogPost(
            title=request.form.get('title'),
            body=request.form.get('body'),
        )
        blogpost.save()
        return redirect(url_for('blog.blog'))

    except Exception as error_message:
        error = error_message or 'Error while creating a user.'
        return render_template('users/register.html', error=error)



@blueprint.get('/<int:id>/edit/')
@login_required
def get_edit(id):
    posts = BlogPost.query.get(id)
    return render_template('blog/update.html', post=posts)

@blueprint.post('/<int:id>/edit/')
@login_required
def post_edit(id):
    try:
        posts = BlogPost.query.get(id)
        posts.title = request.form['title']
        posts.body = request.form['body']
        db.session.commit()
        return redirect(url_for('blog.blog'))

    except Exception as error_message:
        error = error_message or 'Error occurred while creating a user.'
        return render_template('blog/update.html', error=error)    


@blueprint.post('/<int:id>/delete/')
@login_required
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.blog'))
