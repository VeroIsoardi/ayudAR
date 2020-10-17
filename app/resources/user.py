from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.user import User
from app.db import base
from app.helpers.auth import authenticated
from datetime import datetime
from app.models.rol import Rol
from app.models.usersRoles import UsersRoles
from app.models.pageSetting import PageSetting


# Protected resources
def index(num_page):
    """ if not authenticated(session):
        abort(401) """
    params = []
    quantity=PageSetting.find_settings()
    users = base.session.query(User).filter(User.deleted==False).paginate(per_page=quantity.elements, page=num_page, error_out= True)
    num_pages=users.iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2)
    params.append(users)
    params.append(num_pages)
    return params

def login():
    return render_template("auth/login.html")


def new():
    #if not authenticated(session):
    #    abort(401)
    return render_template("user/new.html")


def create():
    #if not authenticated(session):
    #    abort(401)
    params = request.form
    mensaje = User.create(params)
    flash(mensaje)
    return redirect(url_for("user_index"))


def delete(id):
    user = User.find_by_id(id)
    return render_template("user/delete.html",user = user)


def commit_delete():
    params = request.form
    mensaje = User.delete(params)
    flash(mensaje)
    return redirect(url_for("user_index"))


def commit_update():
    params = request.form    
    if request.method == 'POST':
        lista = request.form.getlist('roles[]')
    UsersRoles.get_data(params['id'],lista)
    user = User.find_by_id(params['id'])   
    mensaje = user.update(params)   
    flash(mensaje[0], mensaje[1])
    if mensaje[1] == 'success':
        return redirect(url_for("user_index"))
    else:
        return redirect(url_for('user_update',id=params['id']))


def user_back(id):
    return User.find_by_id(id)


def update(id):
    all_roles = Rol.return_roles()
    user_roles = UsersRoles.find_user_roles_by_id(id)
    roles_name_user = Rol.get_name_roles(user_roles)    
    roles = []
    for item in all_roles:
        if item not in roles_name_user:
            roles.append(item)
    user = User.find_by_id(id)
    return render_template("user/update.html",user = user, all_roles = roles, user_roles = roles_name_user)
