from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post
from flask_blog import app


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/test')
def test():
    return render_template("testBoot.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data} !!!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com"and form.password.data == "pass":
            flash(f"you have logged in as {form.email.data}", 'success')
            return redirect(url_for('home'))
        else:
            flash("please check you credentials", 'danger')
    return render_template('login.html', title="Login", form=form)
