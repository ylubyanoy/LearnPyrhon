from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import Usersdb, db
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Пользователь {} добро пожаловать!!!'.format(form.username.data))
        ref_user = Usersdb.query.filter_by(user_name=form.username.data).first()
        if ref_user is not None:
            login_user(ref_user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Usersdb(email=form.email.data,
                       user_name=form.username.data,
                       user_pass=form.password.data)
        db.session.add(user)
        flash('Теперь вы можете авторизоваться')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из профиля пользователя')
    return redirect(url_for('main.index'))
