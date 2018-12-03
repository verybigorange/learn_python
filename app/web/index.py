from . import web
from flask import render_template,session,redirect
from app.helper.auth import LoginAuth
# from flask_login import login_required

@web.route('/')
@LoginAuth.login_required
def index():
    return render_template('index.html')
