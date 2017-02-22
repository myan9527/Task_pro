from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import user
from ..models import User, Task
from .forms import *
import json

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
@login_required
def profile():
    if not current_user.is_authenticated:
        flash('Please login first.')
        return redirect(url_for('user.login'))
    else:
        form = UserProfileForm()
        form.name.default = current_user.username
        return render_template('user/profile.html', user = current_user, form = form)

@user.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():
    if current_user.is_authenticated:
        # load basic data here
        tasks = Task.get_tasks(current_user.id)
        # data statistics
        data = Task.statistics(tasks)
        return render_template('user/dashboard.html',tasks = tasks, user = current_user, data = json.dumps(data))
    else:
        flash('Please login first.')
        return redirect(url_for('user.login'))


@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        User.add(user)
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
            # code refine
            User.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid password.')
    return render_template("user/change_password.html", form=form)

# task view
@user.route('/newtask', methods = ['GET','POST'])
def newtask():
    form = NewTaskCreateForm()
    if form.validate_on_submit():
        task = Task()
        task.taskname = form.name.data
        task.user_id = current_user.get_userid()
        # add it to db
        Task.add(task)
        return redirect(request.args.get('next') or url_for('user.taskdetail',task)) 
    return render_template('task/newtask.html', form = form)

@user.route('/taskdetail', methods = ['GET','POST'])
def taskdetail(task):
    return render_template('task/taskdetail',task = task)
