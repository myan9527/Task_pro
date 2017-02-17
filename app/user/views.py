from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import user
from .. import db
from ..models import User, Task
from .forms import *

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            user.update_login()
            return redirect(request.args.get('next') or url_for('user.dashboard'))
        flash('Invalid username or password.')
    return render_template('user/login.html', form=form)

@user.route('/profile', methods=['GET','POST'])
def profile():
    if not current_user.is_authenticated:
        flash('Please login first.')
        return redirect(url_for('user.login'))
    else:
        tasks = Task.get_tasks(current_user.get_id())
        return render_template('user/profile.html', user = current_user, tasks = tasks)

@user.route('/dashboard', methods = ['GET'])
def dashboard():
    if current_user.is_authenticated:
        # load basic data here
        v = [1,2,3]
        return render_template('user/dashboard.html',a = v)
    else:
        flash('Please login first.')
        return redirect(url_for('user.login'))


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Success!')
        return redirect(url_for('user.login'))
    return render_template('user/register.html', form=form)


@user.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("user/change_password.html", form=form)


@user.route('/reset', methods=['GET', 'POST'])
def password_reset_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user:
        #     token = user.generate_reset_token()
        #     send_email(user.email, 'Reset Your Password',
        #                'auth/email/reset_password',
        #                user=user, token=token,
        #                next=request.args.get('next'))
        # flash('An email with instructions to reset your password has been '
        #       'sent to you.')
        return redirect(url_for('user.login'))
    return render_template('user/reset_password.html', form=form)


@user.route('/reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            return redirect(url_for('main.index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('user.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('user/reset_password.html', form=form)

# task view
@user.route('/newtask', methods = ['GET', 'POST'])
def newtask():
    form = NewTaskCreateForm()
    return render_template('task/newtask.html', form = form)