from . import api
from flask import jsonify,request

from app.servers.login import validate_account

@api.route('/login',methods = ['POST'])
def login():
    if validate_account(request.form['username'],request.form['password']):
        return jsonify(code  = 200,msg = "登录成功")
    return jsonify(code = 400,msg = "账户或者密码不正确")