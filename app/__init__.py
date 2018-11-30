from flask import Flask
import  os
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

     # 生成随机的字符串作为sesstion秘钥
    app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
    app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。

    # 设置静态资源路径
    app.static_folder = os.path.abspath('static')

    # 注册蓝图
    register_bluepint(app)

    return app

def register_bluepint(app):
    from app.web import web
    from app.api import api

    # 在app中注册蓝图
    app.register_blueprint(web)
    app.register_blueprint(api,url_prefix="/api")