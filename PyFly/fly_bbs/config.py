import os
from flask_uploads import ALL


class DevConfig:
    '''开发环境配置'''

    MONGO_URI = 'mongodb://localhost:27017/pyfly'
    # 这里使用环境变量 SECRET_KEY 来设置该字段的值以策安全
    # 在启动应用前，需要先设置环境变量，否则使用第二个参数作为缺省值
    SECRET_KEY = os.environ.get('SECRET_KEY', 'shiyanlou')
    # 禁用 CSRF 认证
    WTF_CSRF_ENABLED = False
    # 配置允许的扩展名
    UPLOADED_PHOTOS_ALLOW = ALL
    # 配置上传照片的目录
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'uploads/pics')
    # 配置上传文件的目录
    UPLOADED_FILES_DEST = os.path.join(os.getcwd(), 'uploads/files')


class ProConfig(DevConfig):
    '''生产环境配置'''


configs = {
        'Dev': DevConfig,
        'Pro': ProConfig
}
