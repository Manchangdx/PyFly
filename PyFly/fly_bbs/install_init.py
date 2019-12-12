from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from .extensions import mongo


def init():
    if mongo.db.users.find_one({'username': 'admin'}):
        return
    
    mongo.db.users.insert_one({
        'email': 'admin@haha.com', 
        'username': 'admin',
        'password': generate_password_hash('admin'),
        'is_admin': True,
        'renzheng': '社区超级管理员',
        'vip': 5,
        'coin': 9999,
        'avatar': '/static/images/avatar/1.jpg',
        'is_active': True,
        'created_at': datetime.utcnow()
    })

    options = [
        {'name': '网站标题', 'code': 'title', 'val': 'PyFly'},
        {'name': '网站描述', 'code': 'description', 'val': 'PyFly'},
        {'name': '网站关键字', 'code': 'keywords', 'val': 'PyFly'},
        {'name': '网站 LOGO', 'code': 'logo', 
                'val': '/static/images/logo.png'},
        {'name': '签到奖励区间（格式：1-100）', 'code': 'sign_interval', 
                'val': '1-100'},
        {'name': '开启用户注册（0 关闭，1 开启）', 'code': 'open_user',
                'val': 1},
        {'name': '管理员邮箱（申请友链时用）', 'code': 'email', 
                'val': 'admin@haha.com'},
        {'name': '底部信息（支持 HTML 代码）', 'code': 'footer', 
                'val': 'Power By PyFly'}
    ]

    mongo.db.options.insert_many(options)

    mongo.db.catalogs.insert_one({'name': '提问'})

    print(' * Initial data to MongoDB OK')
