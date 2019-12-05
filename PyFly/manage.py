import os
from flask_script import Manager

from fly_bbs import create_app


config = os.environ.get('FLASK_CONFIG', 'Dev')
app = create_app(config)
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
