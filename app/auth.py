#user blue print
from flask import Blueprint
from flask import Flask,request,render_template,flash,redirect,url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .exts import db
from .forms import RegisterForm,NameLoginForm


bp = Blueprint('auth',__name__,url_prefix= '/auth')

@bp.route('/login',methods=['GET','POST'])
def login():
    '''
        Default Login Method,Username
    '''
    login_form = NameLoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        u = User.query.filter_by(username = username).first()
        emsg = None
        if u is None:
            emsg = 'The username is not exist'
        elif not check_password_hash(u.password,password):
            emsg = 'Wrong Password'
        if emsg is None:
            remember = login_form.remember.data
            login_user(u,remember = remember)
            return redirect(url_for('blog.index'))
        flash(emsg)

    return render_template('auth/login.html',form = login_form)

@bp.route('/register',methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        exists = User.query.filter_by(username = username).first()
        if exists:
            emsg = 'This username is exist'
            flash(emsg)
            return render_template('auth/register.html',form = register_form)
        password = generate_password_hash(register_form.password.data,f'pbkdf2:sha256:260000')
        u = User(username = username,password = password)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html',form = register_form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



# @bp.route('/register787',methods=['GET','POST'])
# def register787():
#     print('regist')
#     if request.method =='POST':
#         username = request.form['username']
#         password = request.form['password']
#         error = None


#         if not username:
#             error = 'Username cannot be blank'
#         elif not password:
#             error = 'Password cannot be blank'
#         elif User.query.filter_by(username = username).first() is not None:
#             error = 'User "{}" is existed now'.format(username)

#         if error is None:
#             u=User(username = username,password = generate_password_hash(password,f'pbkdf2:sha256:260000'))
#             # u=User(username = username,password = generate_password_hash(password))
#             #pbkdf2 is short, the default method 'scrypt:32768:8:1' is too long
#             #we can change the password length to adapt the scrypt method
#             db.session.add(u)
#             db.session.commit()
#             return redirect(url_for('auth.login'))
        
#         flash(error)
#     return render_template('auth/register787.html')

