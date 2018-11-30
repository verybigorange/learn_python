from . import web
from flask import render_template,session,redirect

@web.route('/')
def index():
    if not 'user' in session:
        # 重定向也需要return
        return redirect('/login')
    return render_template('index.html')
