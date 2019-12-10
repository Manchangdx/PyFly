from werkzeug.security import check_password_hash


class User:
    user = None
    is_active = False
    is_authenticated = True
    is_anonymous = False

    def __init__(self, user):
        self.user = user
        self.is_active = user['is_active']

    def get_id(self):
        return str(self.user['_id'])

    # 因为该方法不涉及类本身的属性，所以使用静态方法装饰器装饰它
    @staticmethod
    def validate_login(password_hash, password):
        # 此 check_password_hash 方法接收两个参数
        # 数据库中的哈希密码和用户在页面上填写的密码
        # 如果验证密码一致则返回 True ，否则返回 False
        return check_password_hash(password_hash, password)


class R(dict):
    
    @staticmethod
    def ok(msg=None, data=None):
        r = __class__()
        r.put('status', 0)
        r.put('msg', msg)
        r.put('data', data)
        return r

    @staticmethod
    def fail(status=404, msg=None):
        r = __class__()
        r.put('status', status)
        r.put('msg', msg)
        return r

    def put(self, key, value):
        self.__setitem__(key, value)

    def get_status(self):
        return self.get('status')

    def get_msg(self):
        return self.get('msg')


class BaseResult(R):
    def __init__(self, status=0, msg='', data=None):
        self.put('status', status)
        self.put('msg', msg)
        self.put('data', data)
