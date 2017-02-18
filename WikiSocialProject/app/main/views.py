from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import main
from ..models import Articles, Usersdb, db
from .forms import ArticleForm, EditProfileForm


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')


@login_required
@main.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.company_name = form.company_name.data
        db.session.add(current_user)
        flash('Профиль был изменен')
        return redirect(url_for('main.edit_profile'))
    form.username.data = current_user.user_name
    form.email.data = current_user.email
    form.company_name.data = current_user.company_name
    return render_template('edit_profile.html', form=form)


@login_required
@main.route('/articles', methods=('GET', 'POST'))
def articles():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Articles(a_title=form.title.data,
                           a_body=form.body.data,
                           userid=current_user.get_id())
        db.session.add(article)
        return redirect(url_for('main.articles'))
    user_cur = Usersdb.query.filter_by(user_name=current_user.user_name).first()
    user_articles = user_cur.articles.order_by(Articles.a_timestamp.desc()).all()
    return render_template('articles.html', form=form, articles=user_articles)


@login_required
@main.route('/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    article = Articles.query.get_or_404(article_id)
    if current_user != article.username:
        abort(403)
    form = ArticleForm()
    if form.validate_on_submit():
        article.a_title = form.title.data
        article.a_body = form.body.data
        db.session.add(article)
        flash('Статья была изменена')
        return redirect(url_for('main.articles', article_id=article.article_id))
    form.title.data = article.a_title
    form.body.data = article.a_body
    return render_template('edit_article.html', form=form)

