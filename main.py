from app import create_app

app = create_app()

# @app.route('/')
# def index():
#     return redirect(url_for('hello'))
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name = ''):
#     resp =  make_response(render_template('hello.html',name = name))
#     resp.set_cookie('test','2121212')
#     return resp

# # 登录
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('dashbord'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''
#
# # 登出
# @app.route('/loginout')
# def loginout():
#     session.pop('username',None)
#     return redirect(url_for('dashbord'))
#
# # 主界面
# @app.route('/dashbord')
# def dashbord():
#     if 'username' in session:
#         return '已经登录 %s' % (escape(session['username']))
#     else:
#         return 'you are not login in'
#
# @app.errorhandler(404)
# def notFound():
#     return render_template('404.html'), 404
#
#
# @app.errorhandler(500)
# def error(e):
#     return render_template('500.html'), 500

if(__name__ == '__main__'):
    app.run(debug = app.config['DEBUG'],port = app.config['PORT'],host = app.config['HOST'])