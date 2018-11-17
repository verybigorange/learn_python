from flask import Flask
import  os

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # 生成随机的字符串作为秘钥
    app.secret_key = os.urandom(16)

    # 注册蓝图
    register_bluepint(app)

    return app

def register_bluepint(app):
    from app.web.userLogin import login

    # 在app中注册蓝图
    app.register_blueprint(login)