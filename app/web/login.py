from flask import session,render_template,abort
from jinja2 import  TemplateNotFound
from . import  web

@web.route('/login/',methods = ['GET','POST'])
def hi():
    return 'hello world'

# @login.route("/<page>")
# def show(page):
#     try:
#         return render_template(('templates/base/{}.html').format(page))
#     except TemplateNotFound:
#         abort(404)
#
# show('login')