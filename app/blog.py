#blog blueprint
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from . models import Post
from . forms import PostForm
from . exts import db

bp = Blueprint('blog',__name__,url_prefix='/')

@bp.route('/')
def index():
    return 'index'

@bp.route('/detail/<int:id>')
def detail(id):     #search
    return 'detail'

@bp.route('/add',methods = ['GET','POST'])
@login_required
def add():          #add
    form = PostForm()
    if form.validate_on_submit():
        post = Post(author = current_user)
        post.title = form.title.data.strip()
        post.content = form.content.data
        post.content_html = ''
        post.abstract = form.abstract.data.strip()
        if not post.abstract:
            post.abstract = post.abstract[:255]
        db.session.add(post)
        db.session.session.commit()
        post = Post.query.filter_by(author = current_user,title = post.title).order_by(
            Post.created.desc()).first()
        return redirect(url_for('blog.detail',id = post.id))
    return render_template('blog/edit.html',form = form)

@bp.route('/edit/<int:id>',methods = ['GET','POST'])
def edit(id):       #edit
    return 'edit'

@bp.route('/delete/<int:id>')
def delete(id):     #delete
    return 'del'