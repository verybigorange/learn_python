from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import os

web = Blueprint('web', __name__, template_folder=os.path.abspath('templates'))


@web.route('/<page>', methods=['GET'])
def showPage(page='index'):
    try:
        return render_template(('{}.html').format(page))
    except TemplateNotFound:
        abort(404)


# 注意这里要导入用到的视图模块
from app.web import index
from app.web import login