'''
主视图函数 & 涉及到session上下文的操作
'''


# TODO: 我希望这里人能够多一点
__author__ = None

######## Libraries & Utilities ########

#### Flask ####
from flask import Flask, session, request
from flask import render_template, redirect, url_for, flash
#### Stdlib ####
from functools import wraps

#### self-written ####
from globalvar import SECRET_KEY
from utils.user_utils import signinUser, loginUser



######## Initialization ########

app = Flask(__name__)
app.secret_key = SECRET_KEY



######## Functions ########

def login_verification(to_be_decorated):
    '''
    登录状态验证

    USAGE:
        @login_verification

    RETURN:
        success -> procedure will carry on
        fail    -> redirect to logout page (to clear up session)
    '''
    @wraps(to_be_decorated)
    def decorated(*args, **kwargs):
        if 'id' not in session:
            flash("请登录！", category='warning')
            return redirect(url_for('logout'))
        else:
            return to_be_decorated(*args, **kwargs)
    return decorated



######## Views ########

#### Login & Logout ####

@app.route('/')
def START_POINT():
    return redirect(url_for('logout'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        id = request.form.get('id', None)
        passwd = request.form.get('passwd', None)
        if loginUser(id, passwd):
            session['id'] = id
            return redirect(url_for('main_page'))
        else:
            # flash("用户名密码错误！", category='warning')
            # 直接把flash交给user_utils模块，细化操作
            return redirect(url_for('login'))
    # return

@app.route('/logout/')
def logout():
    session.pop('id', None)
    return redirect(url_for('login'))


#### Main Page ####

@app.route('/main_page/', methods=['GET', 'POST'])
@login_verification
def main_page():
    return 'Main Page'

# TODO: 是做一个单页还是多页？？等前端设计出来了再动后面的吧


######## __main__ ########

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
