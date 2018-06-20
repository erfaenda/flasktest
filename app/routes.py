# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Царь Дадон'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Если у тебя есть бит, я его убил!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'КАУ каУУу каУУ кауУУ каУУУУУ'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'Дэнчик Писька'},
            'body': 'Че тут вообще происходит такое'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Пароль не верен')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)