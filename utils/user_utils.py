'''
用户管理：
    - [ ] 登陆
    - [ ] 注册
    - [ ] 身份验证
'''



__author__ = 'smdsbz'





from functools import wraps
import sqlite3, hashlib



from globalvar import USER_DB, SALT






def signinUser(id, passwd):
    '''
    用户注册

    ARGS:
        id      用户名
        passwd  密码源码

    RETURN:
        True    注册成功
        False   注册失败
    '''
    # TODO: 非空检查交给前端处理，这里只是为了保险
    if id is '':
        return False
    elif passwd is '':
        return False
    else:
        with sqlite3.connect(USER_DB) as db:

            # check if id already used
            SQL = "SELECT ID FROM USER WHERE ID = '{}'".format(id)
            cur = db.execute(SQL)
            if cur.fetchone():  # i.e. id used already
                # flash("用户名已经存在！", category='warning')
                return False
                
            # everything OK
            else:
                treated_passwd = hashlib.sha256((SALT+passwd+id).encode('utf-8')).hexdigest()
                SQL = "INSERT INTO USER (ID, PASSWD) VALUES ('{}', '{}')".format(id, treated_passwd)
                cur = db.execute(SQL)
                db.commit()
                # flash("注册成功！请登录！", category='success')
                return True

    # General Exit
    return False
