from flask import Blueprint
import os

web = Blueprint('web',__name__,template_folder = os.path.abspath('templates'))

# 注意这里要导入用到的视图模块
from app.web import login