from pprint import pprint

from STEMizer.models import User, Post
from flask import render_template, request, flash, redirect, url_for
from STEMizer.forms import RegistrationForm, LoginForm
from STEMizer import app, db, bcrypt, main_functions, forms
import requests
from flask_login import login_user, current_user, logout_user, login_required


####################################
# Main Page
####################################

@app.route('/')
@app.route('/home')
def home():
    return render_template('stemizer_homepage.html')

####################################
# Project 6: TBA
####################################

@app.route('/unknown')
def unknown():
    return render_template('unknown.html')

####################################
# Registration Route
####################################
@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('stemizer'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('login'))
    return render_template('english/register.html',title="Register", form=form)

####################################
# Login Route
####################################
@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('stemizerEN'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('stemizerEN'))
        # if form.email.data == 'greg@greg.com' and form.password.data == 'murad':
        #     flash('You have been loged in!','success')
        #     return redirect(url_for('stemizer'))
        # else:
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('english/login.html',title='Login', form=form)

####################################
# Logout Route
####################################
@app.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

####################################
# STEMIZER in English
####################################

@app.route('/stemizerEN')
@login_required
def stemizerEN():
    return render_template('english/stemizer_homepage_en.html')

####################################
# STEMIZER em Portugues
####################################

@app.route('/stemizerPT')
@login_required
def stemizerPT():
    return render_template('portugues/stemizer_homepage_pt.html')

####################################
# Chapter 4
####################################

@app.route('/chapter4')
def chapter4():
    return render_template('english/book5/chapter5_1/introduction.html')

####################################
# Account
####################################
@app.route("/account")
@login_required
def account():
    return render_template('english/account.html', title='Account')