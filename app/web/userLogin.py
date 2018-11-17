from flask import Blueprint,session,render_template,abort
from jinja2 import  TemplateNotFound

login = Blueprint("web",__name__,static_folder='static')

@login.route('/api/login',methods = ['GET','POST'])
def hi():
    if session["user"]:
        return '11'
    return 'hello world'

@login.route("/<page>")
def show(page):
    try:
        return render_template(('templates/base/{}.html').format(page))
    except TemplateNotFound:
        abort(404)

show('login')