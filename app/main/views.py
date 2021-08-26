import datetime
from flask import render_template, redirect, url_for,abort,request, flash
from app.main.forms import Blog_Form, Comment_Form
from app.models import User, Blog, Comment
from .. import db
from . import main
from app.request import find_quotes
from flask_login import login_required, current_user

@main.route('/')
def index():

    posts = Blog.query.all()
    Sports = Blog.query.filter_by(category = 'Sports').all()
    Health = Blog.query.filter_by(category = 'Health').all()
    Maths = Blog.query.filter_by(category = 'Mathematics').all()
    Movie = Blog.query.filter_by(category = 'Movie').all()
    Car = Blog.query.filter_by(category = 'Car').all()
    Music = Blog.query.filter_by(category = 'Music').all()
    random = Blog.query.filter_by(category = 'random').all()

    api = find_quotes()
    quote = api.get('quote')
    quote_author=api.get('author')

    title= 'Welcome to Myner Blog'
    return render_template('index.html', apis= quote , author=quote_author, title = title, blog=posts, Sports=Sports, Health= Health, Maths= Maths, Movie=Movie, Car=Car, Music=Music, random=random)

@main.route('/about')
def about():
    tittle = 'About Myners Blogs'
    return render_template('about.html', tittle = tittle)

@main.route("/post/<int:blog_id>/delete", methods = ['POST','GET'])
@login_required
def delete_blogpost(blog_id):
    post = Blog.query.get(blog_id)
    post.delete_blogpost()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))

@main.route("/comment/<int:comment_id>/delete", methods = ['POST','GET'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    comment.delete_comment()
    flash('Comment deleted!', 'success')
    return redirect(url_for('main.index'))

@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    message = Blog.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=message)


@main.route('/post/<category>')
def post_category(category):

    '''
    View function that returns blogs by category
    '''
    title = f'{category.upper()}'
    if category == "all":
        blog = Blog.query.order_by(Blog.time.desc())
    else:
        blog = Blog.query.filter_by(category=category).order_by(Blog.time.desc()).all()

    return render_template('post.html',title = title,blog = blog)


@main.route('/<name>/new/post', methods=['GET','POST'])
@login_required
def new_post(name):
    form = Blog_Form()
    user = User.query.filter_by(username = name).first()

    if user is None:
        abort(404)

    title_page = "New Post"
    if form.validate_on_submit():

        title=form.title.data
        message=form.message.data
        category=form.category.data
        time = date = datetime.datetime.now()
        blog = Blog(title=title, message=message,category=category, user=current_user, time=time)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.post_category',category = category))

    return render_template('new-post.html', form=form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def add_comment(blog_id):
    form = Comment_Form()
    post = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.add_coment()
        return redirect(url_for('.add_comment', blog_id = blog_id))
    return render_template('comment_post.html', comment_form =form, post = post, all_comments=all_comments)
