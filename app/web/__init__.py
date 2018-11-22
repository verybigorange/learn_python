from flask import Blueprint

web = Blueprint('web',__name__)

# 注意这里要导入用到的视图模块
from app.web import login