from app import app
from flask import render_template,flash, redirect
from .forms import LoginForm


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for '+form.nickname.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
