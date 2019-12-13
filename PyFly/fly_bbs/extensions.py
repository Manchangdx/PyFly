from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL
from bson import ObjectId

from .models import User


mongo = PyMongo()
# 创建 LoginManager 类的实例
login_manager = LoginManager()
# 定义处理登录页的路由函数
# 如果用户未登录时访问了需要登录才能访问的页面
# 会自动跳转到此处提供的视图函数所指向的页面
login_manager.login_view = 'user_view.login'

# 使用该装饰器的作用是将 user_load 方法
# 设置为 login_manager 的 user_callback 属性
# 以便能够在需要的时候使用 user_id 参数找到对应的用户数据
@login_manager.user_loader
def user_load(user_id):
    # 如果 user_id 存在，find_one 方法返回字典对象
    # 否则返回 None
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    return User(user)

# 实例化图片上传对象，extensions 参数代表允许扩展名
upload_photos = UploadSet(extensions=ALL)


def init_extensions(app):
    # 初始化 app 的时候，会调用 app.config 的 MONGO_URI 属性
    # MONGO_URI = 'mongodb://localhost:27017/pyfly'
    # 以确定要连接的数据库名字 pyfly 、端口号 27017
    # 并且给 mongo 定义一个 db 属性，其值就是数据库 pyfly
    mongo.init_app(app)
    # 调用 init_app 方法注册 app 
    # 此方法的主要作用就是将 login_manager 本身赋值给 app.login_manager 属性
    # 以便 app 能够使用其登录登出等功能
    login_manager.init_app(app)
    # 获取配置信息并存储在 app 上
    configure_uploads(app, upload_photos)
