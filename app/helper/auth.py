from flask import session,redirect

class LoginAuth:
    @staticmethod
    def login_required(fn):
        def f(*arg,**kw):
            if not 'user' in session:
            # 重定向也需要return
                return redirect('/login')
            return fn(*arg,**kw)
        return f
        
