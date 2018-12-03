from . import web
from flask import render_template,session,redirect

@web.route('/login/')
def login():
    return render_template('login.html')