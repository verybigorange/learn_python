from . import web
from flask import render_template,session,redirect
from app.helper.auth import LoginAuth

@web.route('/')
@LoginAuth.login_required
def index():
    return render_template('index.html')
