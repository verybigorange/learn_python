from flask import session,render_template,abort
from jinja2 import  TemplateNotFound
from . import  web

@web.route('/login/',methods = ['GET','POST'])
def hi():
    return render_template('hello.html',name = 'python')

# @web.route('/<page>')
# def show(page = None):
#     try:
#         return render_template(('templates/base/{}.html').format(page))
#     except TemplateNotFound:
#         abort(404)

# show('/login')