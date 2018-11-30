from flask import session

def validate_account(username,password):
    # or and not 或与非
    if username == 'admin' and password == '123':
        session['user'] = username
        return True
    return False