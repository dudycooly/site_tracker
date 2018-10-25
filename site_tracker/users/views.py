from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from .forms import LoginForm, RegistrationForm
from .models import User

users = Blueprint('users', __name__)


@users.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Logged in successfully.")
        # There's a subtle security hole in this code, which we will be fixing in our next article.
        # Don't use this exact pattern in anything important.
        return redirect(request.args.get("next") or url_for("tracker.index"))
    return render_template('users/login.html', form=form)


@users.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("*"*80)
        from pprint import pprint
        pprint(form.data)
        user = User.create(**form.data)
        login_user(user)
        return redirect(url_for('tracker.index'))
    return render_template('users/register.html', form=form)


@users.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('tracker.index'))
